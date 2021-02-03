import psycopg2
con = None
def startConnection(value,senha):
    #Conectar no database
    global con
    usuario=value
    try:
        con = psycopg2.connect(
            host = "localhost",
            database = "Projeto_BD",
            user = usuario,
            password = senha,
            port = "5432"
        )
        con.autocommit = True
    except:
        print("Erro ao Efetuar Conexao")

def QueryTol(comando):
    print(comando)
    cmd = con.cursor()
    cmd.execute(comando)
    options=list(cmd.fetchall())
    return options

def ClosedConnection():
    con.close()