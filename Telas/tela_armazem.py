from Controladores.controlador_armazem import ControladorArmazem
import PySimpleGUI as sg

class TelaArmazem():
    def __init__(self, controlador_armazem: ControladorArmazem):
        self.__controlador_armazem = controlador_armazem

    def opcoes_armazem(self):
        layout = [  [sg.Text('Armazem: Escolha uma opção')],
                    [sg.HorizontalSeparator(color='black')],
                    [sg.Radio('Definir armazem', 'RADIO1', default=True, key='resetar'),],
                    [sg.Radio('Mostrar conteúdo do armazem', 'RADIO1', default=False, key='mostrar_dados'),],
                    [sg.Radio('Voltar para a tela inicial', 'RADIO1', default=False, key='inicio'),],
                    [sg.Button('Ok', key='ok'), sg.Button('Cancel')] ]

        window = sg.Window('PIZZARIA', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel' or values['inicio']:
                window.close()
                return 0
            elif event == 'ok':
                if values['resetar']:
                    window.close()
                    return 1
                elif values['mostrar_dados']:
                    window.close()
                    return 2

    def set_armazem(self):
        layout = [  [sg.Text(f'Deseja estabelecer ou resetar para um novo armazem?')],
                    [sg.Button('Sim')], [sg.Button('Não')]]
        window = sg.Window('PIZZARIA', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Não': 
                window.close()
                return 'N'
            elif event == 'Sim':
                window.close()
                return 'S'

    def print_opcao(self, opcao):
        layout = [  [sg.Text(f'{opcao}')],
                    [sg.Button('Ok')]]
        window = sg.Window('PIZZARIA', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Ok': 
                break
        window.close()

    def mostra_ingredientes(self):
        for elemento in self.__controlador_armazem.armazem.estoque:
            dados = ['DADOS DO INGREDIENTE',
                f'Data: {elemento.data}',
                f'Nome: {elemento.nome_ingrediente}',
                f'Quantidade: {elemento.quantidade}',
                f'Fornecedor: {elemento.fornecedor}']
            self.print_opcao('\n'.join(dados))


