class Pizza():
    def __init__(self, sabor, tamanho):
        self.__sabor = sabor
        self.__tamanho = tamanho
        self.__preco = 0.00

    @property
    def sabor(self):
        return self.__sabor

    @property
    def tamanho(self):
        return self.__tamanho

    @property
    def preco(self):
        return self.__preco

    @sabor.setter
    def sabor(self, sabor):
        self.__sabor = sabor

    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    def calcula_preco(self):
        # sabor x tamanho
        if self.__sabor == 'calabrsa':
            self.__preco += 15 * self.__tamanho
        elif self.__sabor == 'portuguesa':
            self.__preco += 18 * self.__tamanho
        elif self.__sabor == 'frango':
            self.__preco += 20 * self.__tamanho
        return self.__preco
