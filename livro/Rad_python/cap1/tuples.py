# É um tipo de sequencia de strings que não permite a alteração de seus valores

#nomes = ('joão', 'Kelly', 'Caroline', 'Estive', 'Karine')

nomes2 = [
    {'nome': 'paulo', 'idade': 35},
    {'nome': 'camilla', 'idade': 32},
    {'nome': 'ben', 'idade': 2}
]

n = input('Forneça um nome para pesquisa: ')


for pessoa in nomes2:
    if pessoa['nome'] == n:
        print(f'O nome {n} foi encontrado!!')
    else:
        print()




