from Entidades.abstractpessoa import Pessoa


class Gerente(Pessoa):
    def __init__(self, nome: str, idade: int, cpf: str, endereco: str, telefone: str):
        super().__init__(nome, idade, cpf, endereco, telefone)
        self.__relatorio_pedidos = []
        self.__relatorio_ingredientes = {}

    def acesso_administrativo(self, cpf: str):
        liberacao = False
        if cpf == self.cpf:
            liberacao = True
            return liberacao
        return liberacao

    @property
    def relatorio_pedidos(self):
        return self.__relatorio_pedidos

    @property
    def relatorio_ingredientes(self):
        return self.__relatorio_ingredientes
