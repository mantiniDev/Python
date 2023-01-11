# Utilizados para armazenar em diferentes posições valores distintos
# uma dimensão - unidimensionais - envolve somente linhas;
# duas dimensões - bidimensionais - envolvem linhas e colunas

x = [0 for i in range(5)]

for i in range(5):
    x[i] = i + 1
    print(x[i])
    i+=1
    
for i in range(5):
    print("Digite o numero %s de 5 \n" %(i+1))
    x[i] = input()

for i in range(5):
    print(x[i])