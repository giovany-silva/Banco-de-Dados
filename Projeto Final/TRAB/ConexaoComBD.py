import psycopg2
con = None
def startConnection():
    #Conectar no database
    global con
    try:
        con = psycopg2.connect(
            host = "localhost",
            database = "PBD",
            user = "postgres",
            password = "root",
            port = "5432"
        )
        con.autocommit = True
    except:
        print("Erro ao Efetuar Conexao")

def QueryTol(comando):
    print(comando)
    cmd = con.cursor()
    cmd.execute(comando)

def ClosedConnection():
    con.close()
