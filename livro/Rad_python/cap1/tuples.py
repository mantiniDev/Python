# É um tipo de sequencia de strings que não permite a alteração de seus valores

nomes = ('joão', 'Kelly', 'Caroline', 'Estive', 'Karine')

n = input('Forneça um nome para pesquisa: ')

if n in nomes:
    print(f'O nome {n} foi encontrado!!')
else:
    print(f'O nome {n} NÂO foi encontrado!!')




