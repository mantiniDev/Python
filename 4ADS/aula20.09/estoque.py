estoque = list()
itens = dict()

for i in range(0,2):
    itens['Codigo'] = int(input('Digite o código de barras: '))
    itens['Nome'] = str(input('Digite o nome do Produto: '))
    itens['Marca'] = str(input('Qual a marca do produto: '))
    itens['Quantidade'] = int(input('Quantiade: '))
    itens['Preço'] = float(input('Preço: '))
    estoque.append(itens)
print('O estoque possui: \n')
for x in estoque:
    for i, t in itens.items():
        print(f'{i} = {t}')
     