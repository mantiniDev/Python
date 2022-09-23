lista = [1, 3, 4, 5]

x = lista.pop(3)
y = lista.remove(4)

print(lista)
print(x)
print(y)

valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um elemento para a lista:')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('FIM')
                             
