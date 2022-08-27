import json

# mudar o nome do arquivo JSON, para ser carregado pelo python
with open("antecipo5122.json", encoding='utf-8') as meu_JSON:
    dados = json.load(meu_JSON)


print('\n'
      '*****************************************************************************\n'
      '**  Sistema criado para listar os erros encontrados na cessão da Antecipo  **\n'
      '*****************************************************************************'
      '\nComece digitendo a quantidade de erros\n')

numErros = int(input('Quantos erros tivemos: '))


listaErros = []
for i in range(numErros):
    numeroCCbs = input("Digite a CCB: ")
    listaErros.append(numeroCCbs)

contador = 0
for j in range(numErros):
    numExt = listaErros.pop()
    for i in dados:
        if numExt == i['number']:
            contador += 1
            numCCB = i['number']
            nome = i['issuer_name']
            numCPF = i['issuer_cpf']
            print(f'Erro n: {contador}\nCCB: {numCCB} \nNome: {nome}')
            #print('CPF: ' + numCPF[-11:-9]+'.'+numCPF[-9:-6]+'.'+numCPF[-6:-3]+'-'+numCPF[-3:-1]+'\n')
            print('CPF: ' + numCPF[3:6]+'.'+numCPF[6:9] +
                  '.'+numCPF[9:12]+'-'+numCPF[12:14]+'\n')
