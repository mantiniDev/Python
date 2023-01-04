# partition(separador) - quebra uma string em 3 partes

frase = ("Vamos estudar python. Estudar python é muito bom")
print(frase.partition("-"))

# split(separador,[n]) - quebra uma string em partes retornando um array. Se o separador não for especificado, é considerado espaço em branco. Escapes são considerados espaço em branco.

# print(frase.split("p",["P"]))

#splitlines(bollean) - quebra uma string em partes conforme novas linhas (\n) Caso True - mostrará a quebra (\n) senão False

#expandtabs() - quebra uma string em nova linhas confomre escape "\n"
# replace(termo, novotermo,ocorrencia) - substitui um termo em uma quantidade de ocorrência.abs(x)