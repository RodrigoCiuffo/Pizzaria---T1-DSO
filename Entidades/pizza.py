class Pizza():
    def __init__(self, sabor, tamanho):
        self.__sabor = sabor
        self.__tamanho = tamanho
        self.__preco = 0.00

    @property
    def preco(self):
        return self.__preco