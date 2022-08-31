lista = ['Paulo', 'Camilla', 'Benjamin', 'Edu', 'Thais', 'Fany']

ausente = lista.pop(5)
print(f'{ausente} não podera comparecer')

newConvidado = input('Novo Convidado: ')
lista.append(newConvidado)

for i in range(0,6):
    print(f'{lista[i]} voce esta convidado para a festa!!!!')
 

