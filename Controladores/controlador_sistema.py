from Controladores.controlador_armazem import ControladorArmazem
from Controladores.controlador_fornecedor import ControladorFornecedor
from Controladores.controlador_cliente import ControladorCliente
from Controladores.controlador_gerente import ControladorGerente
from Controladores.controlador_ingredientes import ControladorIngredientes
from Telas.tela_sistema import TelaSistema


class ControladorSistema():
    def __init__(self):
        self.__controlador_fornecedor = ControladorFornecedor(self)
        self.__controlador_armazem = ControladorArmazem(self)
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_gerente = ControladorGerente(self)
        self.__controlador_ingredientes = ControladorIngredientes(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_armazem(self):
        return self.__controlador_armazem

    @property
    def controlador_fornecedor(self):
        return self.__controlador_fornecedor

    @property
    def controlador_cliente(self):
        return self.__controlador_cliente

    @property
    def controlador_gerente(self):
        return self.__controlador_cliente

    @property
    def controlador_ingredientes(self):
        return self.__controlador_ingredientes

    def acessa_tela_sistema(self):
        self.abre_tela()

    def acessa_tela_fornecedor(self):
        self.__controlador_fornecedor.abre_tela_fornecedor()

    def acessa_tela_cliente(self):
        self.__controlador_cliente.abre_tela_cliente()

    def acessa_tela_gerente(self):
        self.__controlador_gerente.abre_tela_gerente()

    def acessa_tela_armazem(self):
        self.__controlador_armazem.abre_tela_armazem()

    def acessa_tela_ingrediente(self):
        self.__controlador_ingredientes.abre_tela_ingredientes()

    def encerra_sessao(self):
        raise SystemExit(1)

    def abre_tela(self):
        lista_opcoes = {1: self.acessa_tela_fornecedor, 2: self.acessa_tela_cliente, 3: self.acessa_tela_gerente,
                        4: self.acessa_tela_armazem, 5: self.acessa_tela_ingrediente, 0: self.encerra_sessao}

        while True:
            opcao_escolhida = self.__tela_sistema.opcoes_sistema()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
