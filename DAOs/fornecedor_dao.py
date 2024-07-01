import pickle
from DAOs.dao import DAO
from Entidades.fornecedor import Fornecedor

class FornecedorDAO(DAO):
    def __init__(self):
        super().__init__('fornecedores.pkl')

    def carregar_fornecedores(self):
        try:
            with open(self.datasource, 'rb') as file:
                fornecedores = pickle.load(file)
                return fornecedores
        except FileNotFoundError:
            return []

    def add(self, fornecedor: Fornecedor):
        if fornecedor is not None and isinstance(fornecedor, Fornecedor) and isinstance(fornecedor.cnpj, int):
            super().add(fornecedor.cnpj, fornecedor)

    def update(self, fornecedor: Fornecedor):
        if fornecedor is not None and isinstance(fornecedor, Fornecedor) and isinstance(fornecedor.cnpj, int):
            super().update(fornecedor.cnpj, fornecedor)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            super().remove(key)