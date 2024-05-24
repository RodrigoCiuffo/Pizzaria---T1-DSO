from Controladores.controlador_fornecedor import Fornecedor
from Entidades.Enum.nome_ingrediente import NomeIngrediente

class Ingrediente():
    def __init__(self, data: str, nome_ingrediente: NomeIngrediente, quantidade: int, fornecedor: Fornecedor):
        self.__data = data
        self.__nome_ingrediente = nome_ingrediente
        self.__quantidade = quantidade
        self.__fornecedor = fornecedor

    @property
    def data(self):
        return self.__data

    @property
    def nome_ingrediente(self):
        return self.__nome_ingrediente.value

    @property
    def quantidade(self):
        return self.__quantidade

    @property
    def fornecedor(self):
        return self.__fornecedor

    @data.setter
    def data(self, nova_data: str):
        self.__data = nova_data

    @nome_ingrediente.setter
    def nome_ingrediente(self, novo_nome: NomeIngrediente):
        self.__nome_ingrediente = novo_nome

    @quantidade.setter
    def quantidade(self, nova_quantidade: int):
        self.__quantidade = nova_quantidade

    @fornecedor.setter
    def fornecedor(self, novo_fornecedor: Fornecedor):
        self.__fornecedor = novo_fornecedor

    def __repr__(self):
        return "Ingrediente"
