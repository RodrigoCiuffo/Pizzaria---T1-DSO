from DAOs.dao import DAO
from Entidades.gerente import Gerente

class GerenteDAO(DAO):
    def __init__(self):
        super().__init__('gerentes.pkl')

    def add(self, gerente: Gerente):
        if gerente is not None and isinstance(gerente, Gerente) and isinstance(gerente.cpf, str):
            super().add(gerente.cpf, gerente)

    def update(self, gerente: Gerente):
        if gerente is not None and isinstance(gerente, Gerente) and isinstance(gerente.cpf, str):
            super().update(gerente.cpf, gerente)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            super().remove(key)