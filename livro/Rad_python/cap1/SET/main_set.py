import funcoes_set

S1 = set([3,5,6,10,11,100])
S2 = set([1,5,3,6,15,11])

u = funcoes_set.uniao(S1, S2)
funcoes_set.printar(u, 'União')
print(25*'*')

i = funcoes_set.intersecao(S1, S2)
funcoes_set.printar(i, 'Interseção')
print(25*'*')

d = funcoes_set.diferenca(S1, S2)
d1 = funcoes_set.diferenca(S2, S1)
d2 = funcoes_set.def_simetrica(S1, S2)
print(f'Diferença de {S1} - {S2}: {d} ')
print(f'Diferença de {S2} - {S1}: {d1} ')
funcoes_set.printar(d2, 'Diferença Simetrica')
print(25*'*')

e1 = funcoes_set.n_itens(S1)
funcoes_set.printar(e1,'S1 possui :')
e2 = funcoes_set.n_itens(S2)
funcoes_set.printar(e2,'S1 possui :')
print(25*'*')

f1 = funcoes_set.maior_valor(S1)
funcoes_set.printar(f1, 'Maior valor: ')
f2 = funcoes_set.maior_valor(S2)
funcoes_set.printar(f2, 'Maior valor: ')
print(25*'*')

g1 = funcoes_set.menor_valor(S1)
funcoes_set.printar(g1, 'Menor valor: ')
g2 = funcoes_set.menor_valor(S2)
funcoes_set.printar(g2, 'Menor valor: ')
print(25*'*')

h1 = funcoes_set.soma(S1)
funcoes_set.printar(h1,'Soma dos itens')
h2 = funcoes_set.soma(S2)
funcoes_set.printar(h2,'Soma dos itens')
print(25*'*')

i1 = funcoes_set.verdadeiro(S1)
funcoes_set.printar(i1,'Verdadeiro: ')
i2 = funcoes_set.verdadeiro(S2)
funcoes_set.printar(i1,'Verdadeiro: ')
print(25*'*')

j1 = funcoes_set.tudo_verdadeiro(S1)
funcoes_set.printar(j1,'Todos Verdadeiros: ')
j2 = funcoes_set.tudo_verdadeiro(S2)
funcoes_set.printar(j2,'Todos Verdadeiros: ')
print(25*'*')

k1 = funcoes_set.ordenar(S1)
print(f'SET {S1} ordenada: {k1}')
k2 = funcoes_set.ordenar(S2)
print(f'SET {S2} ordenada: {k2}')
print(25*'*')

#l1 = funcoes_set.limpar(S1)
#print(f'SET limpa: {S1}')
#l1 = funcoes_set.limpar(S2)
#print(f'SET limpa: {S2}')
#print(25*'*')

m1 = funcoes_set.remover_aleatorio(S1)
funcoes_set.printar(m1, 'Item retirado: ')
print(25*'*')

