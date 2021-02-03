from decimal import *
from modelo import OderDetails
from datetime import datetime

class View():
	def inicio(self):
		return self.menu()

	def menu(self):
		print("MENU")
		print("1. Cadastrar um produto")
		print("2. Deletar um produto")
		print("3. Cosultar um produto")
		print("4. Alterar dados de um produto")
		print("5. Consultar o relatorio de Pedidos")
		print("6. Cadastrar uma venda")
		print("7. Alterar a quantidade de produto vendido")
		print("0. Sair")
		opcao=int(input("Digite a opcao desejada :"))
		return opcao

	def coletadadosproduto(self):
		productid=input('Digite o identificador do produto: ')
		productname=input('Digite o nome do produto: ')
		supplierid=input('Digite o identificador do fornecedor: ')
		categoryid=input('Digite o identificador da categoria: ')
		quantityperunit=input('Digite a quantidade de produto por embalagem: ')
		unitprice=input('Digite o preço do produto: ')
		unitsinstock=input('Digite a quantidade de unidades no estoque: ')
		unitsonorder=input('Digite a quantidade de unidades disponiveis para venda')
		reorderlevel=input('Digite o nivel do produto: ')
		discontinued=input('O produto esta descontinuado? ')
		valores=[productid,productname,supplierid,categoryid,quantityperunit,unitprice,unitsinstock,unitsorder,reorderlevel,discontinued]
		return valores

	def coletadadosprodutosupdate(self,id):
		atributos={1: 'productname',2:'supplierid',3:'categoryid',4:'quantityperunit',5:'unitprice',6:'unitsinstock',7:'unitsonorder',8:'reorderlevel',9:'discontinued'}
		printf("Digite: ")
		print("1 para o nome do produto")
		print("2 para o identificador do fornecedor")
		print("3 para o identificador da categoria")
		print("4 para a quantidade de produto por embalagem")
		print("5 para o preço unitário")
		print("6 para a quantidade de produtos no estoque")
		print("7 para a quantidade de produtos disponivel para venda")
		print("8 para o nivel do produto")
		print("para descontinuado")
		campo=int(input())
			
		valor=input('Digite o novo valor para o atributo: ')
		if((campo==2) or (campo==3) or (campo==6) or (campo==7) or (campo==8)):
			valor=int(valor)
		elif(campo==6):
			valor=Decimal(valor)
		return (id,atributos[campo],valor)

	def recebecodproduto(self):
		producid=int(input("Digite o identificador do produto: "))
		return productid

	def recebecodpedido(self):
		pedidoid=int(input("Digite o identificador do pedido: "))
		return pedidoid

	def imprimeproduto(self,prod):
		if(prod is not None):
			print("ID :",prod.id)
			print("None :",prod.none)
			print("Fornecedor",prod.fornecedor)
			print("Categoria :",prod.categoria)
			print("Quantidade por embalagem :",prod.quantidade(embalagem))
			print("Preco Unitario :",prod.precounitario)
			print("Estoque :",prod.estoque)
			print("Disponiveis para venda :",prod.venda)
			print("Nivel :",prod.nivel)
			print("Descontinuado :",prod.descontinuado)
		else:
			printf('Consulta vazia')

	def imprimeRelatorio(self,registros):
		if(registros is not None):
			colunas=registros[0]
			dados=registros[1]
			print("A consulta retornou ",len(dados)," registros")
			for i in dados:
				print(colunas[0]," : ",i[0])
				print(colunas[1]," : ",i[1])
				print(colunas[2]," : ",i[2])
				print(colunas[3]," : ",i[3])
				print(colunas[4]," : ",i[4])
		else:
			print("A consulta nao retornou dados")
	def coletadadospedido(self):
		orderid=input('Digite o identificador do pedido: ')
		customerid=input('Digite o identificador do cliente: ')
		employeeid=input('Digite o identificador do funcionario: ')
		orderdate=input('Digite a data do pedido (AAAA-MM-DD): ')
		requiredate=input('Digite a data do fechamento do pedido (AAAA-MM-DD): ')
		shippeddate=input('Digite a data do envio do pedido (AAAA-MM-DD): ')
		freight=input('Digite o valor do frete: ')
		shipname=input('Digite o local do envio')
		shipaddress=input('Digite o enderedo: ')
		shipcity=input('Digite a cidade do envio: ')
		shipregion=input('Digite a regiao do envio: ')
		shippostalcode=input('Digite o CEP:')
		shipcountry=input('Digite  o pais: ')
		shipperid=input('Digite o id do endereco de envio')
		year,month,day=map(int,orderdate.split('-'))
		orderdate=datetime(year,month,day)
		year,month,day=map(int,requireddate.split('-'))
		requireddate=datetime(year,month,day)
		year,month,day=map(int,shippeddate.split('-'))
		shippeddate=datetime(year,month,day)
		pedido=[int(orderid),int(customerid),int(employeeid),orderdate,requiredate,shippeddate,Decimal(freight),shipname,shipaddress,shipcity,shipregion,shippostalcode]
		return pedido;
	def coletaprodutospedido(self,orderid):
		i=1;
		listaProdutos=[]
		while i!=-1:
			print("Informe os produtos para o pedido ",orderid," : ")
			productid=input('Digite o identificador do produto: ')
			unitprice=input('Digite o valor do produto: ')
			quantity=input('Digite a quantidade comprada: ')
			discount=input('Digite o valor de desconto: ')
			produtoPedido=OrderDetails(int(orderid),int(productid),Decimal(unitprice),int(quantity),Decimal(discount))
			listaProdutos.append(produtoPedido)
			i=int(input("Deseja continuar a cadastrar produtos para esse pedido? (-1 para sasir: 1 para continuar)"))
		
		
		return listaProdutos
	def coletadadospedidosupdate(self):
		pedidoid=int(input('Digite o codgo do pedido: '))
		productid=int(input('Digite o identificador do produto: '))
		quantidade=int(input('Digite a quantidade vendida: '))
		return [pedidoid,productid,quantidade]
	def imprimeStatus(self,status):
		if(status=='sucesso'):
			print("Comando executado no banco de dados com sucesso")
		else:
			print(status)

		

				