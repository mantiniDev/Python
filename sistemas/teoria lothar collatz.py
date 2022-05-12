
co = int(input("Digite um núemro: "))
cont = 0
while co != 1:
    if co % 2 == 0:
        resp = co/2
        print(resp)
        co = resp
        cont +=1
    else:
        resp = (3*co)+1
        print(resp)
        co = resp
        cont +=1
print ("Passos:",cont)
    
    