from Entidades.ingrediente import Ingrediente

class Armazem():
    def __init__(self):
        self.__estoque = []
        self.__saidas = []

    @property
    def estoque(self):
        return self.__estoque

    @property
    def saidas(self):
        return self.__saidas

    def add_ingrediente(self, ingrediente: Ingrediente):
        self.__estoque.append(ingrediente)

    def saida_ingredientes(self, consumo):
        consumidos = []
        if 'calabresa' in consumo:
            calabresa = consumo['calabresa']
            consumidos.append(calabresa)

        if 'molho de tomate' in consumo:
            molho = consumo['molho de tomate']
            consumidos.append(calabresa)

        if 'queijo mussarela' in consumo:
            queijo = consumo['queijo mussarela']
            consumidos.append(calabresa)

        if 'tomate' in consumo:
            tomate = consumo['tomate']
            consumidos.append(calabresa)

        if 'cebola' in consumo:
            cebola = consumo['cebola']
            consumidos.append(calabresa)

        if 'azeitona' in consumo:
            azeitona = consumo['azeitona']
            consumidos.append(calabresa)

        if 'ovo cozido' in consumo:
            ovo = consumo['ovo cozido']
            consumidos.append(calabresa)

        if 'presunto' in consumo:
            presunto = consumo['presunto']
            consumidos.append(calabresa)

        if 'peito frango' in consumo:
            frango = consumo['peito frango']
            consumidos.append(calabresa)

        if 'catupiry' in consumo:
            catupiry = consumo['catupiry']
            consumidos.append(calabresa)

