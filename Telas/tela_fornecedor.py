from Controladores.controlador_fornecedor import ControladorFornecedor

class TelaFornecedor():

    def __init__(self, controlador_fornecedor: ControladorFornecedor):
        self.__controladorFornecedor = controlador_fornecedor

    def opcoes_fornecedor(self):
        print("-------- FORNECEDOR ----------")
        print("Escolha a opcao:")
        print("1 - Incluir Fornecedor")
        print("2 - Excluir Fornecedor")
        print("3 - Alterar Fornecedor")
        print("4 - Mostrar Fornecedores")
        print("0 - Retornar")

        while True:
            try:
                escolha = int(input('Digite uma das opções listadas: '))
                if escolha >= 0 and escolha <= 5:
                    break
                else:
                    print('Entrada inválida! O número informado não está entre as opções.')
            except ValueError:
                print('Entrada inválida! O número informado não é um inteiro.')
        return escolha

    def cadastro_fornecedor(self):
        razao_social = input('Digite a razão social do fornecedor: ')
        fornecedores = self.__controladorFornecedor.fornecedores
        while True:
            try:
                cnpj = int(input('Digite o CNPJ do fornecedor: '))
            except ValueError:
                print('CNPJ deve ser um número. Tente novamente.')
                continue

            cnpj_existe = False
            for fornecedor in fornecedores:
                if fornecedor.cnpj == cnpj:
                    cnpj_existe = True
            if cnpj_existe:
                print('Já existe um fornecedor com esse CNPJ! Tente novamente.')
                cnpj_existe = False
            else:
                break
        email = input('Digite o email do fornecedor: ')
        while True:
            try:
                telefone = int(input('Digite o telefone do fornecedor: '))
                break
            except ValueError:
                print('Telefone deve ser um número. Tente novamente.')
        return {"Razao Social": razao_social, "CNPJ": cnpj, "Email": email, "Telefone": telefone}

    def exclusao_fornecedor(self):
        cnpj = int(input('Digite o CNPJ da empresa a ser excluida'))
        return cnpj
        
    def altera_dados_fornecedor(self):
        cnpj = int(input('Digite o CNPJ do fornecedor a ter seus dados alterados'))
        #checar tipo e se existe na lista 
        
        checa_razao = ''
        while checa_razao != 'S' and checa_razao != 'N':
            checa_razao = input('Deseja alterar a razao social? Digite "S" para Sim ou "N" para Nao')
        if checa_razao == 'S':
            nova_razao = input('Digite a nova razao social do fornecedor')

        checa_cnpj = ''
        while checa_cnpj != 'S' and checa_cnpj != 'N':
            checa_cnpj = input('Deseja alterar o CNPJ? Digite "S" para Sim ou "N" para Nao')
        if checa_cnpj == 'S':
            novo_cnpj = int(input('Digite o novo número de CNPJ do fornecedor'))

        checa_email = ''
        while checa_email != 'S' and checa_email != 'N':
            checa_email = input('Deseja alterar o email? Digite "S" para Sim ou "N" para Nao')
        if checa_email == 'S':
            novo_email = input('Digite o novo endereco de email do fornecedor')

        checa_telefone = ''
        while checa_telefone != 'S' and checa_telefone != 'N':
            checa_telefone = input('Deseja alterar o numero de telefone? Digite "S" para Sim ou "N" para Nao')
        if checa_telefone == 'S':
            novo_telefone = int(input('Digite o novo numero de telefone do fornecedor'))

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
            print('---------------------------------------------')
            print("Razao Social: ", fornecedor.razao_social)
            print("CNPJ: ", fornecedor.cnpj)
            print("Email: ", fornecedor.email)
            print("Telefone: ", fornecedor.telefone)
            print('---------------------------------------------')
