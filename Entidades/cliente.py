from Entidades.abstractpessoa import Pessoa
# from Entidades.pedido import Pedido


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, cpf: int, endereco: str, telefone: int):
        super().__init__(nome, idade, cpf, endereco, telefone)
        self.__pedidos = []


# def pedido_atual(self):
#     return 

@property
def pedidos(self):
    return self.__pedidos

# def realiza_pedido(self, cliente: Cliente, data: str):
#     if isinstance(cliente, Cliente) and type(data) == str:
#         pedido = Pedido(cliente, data)

