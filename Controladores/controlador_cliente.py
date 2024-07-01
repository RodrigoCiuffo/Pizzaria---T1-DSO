from Entidades.cliente import Cliente
# from Controladores.controlador_sistema import ControladorSistema
from Entidades.pedido import Pedido
from Entidades.Enum.tamanho_pizza import TamanhoPizza
from Entidades.Enum.sabor_pizza import SaborPizza


class ControladorCliente():
    # def __init__(self, controlador_sistema: ControladorSistema):
    def __init__(self, controlador_sistema):
        imports = self.gerencia_imports()
        self.__controlador_sistema = controlador_sistema
        self.__tela_clientes = imports["Tela"](self)
        self.__clientes = [
            Cliente('rodrigo', 24, '12345678910', 'Rua dos Bobos, N° 0', '12345678')]
        self.__cliente_atual = self.__clientes[0]
        self.__pedido_finalizado = False

    @property
    def clientes(self):
        return self.__clientes

    def gerencia_imports(self):
        from Telas.tela_clientes import TelaClientes
        return {"Tela": TelaClientes}

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

    # def checa_cpf_lista(self):
    #     cpf = input('Digite o cpf sem separação: ')
    #     for cliente in self.__clientes:
    #         if cliente.cpf == cpf:
    #             return self.__tela_clientes.print_opcao('O CLIENTE JÁ EXISTE!')
    #     return cpf

    def adiciona_cliente(self):
        # nome = input('Digite o nome: ')
        # idade = input('Digite a idade: ')
        # # self.checa_int(idade)
        # cpf = int(input('Digite o cpf sem separação: '))
        # # self.checa_int(cpf)
        # endereco = input('Digite o nome o endereco (Rua do bobo, número 0): ')
        # telefone = input('Digite o telefone sem separação (DDD + telefone): ')
        # # self.checa_int(telefone)
        dados = self.__tela_clientes.cadastra_cliente()
        nome = dados[0]
        idade = dados[1]
        cpf = dados[2]
        int(cpf)
        endereco = dados[3]
        telefone = dados[4]
        novo_cliente = Cliente(nome, idade, cpf, endereco, telefone)
        self.__clientes.append(novo_cliente)
        self.__cliente_atual = novo_cliente
        self.__tela_clientes.print_opcao('CLIENTE CADASTRADO COM SUCESSO!')

    def altera_dados(self):
        cpf = self.__tela_clientes.pega_cpf()
        if isinstance(self.checa_cpf(cpf), Cliente):
            self.__cliente_atual = self.checa_cpf(cpf)
        # if cpf == 0 or nome == 'sair':
        #     return self.abre_tela_clientes()
        # self.checa_cpf(cpf)
            # nome = self.__tela_clientes.input_opcao('Digite o novo nome: ')
            # idade = int(self.__tela_clientes.input_opcao(
            #     'Digite a nova idade: '))
            # endereco = self.__tela_clientes.input_opcao(
            #     'Digite o novo endereço (Rua dos bobos, número 0): ')
            # telefone = self.__tela_clientes.input_opcao(
            #     input('Digite o novo telefone: '))
        # for cliente in self.__clientes:
        #     if cliente.cpf == cpf:
            dados = self.__tela_clientes.altera_cliente()
            nome = dados[0]
            idade = dados[1]
            endereco = dados[2]
            telefone = dados[3]
            self.__cliente_atual.nome = nome
            self.__cliente_atual.idade = idade
            self.__cliente_atual.endereco = endereco
            self.__cliente_atual.telefone = telefone
            return self.__tela_clientes.print_opcao('DADOS ALTERADOS COM SUCESSO!')
        return self.__tela_clientes.print_opcao('CLIENTE NÃO ENCONTRADO!')

    def mostrar_dados(self):
        cpf = self.__tela_clientes.pega_cpf()
        if isinstance(self.checa_cpf(cpf), Cliente):
            self.__cliente_atual = self.checa_cpf(cpf)
        dados = ['DADOS DO CLIENTE',
                 f'Nome: {self.__cliente_atual.nome}',
                 f'Idade: {self.__cliente_atual.idade}',
                 f'CPF: {self.__cliente_atual.cpf}',
                 f'Endereco: {self.__cliente_atual.endereco}',
                 f'Telefone: {self.__cliente_atual.telefone}',]
        return self.__tela_clientes.print_opcao('\n'.join(dados))

    def cria_pedido(self):
        data = self.__tela_clientes.input_opcao(
            'Digite a data do pedido (ex: 19/05/2024): ')
        # pedido =  self.__cliente_atual.realiza_pedidos(data)
        # self.__tela_clientes.print_opcao('Selecione a(s) pizzas para o pedido')
        # self.__tela_clientes.print_opcao('----------SABOR----------')
        loop = True
        sabor_pizza = ''
        while loop:
            sabor_escolhido = self.__tela_clientes.escolhe_sabor()
            for sabor in SaborPizza:
                if sabor.value == sabor_escolhido:
                    sabor_pizza = sabor
                    loop = False
                    break
            if loop is True:
                self.__tela_clientes.print_opcao('Informe uma opcao válida!')
        # self.__tela_clientes.print_opcao('----------TAMANHO----------')
        loop = True
        tamanho_pizza = ''
        while loop:
            tamanho_escolhido = self.__tela_clientes.escolhe_tamanho()
            for tamanho in TamanhoPizza:
                if tamanho.value == tamanho_escolhido:
                    tamanho_pizza = tamanho
                    loop = False
                    break
            if loop is True:
                self.__tela_clientes.print_opcao('Informe uma opcao válida!')
        saida_ingredientes = self.__controlador_sistema.controlador_armazem.sai_ingredientes(
            sabor_pizza, tamanho_pizza)
        if saida_ingredientes:
            pedido = Pedido(self.__cliente_atual,
                            sabor_pizza, tamanho_pizza, data)
            mais_pizza = int(self.__tela_clientes.input_opcao2(
                'Deseja adicionar mais uma pizza?'))
        else:
            self.__tela_clientes.print_opcao(
                'Quantidade de ingredientes insuficiente. Favor alterar o tamanho e/ou sabor.\nContate o gerente em caso de dúvidas.')

        while mais_pizza == 1:
            # pedido =  self.__cliente_atual.realiza_pedidos(data)
            # self.__tela_clientes.print_opcao(
            #     'Selecione a(s) pizzas para o pedido')
            # self.__tela_clientes.print_opcao('----------SABOR----------')
            loop = True
            sabor_pizza = ''
            while loop:
                sabor_escolhido = self.__tela_clientes.escolhe_sabor()
                for sabor in SaborPizza:
                    if sabor.value == sabor_escolhido:
                        sabor_pizza = sabor
                        loop = False
                        break
                if loop is True:
                    self.__tela_clientes.print_opcao(
                        'Informe uma opcao válida!')
            # self.__tela_clientes.print_opcao('----------TAMANHO----------')
            loop = True
            tamanho_pizza = ''
            while loop:
                tamanho_escolhido = self.__tela_clientes.escolhe_tamanho()
                for tamanho in TamanhoPizza:
                    if tamanho.value == tamanho_escolhido:
                        tamanho_pizza = tamanho
                        loop = False
                        break
                if loop is True:
                    self.__tela_clientes.print_opcao(
                        'Informe uma opcao válida!')
            saida_ingredientes = self.__controlador_sistema.controlador_armazem.sai_ingredientes(
                sabor_pizza, tamanho_pizza)
            if saida_ingredientes:
                pedido = Pedido(self.__cliente_atual,
                                sabor_pizza, tamanho_pizza, data)
                mais_pizza = int(self.__tela_clientes.input_opcao2(
                    'Deseja adicionar mais uma pizza?'))
            else:
                self.__tela_clientes.print_opcao(
                    'Quantidade de ingredientes insuficiente. Favor alterar o tamanho e/ou sabor.\nContate o gerente em caso de dúvidas.')
            # self.__controlador_sistema.controlador_armazem.sai_ingredientes(sabor_pizza, tamanho_pizza)
            # pedido.adiciona_pizza(sabor_pizza, tamanho_pizza)
            # mais_pizza = int(self.__tela_clientes.input_opcao('Deseja adicionar mais uma pizza?\n 1 - Sim\n 2 - Não\n ->: '))
        # self.__tela_clientes.print_opcao('PEDIDO FINALIZADO!')
        self.__cliente_atual.pedidos.append(pedido)
        return self.__tela_clientes.print_opcao('PEDIDO REALIZADO COM SUCESSO!')

    def pedidos(self):
        for pedido in self.__cliente_atual.pedidos:
            self.__tela_clientes.print_opcao(
                '------------------------------------')
            self.__tela_clientes.print_opcao(f'Cliente: {pedido.cliente}')
            # self.__tela_clientes.print_opcao("Cliente: ", self.__cliente_atual.nome)
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
            # return self.__tela_clientes.print_opcao(funcao_escolhida)
            # if opcao == 3 or opcao == 5:
            #     print(funcao_escolhida())
            # else:
            #     funcao_escolhida()
            # self.__tela_clientes.print_opcao(funcao_escolhida())
