# ELEIÇÕES PREEITURA DO RIO DE JANEIRO

import os

nulo = antonio = jose = maria = branco = total = 0

while True:
    os.system('CLS')
    print(f'[1] Antonio\n'
            f'[2] José\n'
            f'[3] Maria\n'
            f'[4] BRANCO\n'
            f'[ ] NULO')
    
    voto = int(input('Qual o seu voto? (0 para encerrar) '))

    if voto != 0:
            total += 1
    
    if voto not in range(5):
        nulo += 1
    elif voto == 1:
        antonio += 1
    elif voto == 2:
        jose += 1
    elif voto == 3:
        maria += 1
    elif voto == 4:
        branco += 1
    elif voto == 0:
        print('Votação encerrada!')
        break

os.system('CLS')
print('#' * 22)
print('RESULTADO DAS ELEIÇÕES')
print('#' * 22)
print(f'Candidato Antonio obteve {antonio} votos!\n'
      f'Candidato José obteve {jose} votos!\n'
      f'Candidata Maria obteve {maria} votos!\n'
      f'Votos em Branco = {branco}\n'
      f'Votos nulos = {nulo}\n\n'
      f'Eleitores que compareceram às urnas = {total}')

if antonio == jose or antonio == maria or jose == maria:
    print('VOTAÇÃO EM SEGUNDO TURNO')
elif antonio > jose and antonio > maria:
    print('CANDIDATO ELEITO: ANTONIO!')
elif jose > antonio and jose > maria:
    print('CANDIDATO ELEITO: JOSÉ!')
elif maria > antonio and maria > jose:
    print('CANDIDATO ELEITO: MARIA!')