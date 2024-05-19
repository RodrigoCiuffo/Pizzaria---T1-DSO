from Entidades.cliente import Cliente
from Controladores.controlador_sistema import ControladorSistema
# from Entidades.pedido import Pedido



class ControladorCliente():
    def __init__(self, controlador_sistema: ControladorSistema):
        imports = self.gerencia_imports()
        self.__controlador_sistema = controlador_sistema
        self.__tela_clientes = imports["Tela"](self)
        self.__clientes = [Cliente('rodrigo', 24, '12345678910', 'Rua dos Bobos, N° 0', 12345678)]
        self.__cliente_atual = self.__clientes[0]

    def gerencia_imports(self):
        from Telas.tela_clientes import TelaClientes
        return {"Tela": TelaClientes, "Controlador Sistema": ControladorSistema}
        

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
        return (self.__cliente_atual.nome,
                self.__cliente_atual.idade,
                self.__cliente_atual.cpf,
                self.__cliente_atual.endereco,
                self.__cliente_atual.telefone)

    def cria_pedido(self):
        pass

    def pedidos(self):
        return self.__cliente_atual.pedidos()

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
            if opcao == 3 or opcao == 5:
                print(funcao_escolhida())
            else:
                funcao_escolhida()
            # self.__tela_clientes.print_opcao(funcao_escolhida())
