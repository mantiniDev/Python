# PACOTE Uteis

# LINHA DUPLA
def linha():
    print('=' *30)

# LINHA SIMPLES
def linha1():
    print('-' *30)

# LINHA ENFEITADA
def linha2():
    print('-=' *30)

# LIMPA A TELA
def limpa():
    for c in range(1, 25):
        print(' ' *80)

# ESQUEMA DE BANCO DE DADOS
def esquema():
    import sqlite3 as conector
    conexao = None
    cursor = None
    try:
        # CONEXÃO DO BANCO DE DADOS
        conexao = conector.connect('agenda.db')
        cursor = conexao.cursor()
    
        try:
            # CRIA TABELA - KEY NOT NULL - "AUTO INCREMENTO"
            comando = '''CREATE TABLE IF NOT EXISTS agenda (
                        id INTEGER NOT NULL,
                        nome VARCHAR(32) NOT NULL,
                        telef VARCHAR(15) NOT NULL, 
                        PRIMARY KEY(id)
                        );
                    '''
    
            cursor.execute(comando) 
            comando = '''INSERT INTO agenda (id, nome, telef) 
                                VALUES (1, "CONTROLE", "99999-9999");
                            '''
            cursor.execute(comando)
        except:
            pass
    except conector.OperationalError as erro:
        print('Erro Operacional', erro)
    except conector.DatabaseError as erro:
        print('Erro de Banco de Dados', erro)

    finally:
        # Fechamento da Conexões e Cursores
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

# MENU DE OPÇÕES
def menu():
    limpa()
    linha()
    print('| AGENDA PRÁTICA |')
    linha()
    print('| [1] Inserir novo registro |')
    print('| [2] Apagar registro |')
    print('| [3] Atualizar registro |')
    print('| [4] Listar todas as tuplas |')
    print('| [5] Consultar pelo nome |')
    print('| [6] Sair |')
    linha()
