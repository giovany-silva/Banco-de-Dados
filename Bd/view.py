from decimal import *
from datetime import datetime
from Modelo import Pedido

class View():
	def inicio(self):
		return self.menu()

	def menu(self):
		print("MENU")
		print("1. Cadastrar um produto")
		print("2. Deletar um produto")
		print("3. Cosultar um produto")
		print("4. Alterar dados de um produto")
		print("0. Sair")
		opcao=int(input("Digite a opcao desejada :"))
		return opcao

	def coletadadosPedido(self):
		self.orderid = input('Digite o id do pedido: ')
		self.customerid = input('Digite o id consumidor: ')
		self.employeeid = input('Digite o id do empregado: ')
		validade=Pedido.validaAtributo([self.customerid,self.employeeid])
		if(validade=='invalido'):
			print('ID do consumidor e/ou ID do pedido invalidos ')
			self.menu()
		self.orderdate = input('Digite a data do pedido (AAAA-MM-DD): ')
		self.requireddate = input('Digite a data de requerimento do pedido (AAAA-MM-DD): ')
		self.shippeddate = input('Digite a data de envio do pedido (AAAA-MM-DD): ')
		self.freight = input('Digite o  valor do frete')
		self.shipname = input('Digite o nome de envio: ')
		self.shipaddress = input('Digite o endereco do envio: ')
		self.shipcity = input('Digite a cidade do envio: ')
		self.shipregion = input('Digite a regiao do envio: ')
		self.shippostalcode = input('Digite o CEP do envio ')
		self.shipcountry = input('Digite o pais')
		self.shipperid = input('Digite o id de envio')
		year,month,day=map(int,self.orderdate.split('-'))
		orderdate=datetime(year,month,day)
		year,month,day=map(int,self.requireddate.split('-'))
		requireddate=datetime(year,month,day)
		year,month,day=map(int,self.shippeddate.split('-'))
		shippeddate=datetime(year,month,day)
		valores=[self.orderid,self.customerid,self.employeeid,self.orderdate,self.requireddate,self.shippeddate,self.freight,self.shipname,self.shipaddress,self.shipcity,self.shipregion,self.shippostalcode,self.shipcountry,self.shipperid]
		return valores
	def idPedido(self):
		self.orderid=input('Digite o id do pedido: ')
		return self.orderid 
	def imprimeStatus(self,status):
		if(status=='sucesso'):
			print("Comando executado no banco de dados com sucesso")
		else:
			print(status)
	def imprimePedido(self,pedido):
		if(pedido is not None):
			print("ID do pedido: ",pedido.orderid)
			print("ID do consumidor: ",pedido.customerid)
			print("ID do empregado: ",pedido.employeeid)
			print("Data do pedido: ",pedido.orderdate)
			print("Data de requerimento do pedido: ",pedido.requireddate)
			print("Data de envio do pedido: ",pedido.shippeddate)
			print("Valor do frete: ",pedido.freight)
			print("Nome de envio do pedido: ",pedido.shipname)
			print("Endereco de envio: ",pedido.shipaddress)
			print("Cidade de envio: ",pedido.shipcity)
			print("Regiao de envio: ",pedido.shipregion)
			print("CEP de envio: ",pedido.shippostalcode)
			print("Pais de envio: ",pedido.shipcountry)
			print("ID de envio: ",pedido.shipperid)
	def dadosAtualiza(self):
		self.orderid=input('Digite o id do pedido: ')
		validade=Pedido.validaIDPedido([self.orderid])
		if(validade=='invalido'):
			print('ID do pedido invalido ')
			self.menu()
		self.attribute=input('Digite o atributo a ser atualizado: ')
		self.new_value=input('Digite o novo valor do atributo: ')
		return [self.orderid,self.attribute,self.new_value]