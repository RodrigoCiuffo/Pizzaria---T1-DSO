from Controladores.controlador_ingredientes import ControladorIngredientes
from Entidades.Enum.nome_ingrediente import NomeIngrediente

class TelaIngredientes():
    def __init__(self, controlador_ingredientes: ControladorIngredientes):
        self.__controlador_ingredientes = controlador_ingredientes

    def opcoes_ingredientes(self):
        print("-------- INGREDIENTES ----------")
        print("Escolha a opcao:")
        print("1 - Incluir Ingrediente")
        print("2 - Mostrar Conteúdo")
        print("0 - Retornar")

        while True:
            try:
                escolha = int(input('Digite uma das opções listadas: '))
                if escolha >= 0 and escolha <= 5:
                    break
                else:
                    print('Entrada inválida! O número informado não está entre as opções.')
            except ValueError:
                print('Entrada inválida! O número informado não é um inteiro.')
        return escolha

    def cria_ingrediente(self):
        data = input('Digite a data de chegada do ingrediente')
        nome = int(input('Digite o nome do ingrediente'))
        qtde = input('Digite a quantidade, em unidades, do ingrediente')
        cnpj_fornecedor = int(input('Informe o CNPJ do fornecedor que fez o envio'))
        ref_fornecedor = None
        for fornecedor in self.__controlador_ingredientes.__controlador_sistema.__controlador_fornecedor.fornecedores:
            if fornecedor.cnpj == cnpj_fornecedor:
                ref_fornecedor = fornecedor
        if ref_fornecedor is None:
            print('Nenhum fornecedor com o CNPJ informado.')
            return None
        else:
            return {"Data": data, "Nome": nome, "Quantidade": qtde, "Fornecedor": ref_fornecedor}