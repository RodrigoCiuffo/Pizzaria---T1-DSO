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
        
        while True:
            try:
                escolha = int(input('Digite uma das opções listadas: '))
                if escolha >= 0 and escolha <= 5:
                    break
                else:
                    print(
                        'Entrada inválida! O número informado não está entre as opções.')
            except ValueError:
                print('Entrada inválida! O número informado não é um inteiro.')
        return escolha
