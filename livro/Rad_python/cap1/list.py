# É a coleção de elemento que pode compreender outras lsitas

x = [1,2,3,4,[5,6],7]

print(x[0])
print(x[-1])
print(x[-2])
print(x[4])


nomes = ['Beltrano', 'Ciclano', 'Deltrano', 'Joziano']

# x = input('Digite um nome: ')

#if x in nomes:
   # print(f'Nome: {x} - encontrado')
#else:
   # print(f'Nome: {x} - não encontrado')

# operações: retorno de partes inclusão, exclusão nas listas

print(nomes[3])
print(nomes[:3])
print(nomes[3:])
print(nomes[-4:-2])

nomes.insert(0, 'Benjamin') #insere o nome na primeira posição
print(nomes)
nomes.pop(0) # ele retira o valor, mas esse valor pode ser utilizado, retornado sempre (indice)
print(nomes)
del nomes[1] # ele retira o valor e o deleta definitivamente (indice)
print(nomes)
nomes.remove('Deltrano') # remove utilizando um valor(valor)
print(nomes)
nomes.reverse() # inverte a lista
print(nomes)
nomes.sort() # ordena a lista
print(nomes)
q = nomes.count('Joziano') # retorna a quantidade de vezes que um mesmo elemento está contido numa lista
print(q)