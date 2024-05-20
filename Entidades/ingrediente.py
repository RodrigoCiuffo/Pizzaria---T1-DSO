from Controladores.controlador_fornecedor import Fornecedor
from Entidades.Enum.nome_ingrediente import NomeIngrediente

class Ingrediente():
    def __init__(self, data: str, nome_ingrediente: NomeIngrediente, quantidade: int, fornecedor: Fornecedor):
        self.__data = data
        self.__nome_ingrediente = nome_ingrediente
        self.__quantidade = quantidade
        self.__fornecedor = fornecedor
