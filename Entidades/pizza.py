from Entidades.Enum.sabor_pizza import SaborPizza
from Entidades.Enum.tamanho_pizza import TamanhoPizza


class Pizza():
    def __init__(self, sabor: SaborPizza, tamanho: TamanhoPizza):
        self.__sabor = sabor
        self.__tamanho = tamanho
        if sabor.value == 'calabresa':
            custo = 15.00
        elif sabor.value == 'portuguesa':
            custo = 18.00
        elif sabor.value == 'frango':
            custo = 20.00
        if tamanho.value == 'broto':
            consumo = 2
        elif tamanho.value == 'media':
            consumo = 4
        elif tamanho.value == 'grande':
            consumo = 6
        self.__preco = custo * consumo

    @property
    def sabor(self):
        return self.__sabor

    @property
    def tamanho(self):
        return self.__tamanho

    @property
    def preco(self):
        return self.__preco

    @sabor.setter
    def sabor(self, sabor):
        self.__sabor = sabor

    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    # def calcula_preco(self):
    #     # sabor x tamanho
    #     if self.__sabor == 'calabresa' and self.__tamanho == 'broto':
    #         self.__preco += 15 * 2
    #     elif self.__sabor == 'portuguesa':
    #         self.__preco += 18 * self.__tamanho
    #     elif self.__sabor == 'frango':
    #         self.__preco += 20 * self.__tamanho
    #     return self.__preco
