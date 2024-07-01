from Controladores.controlador_fornecedor import ControladorFornecedor
import PySimpleGUI as sg

class TelaFornecedor():

    def __init__(self, controlador_fornecedor: ControladorFornecedor):
        self.__controladorFornecedor = controlador_fornecedor

    def opcoes_fornecedor(self):
        layout = [  [sg.Text('FORNECEDOR: Escolha uma opção')],
                    [sg.HorizontalSeparator(color='black')],
                    [sg.Radio('Cadastrar novo fornecedor', 'RADIO1', default=True, key='cadastrar'),],
                    [sg.Radio('Excluir fornecedor', 'RADIO1', default=False, key='excluir'),],
                    [sg.Radio('Alterar dados do fornecedor', 'RADIO1', default=False, key='alterar'),],
                    [sg.Radio('Mostrar todos os dados do fornecedor', 'RADIO1', default=False, key='mostrar_dados'),],
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
                elif values['excluir']:
                    window.close()
                    return 2
                elif values['alterar']:
                    window.close()
                    return 3
                elif values['mostrar_dados']:
                    window.close()
                    return 4

    def cadastro_fornecedor(self):
        layout = [  [sg.Text('Preencha os campos abaixo')],
                    [sg.HorizontalSeparator(color='black')],
                    [sg.Text('Razão sozial'), sg.InputText(key='razao'),],
                    [sg.Text('CNPJ'), sg.InputText(key='cnpj'),],
                    [sg.Text('E-mail'), sg.InputText(key='email'),],
                    [sg.Text('Telefone'), sg.InputText(key='telefone'),],
                    [sg.Button('Ok', key='ok'), sg.Button('Cancel')] ]

        window = sg.Window('PIZZARIA', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
            elif event == 'ok':
                window.close()
                return {"Razao Social": values['razao'], "CNPJ": values['cnpj'], "Email": values['email'], "Telefone": values['telefone']}
            window.close()

    def exclusao_fornecedor(self):
        layout = [  [sg.Text('Digite o CNPJ da empresa a ser excluida')],
                    [sg.HorizontalSeparator(color='black')],
                    [sg.Text('CNPJ'), sg.InputText(key='cnpj'),],
                    [sg.Button('Ok', key='ok'), sg.Button('Cancel')] ]

        window = sg.Window('PIZZARIA', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
            elif event == 'ok':
                window.close()
                return values['cnpj']
            window.close()

    def print_opcao(self, opcao):
        layout = [  [sg.Text(f'{opcao}')],
                    [sg.Button('Ok')]]
        window = sg.Window('PIZZARIA', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Ok': 
                break
        window.close()

    def mostra_fornecedores(self):
        for fornecedor in self.__controladorFornecedor.fornecedores:
            dados = [f'Razao Social: {fornecedor.razao_social}',
                    f'CNPJ: {fornecedor.cnpj}',
                    f'Email: {fornecedor.email}',
                    f'Telefone: {fornecedor.telefone}',
                    ]
            self.print_opcao('\n'.join(dados))

    def altera_dados_fornecedor(self):
        layout = [  [sg.Text('Preencha os campos abaixo')],
                    [sg.HorizontalSeparator(color='black')],
                    [sg.Text('Razão Social'), sg.InputText(key='razao'),],
                    [sg.Text('Email'), sg.InputText(key='email'),],
                    [sg.Text('Telefone'), sg.InputText(key='telefone'),],
                    [sg.Text('CNPJ Atual'), sg.InputText(key='cnpj'),],
                    [sg.Button('Ok', key='ok'), sg.Button('Cancel')] ]

        window = sg.Window('PIZZARIA', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': 
                break
            elif event == 'ok':
                razao = values['razao']
                email = values['email']
                telefone = values['telefone']
                cnpj = values['cnpj']
                window.close()
                return {"Nova Razao": razao, "CNPJ Atual": cnpj, "Novo Email": email, "Novo Telefone": telefone}
        window.close()
        
    def print_opcao(self, opcao):
        layout = [  [sg.Text(f'{opcao}')],
                    [sg.Button('Ok')]]
        window = sg.Window('PIZZARIA', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Ok': 
                break
        window.close()
