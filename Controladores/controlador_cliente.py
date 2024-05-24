from Entidades.cliente import Cliente
from Entidades.pedido import Pedido
from Entidades.Enum.tamanho_pizza import TamanhoPizza
from Entidades.Enum.sabor_pizza import SaborPizza
from Telas.tela_clientes import TelaClientes


class ControladorCliente():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_clientes = TelaClientes(self)
        self.__clientes = []
        self.__cliente_atual = None

    @property
    def clientes(self):
        return self.__clientes

    def checa_int(self, valor: int):
        valor = valor
        while type(valor) != int:
            valor = input(
                'Digite um valor numérico inteiro: ')
        return valor

    def checa_cpf(self, cpf: str):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
        return self.__tela_clientes.print_opcao('Cliente não encontrado!')

    def adiciona_cliente(self):
        nome = self.__tela_clientes.input_opcao('Digite o nome: ')
        idade = self.__tela_clientes.input_opcao('Digite a idade: ')
        cpf = self.__tela_clientes.input_opcao('Digite o cpf sem separação: ')
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return self.__tela_clientes.print_opcao('CPF digitado já pertence a um cliente! Encerrando operação.')
        endereco = self.__tela_clientes.input_opcao('Digite o nome o endereco (Rua do bobo, número 0): ')
        telefone = self.__tela_clientes.input_opcao('Digite o telefone sem separação (DDD + telefone): ')
        novo_cliente = Cliente(nome, idade, cpf, endereco, telefone)
        self.__clientes.append(novo_cliente)
        self.__cliente_atual = novo_cliente

    def altera_dados(self):
        cpf = self.__tela_clientes.input_opcao(
            'Confirme o CPF do cliente para alterar os dados: ')
        if isinstance(self.checa_cpf(cpf), Cliente):
            self.__cliente_atual = self.checa_cpf(cpf)
            nome = self.__tela_clientes.input_opcao('Digite o novo nome: ')
            idade = int(self.__tela_clientes.input_opcao(
                'Digite a nova idade: '))
            endereco = self.__tela_clientes.input_opcao(
                'Digite o novo endereço (Rua dos bobos, número 0): ')
            telefone = self.__tela_clientes.input_opcao(
                input('Digite o novo telefone: '))
            self.__cliente_atual.nome = nome
            self.__cliente_atual.idade = idade
            self.__cliente_atual.endereco = endereco
            self.__cliente_atual.telefone = telefone
            return self.__tela_clientes.print_opcao('DADOS ALTERADOS COM SUCESSO!')
        return self.__tela_clientes.print_opcao('VOLTANDO AO MENU ANTERIOR...')

    def mostrar_dados(self):
        cpf = self.__tela_clientes.input_opcao(
            'Confirme o CPF do cliente para alterar os dados: ')
        if isinstance(self.checa_cpf(cpf), Cliente):
            self.__cliente_atual = self.checa_cpf(cpf)
        dados = [f'---------------DADOS DO CLIENTE---------------',
                f'Nome: {self.__cliente_atual.nome}',
                f'Idade: {self.__cliente_atual.idade}',
                f'CPF: {self.__cliente_atual.cpf}',
                f'Endereco: {self.__cliente_atual.endereco}',
                f'Telefone: {self.__cliente_atual.telefone}',
                f'-----------FIM DOS DADOS DO CLIENTE-----------']
        return self.__tela_clientes.print_opcao('\n'.join(dados))

    def cria_pedido(self):
        data = self.__tela_clientes.input_opcao('Digite a data (ex: 19/05/2024): ')
        self.__tela_clientes.print_opcao('Selecione a(s) pizzas para o pedido')
        self.__tela_clientes.print_opcao('----------SABOR----------')
        loop = True
        sabor_pizza = ''
        while loop:
            sabor_escolhido = self.__tela_clientes.input_opcao(
                'Escolha uma opcao digitando exatamente o seu nome:\n calabresa\n portuguesa\n frango\n ->: ')
            for sabor in SaborPizza:
                if sabor.value == sabor_escolhido:
                    sabor_pizza = sabor
                    loop = False
                    break
            if loop is True:
                self.__tela_clientes.print_opcao('Informe uma opcao válida!')
        self.__tela_clientes.print_opcao('----------TAMANHO----------')
        loop = True
        tamanho_pizza = ''
        while loop:
            tamanho_escolhido = self.__tela_clientes.input_opcao(
                'Escolha uma opcao digitando exatamente o tamanho:\n broto\n media\n grande\n ->:  ')
            for tamanho in TamanhoPizza:
                if tamanho.value == tamanho_escolhido:
                    tamanho_pizza = tamanho
                    loop = False
                    break
            if loop is True:
                self.__tela_clientes.print_opcao('Informe uma opcao válida!')
        saida_ingredientes = self.__controlador_sistema.controlador_armazem.sai_ingredientes(sabor_pizza, tamanho_pizza)
        if saida_ingredientes is True:
            pedido = Pedido(self.__cliente_atual, sabor_pizza, tamanho_pizza, data)
            while True:
                try:
                    mais_pizza = int(self.__tela_clientes.input_opcao('Deseja adicionar mais uma pizza?\n 1 - Sim\n 2 - Não\n ->:  '))
                    if mais_pizza == 1 or mais_pizza == 2:
                        break
                    else:
                        print('Entrada inválida! O número informado não está entre as opções.')
                except ValueError:
                    print('Entrada inválida! O número informado não é um inteiro.')
        else:
            self.__tela_clientes.print_opcao('Quantidade de ingredientes insuficiente. Favor alterar o tamanho e/ou sabor.\nContate o gerente em caso de dúvidas.')
            self.cria_pedido()
        while mais_pizza == 1:
            self.__tela_clientes.print_opcao(
                'Selecione a(s) pizzas para o pedido')
            self.__tela_clientes.print_opcao('----------SABOR----------')
            loop = True
            sabor_pizza = ''
            while loop:
                sabor_escolhido = self.__tela_clientes.input_opcao(
                    'Escolha uma opcao digitando exatamente o seu nome:\n calabresa\n portuguesa\n frango\n ->: ')
                for sabor in SaborPizza:
                    if sabor.value == sabor_escolhido:
                        sabor_pizza = sabor
                        loop = False
                        break
                if loop is True:
                    self.__tela_clientes.print_opcao(
                        'Informe uma opcao válida!')
            self.__tela_clientes.print_opcao('----------TAMANHO----------')
            loop = True
            tamanho_pizza = ''
            while loop:
                tamanho_escolhido = self.__tela_clientes.input_opcao(
                    'Escolha uma opcao digitando exatamente o tamanho:\n broto\n media\n grande\n ->:  ')
                for tamanho in TamanhoPizza:
                    if tamanho.value == tamanho_escolhido:
                        tamanho_pizza = tamanho
                        loop = False
                        break
                if loop is True:
                    self.__tela_clientes.print_opcao(
                        'Informe uma opcao válida!')
            saida_ingredientes = self.__controlador_sistema.controlador_armazem.sai_ingredientes(sabor_pizza, tamanho_pizza)
            if saida_ingredientes is False:
                self.__tela_clientes.print_opcao('Quantidade de ingredientes disponíveis insuficiente. Favor alterar o tamanho e/ou sabor.\nContate o gerente em caso de dúvidas.')
                continue
            else: 
                pedido.adiciona_pizza(sabor_pizza, tamanho_pizza)
                mais_pizza = int(self.__tela_clientes.input_opcao('Deseja adicionar mais uma pizza?\n 1 - Sim\n 2 - Não\n ->:  '))
                while True:
                    try:
                        mais_pizza = int(self.__tela_clientes.input_opcao('Deseja adicionar mais uma pizza?\n 1 - Sim\n 2 - Não\n ->:  '))
                        if mais_pizza == 1 or mais_pizza == 2:
                            break
                        else:
                            print('Entrada inválida! O número informado não está entre as opções.')
                    except ValueError:
                        print('Entrada inválida! O número informado não é um inteiro.')
        self.__cliente_atual.pedidos.append(pedido)
        return self.__tela_clientes.print_opcao('PEDIDO REALIZADO COM SUCESSO!')

    def pedidos(self):
        for pedido in self.__cliente_atual.pedidos:
            self.__tela_clientes.print_opcao(
                '------------------------------------')
            self.__tela_clientes.print_opcao(f'Cliente: {pedido.cliente}')
            self.__tela_clientes.print_opcao(f'Data: {pedido.data}')
            for pizza in pedido.pizzas:
                self.__tela_clientes.print_opcao(
                    f'Pizza: {pizza.sabor.value}, Tamanho: {pizza.tamanho.value}')
            self.__tela_clientes.print_opcao(f'Valor: R${pedido.valor}0')
            self.__tela_clientes.print_opcao(
                '------------------------------------')

    def abre_tela_cliente(self):
        switcher = {
            0: self.__controlador_sistema.acessa_tela_sistema,
            1: self.adiciona_cliente,
            2: self.altera_dados,
            3: self.mostrar_dados,
            4: self.cria_pedido,
            5: self.pedidos
        }
        while True:
            opcao = self.__tela_clientes.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()