#agenda pratica v 1.0
import os
import sqlite3 as conector
from sqlite3 import Error
from time import sleep
from pacotes.uteis import esquema, linha1, linha2, limpa, menu

# carrega esquema de banco de dados
esquema()

conexao = None
cursor = None

#função conexão banco 
def banco():
    caminho = 'E:\projetoPython\4ADS\aula25_10\agenda.db'
    try:
        conexao = conector.connect(caminho)
    except Error as ex:
        print(ex)
    return conexao
    
#funcao de busca
def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Operação concluida')

#verifica
def verificar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    result = c.fetchall()
    return result       

#inserir nova tupla
def inserir():
    vcon = banco()
    vnome = str(input('Nome: '))
    vtelef = str(input('Telefone: '))
    vsql = "INSERT INTO agenda (nome, telef) VALUES ("+vnome+","+vtelef+")"
    query(vcon, sql)
    sleep(1)
    vcon.close()

#remoção de registro
def apagar():
    vcon = banco()
    vid = str(input('Id do registro a ser apagado: '))
    vsql = "DELETE FROM agenda WHERE id ="+vid
    query(vcon, vsql)
    sleep(1)
    vcon.close()

#atualização de dados
def atualizar():
    vcon = banco()
    vid = str(input('Id do registro a ser alterado: '))
    res = verificar(vcon, "SELECT * FROM agenda WHERE id="+vid)
    resnome = res[0][1]
    restelef = res[0][2]
    vnome = str(input('Digite Novo Nome: '))
    vtelef = str(input('Digite Novo Telefone: '))
    if (len(vnome)==0):
        vnome = resnome
    if (len(vtelef)==0):
        vtelef = restelef
    vsql = "UPDATE agenda SET nome='"+vnome+", telef= "+vtelef+"' WHERE id="+vid
    query(vcon, vsql)
    sleep(1)
    vcon.close()

# consultar todos os registro
def listar():
    vcon = banco()
    vlim = 10
    vcont = 0
    vsql = "SELECT * FROM agenda"
    res = verificar(vcon, vsql)
    linha2()
    for r in res:
        print(f'| Id: {r[0]: <3}| Nome: {r[1]: <15}| Telefone: {r[2]: <15}|')
    vcont += 1
    if vcont >= vlim:
        vcont = 0
    os.system('PAUSE')
    linha2()
    os.system('PAUSE')
    vcon.close()

# consulta registro por nome
def consultar():
    vcon = banco()
    vnome = str(input('Qual o nome a consultar? ')).capitalize()
    vsql = "SELECT * FROM agenda WHERE nome LIKE '%"+vnome+"%'"
    res = verificar(vcon, vsql)
    vlim = 2
    vcont = 0
    limpa()
    for r in res:
        print(f'Id: {r[0]} \nNome: {r[1]} \nTelefone: {r[2]}')
    vcont += 1
    linha1()
    if vcont >= vlim:
        vcont = 0
    os.system('PAUSE')
    limpa()
    os.system('PAUSE')
    vcon.close()

# PROGRAMA PRINCIPAL
op = 0

while op != 6:
    menu()
    op = (input('Opção: '))
if op == 1:
    inserir()
elif op == 2:
    apagar()
elif op == 3:
    atualizar()
elif op == 4:
    os.system('CLS')
    listar()
elif op == 5:
    consultar()
elif op ==6:
    print('\033[1;31m* * * Fim de Programa * * *\033[m')
    exit()
else:
    print('Opção inválida!')
    os.system('PAUSE')
    
os.system('PAUSE')