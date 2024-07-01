from DAOs.dao import DAO
from Entidades.cliente import Cliente

class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('clientes.pkl')

    def add(self, cliente: Cliente):
        if cliente is not None and isinstance(cliente, Cliente) and isinstance(cliente.cpf, int):
            super().add(cliente.cpf, cliente)

    def update(self, cliente: Cliente):
        if cliente is not None and isinstance(cliente, Cliente) and isinstance(cliente.cpf, int):
            super().update(cliente.cpf, cliente)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            super().remove(key)