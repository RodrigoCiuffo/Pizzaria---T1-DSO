from Controladores.controlador_sistema import ControladorSistema

class ControladorIngredientes():
    def __init__(self, controlador_sistema: ControladorSistema):
        imports = self.gerencia_imports()
        self.__controlador_sistema = controlador_sistema
        self.__telaIngredientes = imports(self)
        
    def gerencia_imports(self):
        from Telas.tela_ingredientes import TelaIngredientes
        return TelaIngredientes


    # def inclui_ingrediente(self):
    #     dados_ingrediente = self.__telaIngredientes.cria_ingrediente()
    #     novo_ingrediente = 
