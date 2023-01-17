# Compreende a combinação pares de chave/valores (KEY/VALUE) únicos, onde os valores dos pares são separados por ":" e os pares são separados por ",". Também, são imutáveis. 

paises = {'Brasil':'Brasilia', 'Argentina': 'Buenos Aires', 'Bolivia':'La Paz',}

n = input('Forneça o país: \n')
if n in paises:
    print (f'A capital de {n} é', paises[n])
else:
    print(f'O país: {n}, não consta no dicionário')
    
paises['Australia'] = 'Sweden'
print('\n')
print(f'O dicionario de Paises ficou dessa forma: ')

for PAISES, CAPITAIS in paises.items():
    print(f'A capital de {PAISES} é {CAPITAIS}')
print('\n')
m = input('Digite o pais a ser apagado? ')
del paises[m]
print(f'O dicionario após a exclusão ficou dessa forma: ')

for PAISES, CAPITAIS in paises.items():
    print(f'A capital de {PAISES} é {CAPITAIS}')

print('\n')
print('Os dados de Paises são: ', paises.items())
print('\n')
print('As Chaves de Paises são: ', paises.keys())
print('\n')
paises2 = {'Uruguai':'Montevidéu'}

paises.update(paises2)

print(f'O dicionario versão dinal ficou dessa forma: ')

for PAISES, CAPITAIS in paises.items():
    print(f'A capital de {PAISES} é {CAPITAIS}')




