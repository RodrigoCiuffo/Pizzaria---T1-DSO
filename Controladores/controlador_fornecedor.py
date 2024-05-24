from Entidades.fornecedor import Fornecedor
# from Controladores.controlador_sistema import ControladorSistema


class ControladorFornecedor():
    def __init__(self, controlador_sistema):
        from Telas.tela_fornecedor import TelaFornecedor
        self.__fornecedores = []
        self.__telaFornecedor = TelaFornecedor(self)
        self.__controlador_sistema = controlador_sistema

    def inclui_fornecedor(self):
        dados_fornecedor = self.__telaFornecedor.cadastro_fornecedor()
        fornecedor = Fornecedor(dados_fornecedor["Razao Social"], dados_fornecedor["CNPJ"],
                                dados_fornecedor["Email"], dados_fornecedor["Telefone"])
        self.__fornecedores.append(fornecedor)

    @property
    def controlador_sistema(self):
        return self.__fornecedores

    @property
    def fornecedores(self):
        return self.__fornecedores

    def exclui_fornecedor(self):
        cnpj_excluido = self.__telaFornecedor.exclusao_fornecedor()
        for fornecedor in self.__fornecedores:
            if fornecedor.cnpj == cnpj_excluido:
                self.__fornecedores.remove(fornecedor)
                print('Fornecedor excluido com sucesso!')
                return None
        print('Fornecedor nao encontrado.')
        return None

    def altera_fornecedor(self):
        alteracoes = self.__telaFornecedor.altera_dados_fornecedor()
        cnpj = alteracoes["CNPJ Atual"]
        for fornecedor in self.__fornecedores:
            if fornecedor.cnpj == cnpj:
                if "Nova Razao" in alteracoes:
                    fornecedor.razao_social = alteracoes["Nova Razao"]
                if "Novo CNPJ" in alteracoes:
                    fornecedor.cnpj = alteracoes["Novo CNPJ"]
                if "Novo Email" in alteracoes:
                    fornecedor.email = alteracoes["Novo Email"]
                if "Novo Telefone" in alteracoes:
                    fornecedor.telefone = alteracoes["Novo Telefone"]
                break

    def mostra_fornecedores(self):
        self.__telaFornecedor.mostra_fornecedores()

    def retornar(self):
        self.__controlador_sistema.acessa_tela_sistema()

    def abre_tela_fornecedor(self):
        lista_opcoes = {1: self.inclui_fornecedor, 2: self.exclui_fornecedor,
                        3: self.altera_fornecedor, 4: self.mostra_fornecedores, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__telaFornecedor.opcoes_fornecedor()]()
