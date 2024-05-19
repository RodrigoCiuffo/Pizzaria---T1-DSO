from Entidades.cliente import Cliente
from Controladores.controlador_sistema import ControladorSistema
# from Entidades.pedido import Pedido


class ControladorCliente():
    def __init__(self, controlador_sistema: ControladorSistema):
        imports = self.gerencia_imports()
        self.__controlador_sistema = controlador_sistema
        self.__tela_clientes = imports["Tela"](self)
        self.__clientes = [
            Cliente('rodrigo', 24, 12345678910, 'Rua dos Bobos, N° 0', 12345678)]
        self.__cliente_atual = self.__clientes[0]

    def gerencia_imports(self):
        from Telas.tela_clientes import TelaClientes
        return {"Tela": TelaClientes, "Controlador Sistema": ControladorSistema}

    def checa_int(self, valor: int):
        valor = valor
        while type(valor) != int:
            valor = input(
                'Digite um valor numérico inteiro: ')
        return valor
    
    def checa_cpf(self, cpf: int):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
        return self.__tela_clientes.print_opcao('Cliente não encontrado!')
    
    def checa_cpf_lista(self):
        cpf = input('Digite o cpf sem separação: ')
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return self.__tela_clientes.print_opcao('O CLIENTE JÁ EXISTE!')
        return cpf

    def adiciona_cliente(self):
        nome = input('Digite o nome: ')
        idade = input('Digite a idade: ')
        # self.checa_int(idade)
        cpf = int(input('Digite o cpf sem separação: '))
        # self.checa_int(cpf)
        endereco = input('Digite o nome o endereco (Rua do bobo, número 0): ')
        telefone = input('Digite o telefone sem separação (DDD + telefone): ')
        # self.checa_int(telefone)
        novo_cliente = Cliente(nome, idade, cpf, endereco, telefone)
        self.__clientes.append(novo_cliente)
        self.__cliente_atual = novo_cliente

    def altera_dados(self):
        cpf = int(input('Confirme o CPF do cliente para alterar os dados: '))
        if isinstance(self.checa_cpf(cpf), Cliente):
            self.__cliente_atual = self.checa_cpf(cpf)
        # if cpf == 0 or nome == 'sair':
        #     return self.abre_tela_clientes()
        # self.checa_cpf(cpf)
            nome = input('Digite o novo nome: ')
            idade = int(input('Digite a nova idade: '))
            endereco = input('Digite o novo endereço (Rua dos bobos, número 0): ')
            telefone = int(input('Digite o novo telefone: '))
        # for cliente in self.__clientes:
        #     if cliente.cpf == cpf:
            self.__cliente_atual.nome = nome
            self.__cliente_atual.idade = idade
            self.__cliente_atual.endereco = endereco
            self.__cliente_atual.telefone = telefone
            return self.__tela_clientes.print_opcao('DADOS ALTERADOS COM SUCESSO!')
        return self.__tela_clientes.print_opcao('VOLTANDO AO MENU ANTERIOR...')

    def mostrar_dados(self):
        dados = [f'---------------DADOS DO CLIENTE---------------',
                f'Nome: {self.__cliente_atual.nome}',
                 f'Idade: {self.__cliente_atual.idade}',
                 f'CPF: {self.__cliente_atual.cpf}',
                 f'Endereco: {self.__cliente_atual.endereco}',
                 f'Telefone: {self.__cliente_atual.telefone}',
                 f'-----------FIM DOS DADOS DO CLIENTE-----------']
        return self.__tela_clientes.print_opcao('\n'.join(dados))

    def cria_pedido(self):
        pass

    def pedidos(self):
        return self.__cliente_atual.pedidos

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
