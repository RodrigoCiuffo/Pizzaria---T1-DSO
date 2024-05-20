from Controladores.controlador_sistema import ControladorSistema
from Entidades.ingrediente import Ingrediente
from Entidades.Enum.nome_ingrediente import NomeIngrediente
from Controladores.controlador_fornecedor import ControladorFornecedor

class ControladorIngredientes():
    def __init__(self, controlador_sistema: ControladorSistema, controlador_fornecedor: ControladorFornecedor):
        self.__controlador_sistema = controlador_sistema
        self.__telaIngredientes = None
        self.__controlador_fornecedor = controlador_fornecedor
        self.gerencia_imports()

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    def gerencia_imports(self):
        from Telas.tela_ingredientes import TelaIngredientes
        self.__telaIngredientes = TelaIngredientes(self)

    def inclui_ingrediente(self):
        data = input('Digite a data de chegada do ingrediente')
        loop = True
        while loop:
            nome_escolhido = input('Digite o nome do ingrediente')
            for nome_ingrediente in NomeIngrediente:
                if nome_ingrediente.value == nome_escolhido:
                    nome = nome_ingrediente
                    loop = False
                    break
            if loop is True:
                print('Informe uma opcao válida!')
        while True:
            try:
                qtde = int(input('Digite a quantidade, em unidades, do ingrediente: '))
                cnpj_fornecedor = int(input('Informe o CNPJ do fornecedor que fez o envio: '))
                break
            except ValueError:
                print("Valor inválido! Por favor, digite números inteiros válidos para a quantidade e o CNPJ.")
        ref_fornecedor = None
        for fornecedor in self.__controlador_fornecedor.fornecedores:
            if fornecedor.cnpj == cnpj_fornecedor:
                ref_fornecedor = fornecedor
        if ref_fornecedor is None: 
            print('Nenhum fornecedor com o CNPJ informado.')
            return None
        else:
            dados_ingrediente = {"Data": data, "Nome": nome, "Quantidade": qtde, "Fornecedor": ref_fornecedor}
            novo_ingrediente = Ingrediente(dados_ingrediente["Data"], dados_ingrediente["Nome"], dados_ingrediente["Quantidade"], dados_ingrediente["Fornecedor"])
            self.__controlador_sistema.controlador_armazem.armazem.estoque.append(novo_ingrediente)

    def retornar(self):
        self.__controlador_sistema.acessa_tela_sistema()

    def abre_tela_ingredientes(self):
        lista_opcoes = {1: self.inclui_ingrediente, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__telaIngredientes.opcoes_ingredientes()]()