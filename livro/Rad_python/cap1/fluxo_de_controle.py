# if/else

m = int(input("Digite sua idade: "))

if(m>60):
    print('Você é da terceira idade.')
else:
    print('Você ainda não chegou na terceira idade.')
    

# if/elif/else

maiorIdade = 18

m1 = int(input('Qual a sua idade: '))

if(m1>60):
    print('Você é da terceira idade.')

elif (m1 >= maiorIdade and m1 < 60):
    print('Você tem a maior idade Penal.')
    
else:
    print('Você ainda não chegou na terceira idade.')
    