import psycopg2

class config: 
	def setParametros(self):
		
		return self

	def alteraBD(self,stringSQL,valores):
		conn=None

		try:
			conexao=psycopg2.connect(host='localhost',port='5432',dbname='Northwind',user='postgres',password='melise123')
			sessao=conexao.cursor()
			sessao.execute(stringSQL,valores)
			conexao.commit()
			sessao.close()

		except psycopg2.Error:
			return psycopg2.Error
		finally:
			if conn is not None:
				conn.close()
			return 'sucesso'
	def consultaBD(self,stringSQL,id):
		conn=None
		try:
			conexao=psycopg2.connect(host='localhost',port='5432',dbname='Northwind',user='postgres',password='melise123')
			sessao=conexao.cursor()
			sessao.execute(stringSQL,id)
			registros=sessao.fetchall()
			colnames=[desc[0] for desc in sessao.description]
			conexao.commit()
			sessao.close()

		except psycopg2.Error:
			return psycopg2.Error
		finally:
			if conn is not None:
				conn.close()
		return (colnames,registros)
