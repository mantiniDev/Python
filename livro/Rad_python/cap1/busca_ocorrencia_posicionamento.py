# count(s,inicio,final) - retorna a quantidade de ocorrências de um valor em uma string

nome = 'Python 33' 
print(nome.count('3',0,len(nome)))

# find(s,inicio,final) - retorna o valor da primeira ocorrência de um valor em uma string

print(nome.find('3',0,len(nome))) #obs no livro

# index(s,inicio,final) - retorna a primeira posição da ocorência de um valor em uma string.

print(nome.index('3',0,len(nome))) #obs no livro, pg. 21. 

# rfind(s,inicio,final) - retorna a última posição da ocorrência de um valor em uma string.

print(nome.rfind('3', 0, len(nome)))