from Telas.tela_clientes import TelaClientes
from Entidades.cliente import Cliente
from Entidades.pedido import Pedido
from controlador_sistema import ControladorSistema


class ControladorCliente():
    def __init__(self, controlador_sistema: ControladorSistema,):
        self.__controlador_sistema = controlador_sistema
        self.__tela_clientes = TelaClientes(self)
        self.__clientes = []
        self.__cliente_atual = None

    def adiciona_cliente(self):
        nome = input('Digite o nome: ')
        idade = input(int('Digite a idade: '))
        cpf = input(int('Digite o cpf sem separação:'))
        endereco = input('Digite o nome o endereco (Rua do bobo, número 0): ')
        telefone = input(
            int('Digite o telefone sem separação (DDD + telefone): '))
        if (type(nome) == str and
            type(idade) == int and
            type(cpf) == int and
            type(endereco) == str and
                type(telefone) == int):
            novo_cliente = Cliente(nome, idade, cpf, endereco, telefone)
            self.__clientes.append(novo_cliente)
            self.__cliente_atual = novo_cliente

    def altera_dados(self):
        cpf = input(int('Confirme o CPF do cliente para alterar os dados: '))
        while cpf.len() != 11 or cpf != 0:
            cpf = input(int(
                'Confirme o CPF do cliente com 11 dígitos para alterar os dados ou digite 0 para cancelar: '))
        if cpf == 0 or nome == 'sair':
            return self.abre_tela_clientes()
        nome = input('Digite o novo nome: ')
        idade = input(int('Digite a nova idade: '))
        endereco = input('Digite o novo endereço (Rua dos bobos, número 0): ')
        telefone = input(int('Digite o novo telefone'))
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                cliente.nome = nome
                cliente.idade = idade
                cliente.endereco = endereco
                cliente.telefone = telefone
                return 'Dados alterados com sucesso'
        return 'Cliente não encontrado'

    def mostrar_dados(self):
        return ('Nome: ' + self.__cliente_atual.nome(),
                'Idade: ' + self.__cliente_atual.idade(),
                'Cpf: ' + self.__cliente_atual.cpf(),
                'Endereço: ' + self.__cliente_atual.endereco(),
                'Telefone: ' + self.__cliente_atual.telefone())

    # def cria_pedido(self):


    def pedidos(self):
        return self.__cliente_atual.pedidos()

    def abre_tela_clientes(self):
        switcher = {
            0: self.__controlador_sistema.tela_sistema,
            1: self.adicional_cliente,
            2: self.altera_dados,
            3: self.mostrar_dados,
            4: self.cria_pedido,
            5: self.pedidos
        }
        while True:
            opcao = self.__tela_clientes.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            if opcao == 3 or opcao == 5:
                print(funcao_escolhida())
            else:
                funcao_escolhida()
            # self.__tela_clientes.print_opcao(funcao_escolhida())
