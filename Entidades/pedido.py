from Entidades.cliente import Cliente
from Entidades.pizza import Pizza
from Entidades.Enum.sabor_pizza import SaborPizza
from Entidades.Enum.tamanho_pizza import TamanhoPizza

class Pedido():
    def __init__(self, cliente: Cliente, sabor: SaborPizza, tamanho: TamanhoPizza, data: str):
        self.__cliente = cliente
        self.__data = data
        self.__pizzas = []
        self.__valor = 0.00
        self.adiciona_pizza(sabor, tamanho)

    def cliente(self):
        return self.__cliente.nome

    @property
    def data(self):
        return self.__data
    
    @property
    def valor(self):
        return self.__valor
    
    @property
    def pizzas(self):
        return self.__pizzas

    @property
    def valor(self):
        return self.__valor

    def adiciona_pizza(self, sabor, tamanho):
        pizza = Pizza(sabor, tamanho)
        self.__pizzas.append(pizza)
        self.__valor += pizza.preco

