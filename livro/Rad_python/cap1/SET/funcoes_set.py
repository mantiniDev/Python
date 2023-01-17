# é uma coleção de valores que possibilita a execução de uma série de operações de conjuntos como:


#printar (item a ser printado, nome do item)
def printar(i, nome):
    print(f'{nome}: {i}')

#union (|)
def uniao(S1, S2):
    S3 = S1|S2
    return S3

#interseção (&)
def intersecao(S1, S2):
    S3 = S1&S2
    return S3

#diferença (-)
def diferenca(S1, S2):
    S3 = S1-S2
    return S3

#diferença simétrica
def def_simetrica(S1, S2):
    S3 = S1^S2
    return S3

#retorna um numero de itens
def n_itens(S):
    resp = len(S)
    return resp

#retorna o maior valor de um SET
def maior_valor(S):
    resp = max(S)
    return resp

#retorna o menor valor de um SET
def menor_valor(S):
    resp = min(S)
    return resp

#retorna a soma de itens de um SET
#duplicados só se considera uma vez
def soma(S):
    resp = sum(S)
    return resp

#retorna true se existe item do SET for True
def verdadeiro(S):
    resp = any(S)
    return resp

#retorna true se todos forem true no SET
def tudo_verdadeiro(S):
    resp = any(S)
    return resp

#ordena a SET
def ordenar(S):
    resp = sorted(S)
    return resp

#limpa a SET
def limpar(S):
    resp = clear(S)
    return resp

#retira um item arbitrário
def remover_aleatorio(S):
    resp = pop(S)
    return resp    