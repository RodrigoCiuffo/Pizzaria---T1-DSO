# from Controladores.controlador_ingredientes import ControladorIngredientes
from Entidades.Enum.nome_ingrediente import NomeIngrediente

class TelaIngredientes():
    def __init__(self, controlador_ingredientes):
        self.__controlador_ingredientes = controlador_ingredientes

    def opcoes_ingredientes(self):
        print("-------- INGREDIENTES ----------")
        print("Escolha a opcao:")
        print("1 - Incluir Ingrediente")
        print("2 - Buscar Ingrediente")
        print("0 - Retornar")

        while True:
            try:
                escolha = int(input('Digite uma das opções listadas: '))
                if escolha >= 0 and escolha <= 2:
                    break
                else:
                    print('Entrada inválida! O número informado não está entre as opções.')
            except ValueError:
                print('Entrada inválida! O número informado não é um inteiro.')
        return escolha

    def busca_ingrediente(self):
        data = input('Digite a data de chegada do ingrediente')
        while True:
            try:
                cnpj = int(input('Digite o CNPJ do fornecedor responsável pelo envio'))
                break 
            except ValueError:
                print('Entrada inválida! O número informado não é um inteiro.')
        return {"Data": data,"CNPJ": cnpj}

    def printa_tela(self, arg):
        print(arg)
