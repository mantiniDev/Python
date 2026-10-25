#!/usr/bin/env bash
# Otimizações para Linux no Acer Chromebook 11 C731 (placa "RELM")
#   CPU: Intel Celeron N3060 (Braswell, 2 núcleos)
#   RAM: 4 GB | Armazenamento: eMMC 16/32 GB | Vídeo: Intel HD 400
#
# Uso:
#   sudo bash otimizar.sh          -> pergunta antes de cada passo
#   sudo bash otimizar.sh -y       -> aplica tudo que é recomendado sem perguntar
#   bash otimizar.sh --info        -> só mostra o diagnóstico (não altera nada)
#
# Funciona em distros baseadas em Debian/Ubuntu (apt), Fedora (dnf) e Arch (pacman).
# Tudo que o script cria fica em arquivos próprios (*chromebook*), fáceis de remover.

set -uo pipefail

AUTO=0
SO_INFO=0
for arg in "$@"; do
    case "$arg" in
        -y|--sim) AUTO=1 ;;
        --info) SO_INFO=1 ;;
        -h|--help) sed -n '2,13p' "$0"; exit 0 ;;
        *) echo "Opção desconhecida: $arg"; exit 1 ;;
    esac
done

verde() { printf '\e[32m%s\e[0m\n' "$*"; }
amarelo() { printf '\e[33m%s\e[0m\n' "$*"; }
titulo() { printf '\n\e[1;36m== %s ==\e[0m\n' "$*"; }

# perguntar "texto" [padrao s/n]
perguntar() {
    local padrao="${2:-s}"
    if [[ $AUTO -eq 1 ]]; then
        [[ $padrao == s ]]
        return
    fi
    local opcoes="[S/n]"
    [[ $padrao == n ]] && opcoes="[s/N]"
    read -rp "$1 $opcoes " resp
    resp="${resp:-$padrao}"
    [[ ${resp,,} == s* ]]
}

tem() { command -v "$1" >/dev/null 2>&1; }

servico_existe() { systemctl list-unit-files "$1" 2>/dev/null | grep -q "^$1"; }

# ---------------------------------------------------------------------------
# Diagnóstico
# ---------------------------------------------------------------------------
diagnostico() {
    titulo "Diagnóstico do sistema"
    . /etc/os-release 2>/dev/null
    echo "Distro:        ${PRETTY_NAME:-desconhecida}"
    echo "Kernel:        $(uname -r)"
    echo "Ambiente:      ${XDG_CURRENT_DESKTOP:-${DESKTOP_SESSION:-desconhecido}}"
    echo "Modelo:        $(cat /sys/class/dmi/id/product_name 2>/dev/null || echo '?')"
    echo "Firmware:      $(cat /sys/class/dmi/id/bios_vendor 2>/dev/null) $(cat /sys/class/dmi/id/bios_version 2>/dev/null)"
    echo "CPU:           $(grep -m1 'model name' /proc/cpuinfo | cut -d: -f2 | xargs)"
    echo "Governor CPU:  $(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor 2>/dev/null || echo '?')"
    echo
    free -h
    echo
    echo "Swap ativo:"
    swapon --show 2>/dev/null || true
    echo
    df -h / | tail -n +1
    echo
    echo "Swappiness:    $(cat /proc/sys/vm/swappiness)"
    if tem aplay; then
        echo "Placas de som: $(aplay -l 2>/dev/null | grep -c '^card') encontrada(s)"
    fi
    if tem systemctl; then
        echo
        echo "Serviços que mais demoraram no boot:"
        systemd-analyze blame 2>/dev/null | head -n 8
    fi
    if tem snap; then
        echo
        amarelo "Snap está instalado (consome RAM e disco; veja o README)."
    fi
}

if [[ $SO_INFO -eq 1 ]]; then
    diagnostico
    exit 0
fi

