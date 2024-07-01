from Controladores.controlador_cliente import ControladorCliente
import PySimpleGUI as sg

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
        layout = [  [sg.Text('CLIENTE: Escolha uma opção')],
                    [sg.HorizontalSeparator(color='black')],
                    [sg.Radio('Cadastrar novo cliente', 'RADIO1', default=True, key='cadastrar'),],
                    [sg.Radio('Alterar dados do cliente', 'RADIO1', default=False, key='alterar'),],
                    [sg.Radio('Mostrar todos os dados do cliente', 'RADIO1', default=False, key='mostrar_dados'),],
                    [sg.HorizontalSeparator(color='black')],
                    [sg.Text('PEDIDO: Escolha uma opção')],
                    [sg.Radio('Criar pedido', 'RADIO1', default=False, key='pedir'),],
                    [sg.Radio('Listar pedidos', 'RADIO1', default=False, key='pedidos'),],
                    [sg.Radio('Voltar para a tela inicial', 'RADIO1', default=False, key='inicio'),],
                    [sg.Button('Ok', key='ok'), sg.Button('Cancel')] ]

        window = sg.Window('PIZZARIA', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel' or values['inicio']:
                window.close()
                return 0
            elif event == 'ok':
                if values['cadastrar']:
                    window.close()
                    return 1
                elif values['alterar']:
                    window.close()
                    return 2
                elif values['mostrar_dados']:
                    window.close()
                    return 3
                elif values['pedir']:
                    window.close()
                    return 4
                elif values['pedidos']:
                    window.close()
                    return 5

    def print_opcao(self, opcao):
        layout = [  [sg.Text(f'{opcao}')],
                    [sg.Button('Ok')]]
        window = sg.Window('PIZZARIA', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Ok': 
                break
        window.close()

    def print_opcao2(self, opcao):
        layout = [  [sg.Text(f'{opcao}')],
                    [sg.Button('Sim')], [sg.Button('Não')]]
        window = sg.Window('PIZZARIA', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Não': 
                window.close()
                return 2
            elif event == 'Sim':
                window.close()
                return 1
        

    def input_opcao(self, opcao):
        layout = [  [sg.Text(f'{opcao}')],
                    [sg.InputText(key='input')],
                    [sg.Button('Ok')], sg.Button('Cancel')],
        window = sg.Window('PIZZARIA', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': 
                break
            elif event == 'Ok':
                window.close()
                return values['input']
        window.close()


    def cadastra_cliente(self):
            layout = [  [sg.Text('Preencha os campos abaixo')],
                        [sg.HorizontalSeparator(color='black')],
                        [sg.Text('Nome'), sg.InputText(key='nome'),],
                        [sg.Text('Idade'), sg.InputText(key='idade'),],
                        [sg.Text('CPF'), sg.InputText(key='cpf'),],
                        [sg.Text('Endereço'), sg.InputText(key='endereço'),],
                        [sg.Text('Telefone'), sg.InputText(key='telefone'),],
                        [sg.Button('Ok', key='ok'), sg.Button('Cancel')] ]

            window = sg.Window('PIZZARIA', layout)

            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event == 'Cancel': 
                    break
                elif event == 'ok':
                    nome = values['nome']
                    idade = values['idade']
                    cpf = values['cpf']
                    endereco = values['endereço']
                    telefone = values['telefone']
                    window.close()
                    return [nome, idade, cpf, endereco, telefone]
            window.close()

    def altera_cliente(self):
            layout = [  [sg.Text('Preencha os campos abaixo')],
                        [sg.HorizontalSeparator(color='black')],
                        [sg.Text('Nome'), sg.InputText(key='nome'),],
                        [sg.Text('Idade'), sg.InputText(key='idade'),],
                        [sg.Text('Endereço'), sg.InputText(key='endereço'),],
                        [sg.Text('Telefone'), sg.InputText(key='telefone'),],
                        [sg.Button('Ok', key='ok'), sg.Button('Cancel')] ]

            window = sg.Window('PIZZARIA', layout)

            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event == 'Cancel': 
                    break
                elif event == 'ok':
                    nome = values['nome']
                    idade = values['idade']
                    endereco = values['endereço']
                    telefone = values['telefone']
                    window.close()
                    return [nome, idade, endereco, telefone]
            window.close()

    def pega_cpf(self):
        layout = [  [sg.Text('Confirme o CPF do cliente')],
                    [sg.HorizontalSeparator(color='black')],
                    [sg.Text('CPF'), sg.InputText(key='cpf'),],
                    [sg.Button('Ok', key='ok'), sg.Button('Cancel')] ]

        window = sg.Window('PIZZARIA', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': 
                break
            elif event == 'ok':
                window.close()
                return values['cpf']
        window.close()

    def escolhe_sabor(self):
        layout = [  [sg.Text('Escolha o sabor')],
                    [sg.HorizontalSeparator(color='black')],
                    [sg.Radio('Calabresa', 'RADIO1', default=True, key='calabresa'),],
                    [sg.Radio('Portuguesa', 'RADIO1', default=False, key='portuguesa'),],
                    [sg.Radio('Frango', 'RADIO1', default=False, key='frango'),],
                    [sg.Button('Ok', key='ok'), sg.Button('Cancel')] ]

        window = sg.Window('PIZZARIA', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': 
                break
            elif event == 'ok':
                if values['calabresa']:
                    window.close()
                    return 'calabresa'
                elif values['portuguesa']:
                    window.close()
                    return 'portuguesa'
                elif values['frango']:
                    window.close()
                    return 'frango'
                # return values['sabor']
        window.close()

    def escolhe_tamanho(self):
        layout = [  [sg.Text('Escolha o tamanho')],
                    [sg.HorizontalSeparator(color='black')],
                    [sg.Radio('Broto', 'RADIO1', default=False, key='broto'),],
                    [sg.Radio('Média', 'RADIO1', default=True, key='media'),],
                    [sg.Radio('Grande', 'RADIO1', default=False, key='grande'),],
                    [sg.Button('Ok', key='ok'), sg.Button('Cancel')] ]

        window = sg.Window('PIZZARIA', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': 
                break
            elif event == 'ok':
                if values['broto']:
                    window.close()
                    return 'broto'
                elif values['media']:
                    window.close()
                    return 'media'
                elif values['grande']:
                    window.close()
                    return 'grande'
        window.close()