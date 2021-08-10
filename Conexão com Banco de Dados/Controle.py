from view import View
from Modelo import Pedido
class Controle:
	def inicio(self):
		opcao=self.view.inicio()
		while opcao!=0:
			if opcao==1:
				p = self.view.coletadadosPedido()
				pedido=Pedido.criaPedido(p)
				status=Pedido.inserePedido(pedido)
				self.view.imprimeStatus(status)
			if opcao==2:
				p = self.view.idPedido()
				status=Pedido.deletaPedido(p)
				self.view.imprimeStatus(status)
			if opcao==3:
				id=self.view.idPedido()
				pedido=Pedido.consultaPedido(id)
				self.view.imprimePedido(pedido)
			if opcao==4:
				lista=self.view.dadosAtualiza()
				status=Pedido.atualizaPedido(lista)
				self.view.imprimeStatus(status)
	def __init__(self):
		self.view= View()
if __name__=="__main__":
	main=Controle()
	main.inicio()		