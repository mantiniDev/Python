locadora = list()
acervo = dict()


for cont in range(0,2):
    acervo['Titulo'] = str(input('Qual o nome do Filme: '))
    acervo['Ano'] = str(input('Qual o ano do filme: '))
    acervo['Diretor'] = str(input('Qual o diretor do filme: '))
    #locadora.append(acervo)
    locadora.append(acervo.copy())
print(locadora)