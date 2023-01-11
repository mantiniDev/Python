# É a coleção de elemento que pode compreender outras lsitas

x = [1,2,3,4,[5,6],7]

print(x[0])
print(x[-1])
print(x[-2])
print(x[4])


nomes = ['Beltrano', 'Ciclano', 'Deltrano', 'Joziano']

x = input('Digite um nome: ')

if x in nomes:
    print(f'Nome: {x} - encontrado')
else:
    print(f'Nome: {x} - não encontrado')
