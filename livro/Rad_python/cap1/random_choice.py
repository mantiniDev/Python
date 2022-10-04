# sorteia números aleatórios em uma faixa de valores
from random import choice

for i in range(6):
    r = choice(range(1,61))    
    print(f'Numero : {r}')