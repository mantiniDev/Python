# breack - permite a execução do código saída de um determinado loop;

# continue - faz a execução retornar ao início, não executando o restante de código após sua declaração;

# pass - não faz nada, consiste em uma declaração vazia. 

k = 0
while true:
    k = k+1
    if (k <= 10):
        print(k)
    if (k == 11):
        break

k = 1
while k <= 10:
    if k==7 or k==9:
        k+=1
        continue
    print (k)
    k=k+1

k=1
while k <= 10:
    if k==7:
        pass
    else:
        print(k)
    k+=1