if [[ $EUID -ne 0 ]]; then
    echo "Rode com sudo: sudo bash $0"
    exit 1
fi

# ---------------------------------------------------------------------------
# Gerenciador de pacotes
# ---------------------------------------------------------------------------
if tem apt-get; then
    PM=apt
    instalar() { DEBIAN_FRONTEND=noninteractive apt-get install -y "$@"; }
    apt-get update -qq
elif tem dnf; then
    PM=dnf
    instalar() { dnf install -y "$@"; }
elif tem pacman; then
    PM=pacman
    instalar() { pacman -S --needed --noconfirm "$@"; }
else
    echo "Gerenciador de pacotes não suportado (esperado apt, dnf ou pacman)."
    exit 1
fi

diagnostico

# ---------------------------------------------------------------------------
# 1. zram: swap comprimido na RAM (o ganho mais perceptível com 4 GB)
# ---------------------------------------------------------------------------
titulo "1. zram (swap comprimido na memória)"
echo "Faz os 4 GB renderem como ~6-7 GB e evita usar o eMMC como swap."
if perguntar "Configurar zram?"; then
    case $PM in
        apt)
            instalar zram-tools
            cat > /etc/default/zramswap <<'EOF'
# Configurado por otimizar.sh (Chromebook C731)
ALGO=zstd
PERCENT=60
PRIORITY=100
EOF
            systemctl restart zramswap.service
            ;;
        dnf|pacman)
            [[ $PM == pacman ]] && instalar zram-generator
            [[ $PM == dnf ]] && instalar zram-generator-defaults
            cat > /etc/systemd/zram-generator.conf <<'EOF'
# Configurado por otimizar.sh (Chromebook C731)
[zram0]
zram-size = ram * 0.6
compression-algorithm = zstd
swap-priority = 100
EOF
            systemctl daemon-reload
            systemctl restart systemd-zram-setup@zram0.service
            ;;
    esac
    verde "zram ativo."
fi

# ---------------------------------------------------------------------------
# 2. Ajustes de memória do kernel
# ---------------------------------------------------------------------------
titulo "2. Ajustes de memória (sysctl)"
if perguntar "Aplicar ajustes de memória pensados para zram?"; then
    cat > /etc/sysctl.d/99-chromebook.conf <<'EOF'
# Configurado por otimizar.sh (Chromebook C731)
# Com zram, mandar páginas pouco usadas para o swap comprimido é barato.
vm.swappiness = 150
# zram não se beneficia de leitura antecipada de páginas.
vm.page-cluster = 0
# Mantém em cache a estrutura de diretórios por mais tempo.
vm.vfs_cache_pressure = 50
EOF
    sysctl --system >/dev/null
    verde "Ajustes aplicados."
fi

# ---------------------------------------------------------------------------
# 3. earlyoom: evita o travamento total quando a memória acaba
# ---------------------------------------------------------------------------
titulo "3. earlyoom (evita congelamento por falta de memória)"
if systemctl is-enabled systemd-oomd.service >/dev/null 2>&1; then
    echo "systemd-oomd já está ativo nesta distro; pulando."
elif perguntar "Instalar earlyoom?"; then
    instalar earlyoom
    systemctl enable --now earlyoom.service
    verde "earlyoom ativo."
fi

# ---------------------------------------------------------------------------
# 4. Cuidados com o eMMC
# ---------------------------------------------------------------------------
titulo "4. eMMC (TRIM semanal e logs menores)"
if perguntar "Ativar TRIM semanal e limitar os logs do sistema a 50 MB?"; then
    systemctl enable --now fstrim.timer
    mkdir -p /etc/systemd/journald.conf.d
    cat > /etc/systemd/journald.conf.d/00-chromebook.conf <<'EOF'
# Configurado por otimizar.sh (Chromebook C731)
[Journal]
SystemMaxUse=50M
EOF
    systemctl restart systemd-journald
    journalctl --vacuum-size=50M >/dev/null 2>&1
    verde "TRIM e limite de logs configurados."
