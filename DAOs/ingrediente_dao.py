import pickle
from DAOs.dao import DAO
from Entidades.ingrediente import Ingrediente

class IngredienteDAO(DAO):
    def __init__(self):
        super().__init__('ingredientes.pkl')
        self.__load()

    def __dump(self):
        pickle.dump(self._DAO__cache, open(self._DAO__datasource, 'wb'))

    def __load(self):
        try:
            self._DAO__cache = pickle.load(open(self._DAO__datasource, 'rb'))
        except FileNotFoundError:
            self.__dump()

    def add(self, ingrediente: Ingrediente):
        if ingrediente is not None and isinstance(ingrediente, Ingrediente):
            key = ingrediente.nome_ingrediente
            super().add(key, ingrediente)

    def update(self, ingrediente: Ingrediente):
        if ingrediente is not None and isinstance(ingrediente, Ingrediente):
            key = ingrediente.nome_ingrediente
            super().update(key, ingrediente)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            super().remove(key)

    def get_all(self):
        return super().get_all()