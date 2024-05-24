from Controladores.controlador_gerente import ControladorGerente


class TelaGerente():
    def __init__(self, controlador: ControladorGerente):
        self.__controlador = controlador

    def le_num(self, mensagem: str, inteiros_validos: list):
        while True:
            if type(mensagem) == str:
                valor_lido = input(mensagem)
                try:
                    inteiro = int(valor_lido)
                    if inteiros_validos and inteiro not in inteiros_validos:
                        raise ValueError
                    return inteiro
                except ValueError:
                    print('Valor incorreto: Digite um valor numérico inteiro válido')
                    if inteiros_validos:
                        print('Valores válidos: ', inteiros_validos)

    def mostra_tela_opcoes(self):
        print('-------------BEM-VINDO!--------------')
        print('1 - Cadastrar novo gerente')
        print('2 - Excluir gerente atual')
        print('3 - Alterar dados do gerente')
        print('4 - Mostrar todos os dados do gerente')
        print('5 - Gerar relatorio de pedidos')
        print('6 - Gerar relatorio de ingredientes')
        print('-------------------------------------')
        print('0 - Voltar para a tela inicial')
        opcao = self.le_num('Digite uma das opções: ', [1, 2, 3, 4, 5, 6, 0])
        return opcao

    def print_opcao(self, opcao):
        print(opcao)

    def input_opcao(self, opcao):
        retorno = input(opcao)
        return retorno

    def input_opcao_int(self, opcao):
        retorno = int(input(opcao))
        return retorno
