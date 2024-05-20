from Controladores.controlador_armazem import ControladorArmazem

class TelaArmazem():
    def __init__(self, controlador_armazem: ControladorArmazem):
        self.__controlador_armazem = controlador_armazem

    def opcoes_armazem(self):
        print("-------- ARMAZEM ----------")
        print("Escolha a opcao:")
        print("1 - Incluir Armazem")
        print("2 - Mostrar Conteúdo")
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

    def set_armazem(self):
        while True:
            try:
                verificador = input('Deseja estabelecer ou resetar para um novo armazem? S/N: ').strip().upper()
                if verificador not in ['S', 'N']:
                    raise ValueError("Entrada inválida. Por favor, digite 'S' para Sim ou 'N' para Não.")
                break  
            except ValueError as e:
                print(e)
        return verificador

    def mostra_ingredientes(self):
        for elemento in self.__controlador_armazem.armazem.estoque:
            print("Data: ", elemento.data)
            print("Nome: ", elemento.nome_ingrediente)
            print("Quantidade: ", elemento.quantidade)
            print("Fornecedor: ", elemento.fornecedor)