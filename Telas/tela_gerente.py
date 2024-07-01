from Controladores.controlador_gerente import ControladorGerente
import PySimpleGUI as sg

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
        layout = [  [sg.Text('GERENTE: Escolha uma opção')],
                    [sg.HorizontalSeparator(color='black')],
                    [sg.Radio('Cadastrar novo gerente', 'RADIO1', default=True, key='cadastrar'),],
                    [sg.Radio('Excluir gerente atual', 'RADIO1', default=False, key='excluir'),],
                    [sg.Radio('Alterar dados do gerente', 'RADIO1', default=False, key='alterar'),],
                    [sg.Radio('Mostrar todos os dados do gerente', 'RADIO1', default=False, key='mostrar_dados'),],
                    [sg.Radio('Gerar relatorio de pedidos', 'RADIO1', default=False, key='pedidos'),],
                    [sg.Radio('Gerar relatorio de ingredientes', 'RADIO1', default=False, key='ingredientes'),],
                    [sg.Radio('Voltar para a tela inicial', 'RADIO1', default=False, key='inicio'),],
                    [sg.Button('Ok', key='ok'), sg.Button('Cancel')] ]

        window = sg.Window('PIZZARIA', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel' or values['inicio']:
                window.close()
                self.__controlador.controlador_sistema.acessa_tela_sistema()
                break
            elif event == 'ok':
                if values['cadastrar']:
                    window.close()
                    return 1
                elif values['excluir']:
                    window.close()
                    return 2
                elif values['alterar']:
                    window.close()
                    return 3
                elif values['mostrar_dados']:
                    window.close()
                    return 4
        
    def print_opcao(self, opcao):
        layout = [  [sg.Text(f'{opcao}')],
                    [sg.Button('Ok')]]
        window = sg.Window('PIZZARIA', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Ok': 
                break
        window.close()


    def exclui_gerente(self, opcao):
        print(opcao)
        layout = [  [sg.Text(f'{opcao}')],
                    [sg.Button('Yes'), sg.Button('No')]
            ]
        window = sg.Window('PIZZARIA', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'No': 
                window.close()
                return 2
            elif event == 'Yes':
                window.close()
                return 1

    def cadastra_gerente(self):
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

    def altera_gerente(self):
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