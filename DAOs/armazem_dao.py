import pickle
from Entidades.armazem import Armazem
from DAOs.dao import DAO

class ArmazemDAO(DAO):
    def __init__(self):
        super().__init__('armazem.pkl')
        self.__armazem = Armazem()
        self.__load()

    def __dump(self):
        with open(self._DAO__datasource, 'wb') as file:
            pickle.dump((self.__armazem, []), file)

    def __load(self):
        try:
            with open(self._DAO__datasource, 'rb') as file:
                self.__armazem, _ = pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, ValueError):
            print(f"Erro ao carregar dados de {self._DAO__datasource}. Inicializando com valores padrão.")
            self.__armazem = Armazem()

    def save_armazem(self):
        with open(self._DAO__datasource, 'wb') as file:
            pickle.dump((self.__armazem, []), file)

    @property
    def armazem(self):
        return self.__armazem