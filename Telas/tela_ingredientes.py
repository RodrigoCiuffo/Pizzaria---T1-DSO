from Controladores.controlador_ingredientes import ControladorIngredientes

class TelaIngredientes():
    def __init__(self, controlador_armazem: ControladorIngredientes):
        self.__controlador_armazem = controlador_armazem