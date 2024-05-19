from Controladores.controlador_armazem import ControladorArmazem

class TelaArmazem():
    def __init__(self, controlador_armazem: ControladorArmazem):
        self.__controlador_armazem = controlador_armazem