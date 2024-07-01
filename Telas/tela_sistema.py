import PySimpleGUI as sg

class TelaSistema():
    def __init__(self):
        pass

    def opcoes_sistema(self):
        layout = [  [sg.Text('SISTEMA: Escolha uma opção')],
                    [sg.Radio('Fornecedor', 'RADIO1', default=True, key='fornecedor'),],
                    [sg.Radio('Cliente', 'RADIO1', default=False, key='cliente'),],
                    [sg.Radio('Gerente', 'RADIO1', default=False, key='gerente'),],
                    [sg.Radio('Armazem', 'RADIO1', default=False, key='armazem'),],
                    [sg.Radio('Ingredientes', 'RADIO1', default=False, key='ingredientes'),],
                    [sg.Button('Ok', key='ok'), sg.Button('Cancel')] ]

        window = sg.Window('PIZZARIA', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                return 0
            elif event == 'ok':
                if values['fornecedor']:
                    window.close()
                    return 1
                elif values['cliente']:
                    window.close()
                    return 2
                elif values['gerente']:
                    window.close()
                    return 3
                elif values['armazem']:
                    window.close()
                    return 4
                elif values['ingredientes']:
                    window.close()
                    return 5
        window.close()