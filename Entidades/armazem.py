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
                ingredientes = ['calabresa', 'molho de tomate', 'queijo mussarela', 'cebola', 'azeitona']
            elif sabor.value == 'portuguesa':
                ingredientes = ['ovo', 'molho', 'queijo', 'presunto', 'cebola', 'azeitona']
            elif sabor.value == 'frango':
                ingredientes = ['frango', 'molho', 'queijo', 'catupiry', 'azeitona']

            if tamanho.value == 'broto':
                subtraendo = 2
            elif tamanho.value == 'media':
                subtraendo = 4
            elif tamanho.value == 'grande':
                subtraendo = 6 
            for i in ingredientes:
                for ingrediente in self.__estoque:
                    if ingrediente.nome_ingrediente == i:
                        ingrediente.quantidade -= subtraendo
                        break
                self.__saidas.append({i: subtraendo})
        return None

    # def saida_ingredientes(self, consumo):
    #     consumidos = []
    #     if 'calabresa' in consumo:
    #         calabresa = consumo['calabresa']
    #         consumidos.append(calabresa)

    #     if 'molho de tomate' in consumo:
    #         molho = consumo['molho de tomate']
    #         consumidos.append(calabresa)

    #     if 'queijo mussarela' in consumo:
    #         queijo = consumo['queijo mussarela']
    #         consumidos.append(calabresa)

    #     if 'tomate' in consumo:
    #         tomate = consumo['tomate']
    #         consumidos.append(calabresa)

    #     if 'cebola' in consumo:
    #         cebola = consumo['cebola']
    #         consumidos.append(calabresa)

    #     if 'azeitona' in consumo:
    #         azeitona = consumo['azeitona']
    #         consumidos.append(calabresa)

    #     if 'ovo cozido' in consumo:
    #         ovo = consumo['ovo cozido']
    #         consumidos.append(calabresa)

    #     if 'presunto' in consumo:
    #         presunto = consumo['presunto']
    #         consumidos.append(calabresa)

    #     if 'peito frango' in consumo:
    #         frango = consumo['peito frango']
    #         consumidos.append(calabresa)

    #     if 'catupiry' in consumo:
    #         catupiry = consumo['catupiry']
    #         consumidos.append(calabresa)

