from Entidades.armazem import Armazem
from Telas.tela_armazem import TelaArmazem

class ControladorArmazem():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__telaArmazem = TelaArmazem(self)
        self.__armazem = Armazem()

    @property
    def armazem(self):
        return self.__armazem

    def inclui_armazem(self):
        verificacao = self.__telaArmazem.set_armazem()
        if verificacao == 'S':
            self.__armazem = Armazem()

    def mostra_conteudo(self):
        self.__telaArmazem.mostra_ingredientes()

    def sai_ingredientes(self, sabor, tamanho):
        return self.__armazem.saida_ingrediente(sabor, tamanho)

    def retornar(self):
        self.__controlador_sistema.acessa_tela_sistema()

    def abre_tela_armazem(self):
        lista_opcoes = {1: self.inclui_armazem,
                        2: self.mostra_conteudo, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__telaArmazem.opcoes_armazem()]()
