import pickle
from DAOs.dao import DAO
from Entidades.pedido import Pedido
from Entidades.cliente import Cliente

class PedidoDAO(DAO):
    def __init__(self):
        super().__init__('pedidos.pkl')
        self.__load()

    def __dump(self):
        pickle.dump(self._DAO__cache, open(self._DAO__datasource, 'wb'))

    def __load(self):
        try:
            self._DAO__cache = pickle.load(open(self._DAO__datasource, 'rb'))
        except FileNotFoundError:
            self.__dump()

    def add(self, pedido: Pedido):
        if pedido is not None and isinstance(pedido, Pedido):
            key = f"{pedido.cliente}_{pedido.data}"
            super().add(key, pedido)

    def update(self, pedido: Pedido):
        if pedido is not None and isinstance(pedido, Pedido):
            key = f"{pedido.cliente}_{pedido.data}"
            super().update(key, pedido)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            super().remove(key)

    def get_all(self):
        return super().get_all()