from decimal import *
from psycopg2.extensions import AsIs
from datetime import datetime
from config import config

class Pedido ():
#falta validar customerid e emmployeeid
	def __init__(self,orderid,customerid,employeeid,orderdate,requireddate,shippeddate,freight,shipname,shipaddress,shipcity,shipregion,shippostalcode,shipcountry,shipperid):
		self.orderid = orderid
		self.customerid = customerid
		self.employeeid = employeeid
		self.orderdate = orderdate
		self.requireddate = requireddate
		self.shippeddate = shippeddate
		self.freight = freight
		self.shipname = shipname
		self.shipaddress = shipaddress
		self.shipcity = shipcity
		self.shipregion = shipregion
		self.shippostalcode = shippostalcode
		self.shipcountry = shipcountry
		self.shipperid = shipperid
 
	def criaPedido (lista):
	#se tiver algum argumento nulo nao converter
		A=lista[0]
		B=lista[2]
		C=lista[6]
		D=lista[13]
		if(A!=None):
			A=int(A)
		if(B!=None):
			B=int(B)
		if(C!=None):
			C=Decimal(C)
		if(D!=None):
			D=int(D)
		pedido=Pedido (A, lista[1],B, lista[3], lista[4],lista[5], C, lista[7], lista[8], lista[9], lista[10],lista[11], lista[12],D)
		return pedido

	def inserePedido(pedido):

		string_sql='INSERT INTO northwind.orders (orderid, customerid, employeeid,orderdate, requireddate,shippeddate,freight,shipname,shipaddress,shipcity,shipregion,shippostalcode,shipcountry,shipperid)VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
		record_to_insert = (pedido.orderid, pedido.customerid,pedido.employeeid,pedido.orderdate,pedido.requireddate,pedido.shippeddate,pedido.freight,pedido.shipname,pedido.shipaddress,pedido.shipcity,pedido.shipregion,pedido.shippostalcode,pedido.shipcountry,pedido.shipperid)
		status=config.alteraBD(config,string_sql,record_to_insert)
		return status

	def deletaPedido(id):		
		string_sql ='DELETE FROM northwind.orders_details WHERE orderid = %s'
		config.alteraBD(config,string_sql,[id])
		string_sql = 'DELETE FROM northwind.orders WHERE orderid = %s'
		status=config.alteraBD(config,string_sql,[id])
		return status
		

	def consultaPedido(id):
		string_sql='SELECT * FROM northwind.orders WHERE orderid = %s'
		registros=config.consultaBD(config,string_sql,[id])
		if(len(registros[1])!=0):
			pedido=Pedido.criaPedido(registros[1][0])
			return pedido
		else:
			return None
		
	def atualizaPedido(lista):
		string_sql = """UPDATE northwind.orders SET %s = %s WHERE orderid = %s"""
		record_to_insert = ((AsIs(lista[1])), int(lista[2]), int(lista[0]))
		status=config.alteraBD(config,string_sql,record_to_insert)
		return status
	def validaAtributo(lista):
		string_sql='SELECT * FROM northwind.orders WHERE customerid= %s and employeeid= %s'
		record_to_insert=(lista[0],lista[1])
		registros=config.consultaBD(config,string_sql,record_to_insert)
		if(len(registros[1])!=0):
			return 'valido'
		else:
			return 'invalido'
	def validaIDPedido(lista):
		string_sql='SELECT * FROM northwind.orders WHERE orderid= %s'
		record_to_insert=(lista[0])
		registros=config.consultaBD(config,string_sql,record_to_insert)
		if(len(registros[1])!=0):
			return 'valido'
		else:
			return 'invalido'
		