from Controladores.controlador_sistema import ControladorSistema
from Entidades.ingrediente import Ingrediente

class ControladorIngredientes():
    def __init__(self, controlador_sistema: ControladorSistema):
        imports = self.gerencia_imports()
        self.__controlador_sistema = controlador_sistema
        self.__telaIngredientes = imports(self)

    def gerencia_imports(self):
        from Telas.tela_ingredientes import TelaIngredientes
        return TelaIngredientes

    def inclui_ingrediente(self):
        dados_ingrediente = self.__telaIngredientes.cria_ingrediente()
        if dados_ingrediente is None:
            return None
        else:
            novo_ingrediente = Ingrediente(dados_ingrediente["Data"], dados_ingrediente["Nome"], dados_ingrediente["Quantidade"], dados_ingrediente["Fornecedor"])
            self.__controlador_sistema.controlador_armazem.estoque.append(novo_ingrediente)