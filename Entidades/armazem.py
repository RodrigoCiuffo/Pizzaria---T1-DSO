from Entidades.ingrediente import Ingrediente
from Entidades.Enum.nome_ingrediente import NomeIngrediente
from Entidades.Enum.tamanho_pizza import TamanhoPizza
from Entidades.Enum.sabor_pizza import SaborPizza


class Armazem():
    def __init__(self):
        self.__estoque = []
        self.__saidas = []

    @property
    def estoque(self):
        return self.__estoque

    @property
    def saidas(self):
        return self.__saidas

    def add_ingrediente(self, ingrediente: Ingrediente):
        self.__estoque.append(ingrediente)

    def saida_ingrediente(self, sabor: NomeIngrediente, tamanho: TamanhoPizza):
        if isinstance(sabor, SaborPizza) and isinstance(tamanho, TamanhoPizza):
            if sabor.value == 'calabresa':
                ingredientes = ['calabresa', 'molho de tomate',
                                'queijo mussarela', 'cebola', 'azeitona']
            elif sabor.value == 'portuguesa':
                ingredientes = ['ovo cozido', 'molho de tomate',
                                'queijo mussarela', 'presunto', 'cebola', 'azeitona']
            elif sabor.value == 'peito de frango':
                ingredientes = ['peito de frango', 'molho de tomate',
                                'queijo mussarela', 'catupiry', 'azeitona']

            if tamanho.value == 'broto':
                subtraendo = 2
            elif tamanho.value == 'media':
                subtraendo = 4
            elif tamanho.value == 'grande':
                subtraendo = 6
            isOk = True
            for i in ingredientes:
                check = 0
                for ingrediente in self.__estoque:
                    if ingrediente.nome_ingrediente == i:
                        if ingrediente.quantidade >= subtraendo and check == 0:
                            ingrediente.quantidade -= subtraendo
                            check += 1
                if check == 0:
                    isOk = False
                    return isOk
                self.__saidas.append({i: subtraendo})
        return isOk
