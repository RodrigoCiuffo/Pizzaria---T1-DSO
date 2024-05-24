class TelaSistema():
    def __init__(self):
        pass

    def opcoes_sistema(self):
        print("-------- Pizzaria ---------")
        print("Escolha sua opcao")
        print("1 - Fornecedor")
        print("2 - Cliente")
        print("3 - Gerente")
        print("4 - Armazem")
        print("5 - Ingredientes")
        print("0 - Encerrar sessão")

        opcao = int(input("Escolha a opcao: "))
        return opcao
