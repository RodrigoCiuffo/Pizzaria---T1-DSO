from Controladores.controlador_fornecedor import ControladorFornecedor
import PySimpleGUI as sg

class TelaFornecedor():

    def __init__(self, controlador_fornecedor: ControladorFornecedor):
        self.__controladorFornecedor = controlador_fornecedor

    def opcoes_fornecedor(self):
        # print("-------- FORNECEDOR ----------")
        # print("Escolha a opcao:")
        # print("1 - Incluir Fornecedor")
        # print("2 - Excluir Fornecedor")
        # print("3 - Alterar Fornecedor")
        # print("4 - Mostrar Fornecedores")
        # print("0 - Retornar")
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
        #     except ValueError:
        #         print('CNPJ deve ser um número. Tente novamente.')
        #         continue

        #     cnpj_existe = False
        #     for fornecedor in fornecedores:
        #         if fornecedor.cnpj == cnpj:
        #             cnpj_existe = True
        #     if cnpj_existe:
        #         print('Já existe um fornecedor com esse CNPJ! Tente novamente.')
        #         cnpj_existe = False
        #     else:
        #         break
        # email = input('Digite o email do fornecedor: ')
        # while True:
        #     try:
        #         telefone = int(input('Digite o telefone do fornecedor: '))
        #         break
        #     except ValueError:
        #         print('Telefone deve ser um número. Tente novamente.')
        # return {"Razao Social": razao_social, "CNPJ": cnpj, "Email": email, "Telefone": telefone}

    def exclusao_fornecedor(self):
        # cnpj = int(input('Digite o CNPJ da empresa a ser excluida'))
        # return cnpj
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

    def altera_dados_fornecedor(self):
        cnpj = int(
            input('Digite o CNPJ do fornecedor a ter seus dados alterados'))
        # checar tipo e se existe na lista

        checa_razao = ''
        while checa_razao != 'S' and checa_razao != 'N':
            checa_razao = input(
                'Deseja alterar a razao social? Digite "S" para Sim ou "N" para Nao')
        if checa_razao == 'S':
            nova_razao = input('Digite a nova razao social do fornecedor')

        checa_cnpj = ''
        while checa_cnpj != 'S' and checa_cnpj != 'N':
            checa_cnpj = input(
                'Deseja alterar o CNPJ? Digite "S" para Sim ou "N" para Nao')
        if checa_cnpj == 'S':
            novo_cnpj = int(
                input('Digite o novo número de CNPJ do fornecedor'))

        checa_email = ''
        while checa_email != 'S' and checa_email != 'N':
            checa_email = input(
                'Deseja alterar o email? Digite "S" para Sim ou "N" para Nao')
        if checa_email == 'S':
            novo_email = input('Digite o novo endereco de email do fornecedor')

        checa_telefone = ''
        while checa_telefone != 'S' and checa_telefone != 'N':
            checa_telefone = input(
                'Deseja alterar o numero de telefone? Digite "S" para Sim ou "N" para Nao')
        if checa_telefone == 'S':
            novo_telefone = int(
                input('Digite o novo numero de telefone do fornecedor'))

        alteracoes = {}
        alteracoes["CNPJ Atual"] = cnpj
        if checa_razao == 'S':
            alteracoes["Nova Razao"] = nova_razao
        if checa_cnpj == 'S':
            alteracoes["Novo CNPJ"] = novo_cnpj
        if checa_email == 'S':
            alteracoes["Novo Email"] = novo_email
        if checa_telefone == 'S':
            alteracoes["Novo Telefone"] = novo_telefone

        return alteracoes

    def mostra_fornecedores(self):
        for fornecedor in self.__controladorFornecedor.fornecedores:
            dados = [f'Razao Social: {fornecedor.razao_social}',
                     f'CNPJ: {fornecedor.cnpj}',
                     f'Email: {fornecedor.email}',
                     f'Telefone: {fornecedor.telefone}',
                     ]
            self.print_opcao('\n'.join(dados))
            # print('---------------------------------------------')
            # print("Razao Social: ", fornecedor.razao_social)
            # print("CNPJ: ", fornecedor.cnpj)
            # print("Email: ", fornecedor.email)
            # print("Telefone: ", fornecedor.telefone)
            # print('---------------------------------------------')
