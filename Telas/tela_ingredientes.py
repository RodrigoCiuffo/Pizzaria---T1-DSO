# from Controladores.controlador_ingredientes import ControladorIngredientes
from Entidades.Enum.nome_ingrediente import NomeIngrediente
import PySimpleGUI as sg

class TelaIngredientes():
    def __init__(self, controlador_ingredientes):
        self.__controlador_ingredientes = controlador_ingredientes

    def opcoes_ingredientes(self):
        layout = [  [sg.Text('Ingrediente: Escolha uma opção')],
                    [sg.HorizontalSeparator(color='black')],
                    [sg.Radio('Incluir ingrediente', 'RADIO1', default=True, key='criar'),],
                    [sg.Radio('Buscar ingrediente', 'RADIO1', default=False, key='buscar'),],
                    [sg.Radio('Voltar para a tela inicial', 'RADIO1', default=False, key='inicio'),],
                    [sg.Button('Ok', key='ok'), sg.Button('Cancel')] ]

        window = sg.Window('PIZZARIA', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel' or values['inicio']:
                window.close()
                return 0
            elif event == 'ok':
                if values['criar']:
                    window.close()
                    return 1
                elif values['buscar']:
                    window.close()
                    return 2

    def busca_ingrediente(self):
        layout = [  [sg.Text('Preencha os campos abaixo')],
                    [sg.HorizontalSeparator(color='black')],
                    [sg.Text('CNPJ'), sg.InputText(key='cnpj'),],
                    [sg.Text('Data'), sg.InputText(key='data'),],
                    [sg.Button('Ok', key='ok'), sg.Button('Cancel')] ]

        window = sg.Window('PIZZARIA', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': 
                break
            elif event == 'ok':
                cnpj = values['cnpj']
                data = values['data']
                window.close()
                return {"CNPJ": cnpj, "Data": data}
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

    def print_opcao2(self, opcao):
        layout = [  [sg.Text(f'{opcao}')],
                    [sg.Button('Sim')], [sg.button('Não')]]
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


    def printa_tela(self, arg):
        print(arg)
