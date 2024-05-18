from Controladores.controlador_cliente import ControladorCliente

class TelaClientes():
    def __init__(self, controlador: ControladorCliente):
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
        print('1 - Cadastrar novo cliente')
        print('2 - Alterar dados do cliente')
        print('3 - Mostrar todos os dados do cliente')
        print('----------OPÇÕES DE PEDIDOS----------')
        print('4 - Criar pedido')
        print('5 - Listar pedidos')
        print('-------------------------------------')
        print('0 - Voltar para a tela inicial')
        opcao = self.le_numero('Digite uma das opções: ', [1, 2, 3, 4, 5, 0])
        return opcao
    
    def print_opcao(self, opcao):
        print(opcao)