fi

# ---------------------------------------------------------------------------
# 5. Bateria e temperatura
# ---------------------------------------------------------------------------
titulo "5. Bateria e temperatura (TLP + thermald)"
if perguntar "Instalar TLP e thermald?"; then
    # TLP conflita com power-profiles-daemon / tuned-ppd
    for s in power-profiles-daemon.service tuned.service tuned-ppd.service; do
        servico_existe "$s" && systemctl disable --now "$s" 2>/dev/null
    done
    instalar tlp thermald
    systemctl enable --now tlp.service thermald.service
    verde "TLP e thermald ativos."
fi

# ---------------------------------------------------------------------------
# 6. Aceleração de vídeo (Intel HD 400 / Braswell usa o driver i965)
# ---------------------------------------------------------------------------
titulo "6. Aceleração de vídeo por hardware"
echo "Deixa vídeos (YouTube etc.) bem mais leves para a CPU."
if perguntar "Instalar driver VA-API i965?"; then
    case $PM in
        apt) instalar i965-va-driver vainfo ;;
        dnf) instalar libva-intel-driver libva-utils \
                 || amarelo "No Fedora o pacote pode exigir o repositório RPM Fusion." ;;
        pacman) instalar libva-intel-driver libva-utils ;;
    esac
    mkdir -p /etc/environment.d
    echo "LIBVA_DRIVER_NAME=i965" > /etc/environment.d/90-chromebook-vaapi.conf
    verde "Driver instalado (vale após reiniciar; teste com: vainfo)."
fi

# ---------------------------------------------------------------------------
# 7. Serviços que normalmente não são necessários
# ---------------------------------------------------------------------------
titulo "7. Desativar serviços desnecessários"
declare -A DESCRICAO=(
    [ModemManager.service]="modem 3G/4G (o C731 não tem)"
    [cups.service]="impressão (desative se não usa impressora)"
    [cups-browsed.service]="busca de impressoras na rede"
    [bluetooth.service]="Bluetooth (desative se não usa fone/mouse BT)"
    [avahi-daemon.service]="descoberta de dispositivos na rede local"
)
for s in ModemManager.service cups-browsed.service cups.service avahi-daemon.service bluetooth.service; do
    servico_existe "$s" || continue
    systemctl is-enabled "$s" >/dev/null 2>&1 || continue
    padrao=n
    [[ $s == ModemManager.service || $s == cups-browsed.service ]] && padrao=s
    if perguntar "Desativar ${DESCRICAO[$s]}?" "$padrao"; then
        systemctl disable --now "$s" 2>/dev/null
        [[ $s == avahi-daemon.service ]] && systemctl disable --now avahi-daemon.socket 2>/dev/null
        [[ $s == cups.service ]] && systemctl disable --now cups.socket cups.path 2>/dev/null
        verde "$s desativado (reativar: sudo systemctl enable --now $s)."
    fi
done

# ---------------------------------------------------------------------------
# 8. Limpeza
# ---------------------------------------------------------------------------
titulo "8. Limpeza de pacotes"
if perguntar "Remover pacotes órfãos e limpar o cache de pacotes?"; then
    case $PM in
        apt) apt-get autoremove --purge -y && apt-get clean ;;
        dnf) dnf autoremove -y && dnf clean all ;;
        pacman)
            orfaos=$(pacman -Qdtq || true)
            [[ -n $orfaos ]] && pacman -Rns --noconfirm $orfaos
            pacman -Sc --noconfirm
            ;;
    esac
    verde "Limpeza concluída."
fi

titulo "Pronto"
echo "Reinicie o Chromebook para tudo entrar em vigor."
echo "Depois rode 'bash otimizar.sh --info' para conferir o resultado."
echo "Próximos passos (áudio, teclas do Chromebook, firmware): veja o README.md."
