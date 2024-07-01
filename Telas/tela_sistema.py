import PySimpleGUI as sg

class TelaSistema():
    def __init__(self):
        pass

    def opcoes_sistema(self):
        # print("-------- Pizzaria ---------")
        # print("Escolha sua opcao")
        # print("1 - Fornecedor")
        # print("2 - Cliente")
        # print("3 - Gerente")
        # print("4 - Armazem")
        # print("5 - Ingredientes")
        # print("0 - Encerrar sessão")

        # opcao = int(input("Escolha a opcao: "))
        # return opcao

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
                break
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