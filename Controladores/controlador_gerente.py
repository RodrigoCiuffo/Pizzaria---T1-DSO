from Controladores.controlador_cliente import ControladorCliente
from Controladores.controlador_sistema import ControladorSistema
from Entidades.gerente import Gerente


class ControladorGerente():
    def __init__(self, controlador_sistema: ControladorSistema, controlador_cliente: ControladorCliente):
        imports = self.gerencia_imports()
        self.__controlador_sistema = controlador_sistema
        self.__tela_gerente = imports["Tela"](self)
        self.__gerente_atual = None
        self.__controlador_cliente = controlador_cliente

    def gerencia_imports(self):
        from Telas.tela_gerente import TelaGerente
        return {"Tela": TelaGerente}

    def cria_gerente(self):
        if self.__gerente_atual is None:
            nome = self.__tela_gerente.input_opcao('Digite o nome do gerente: ')
            idade = self.__tela_gerente.input_opcao('Digite o idade do gerente: ')
            cpf = self.__tela_gerente.input_opcao('Digite o cpf do gerente: ')
            int(cpf)
            endereco = self.__tela_gerente.input_opcao('Digite o endereço do gerente: ')
            telefone = self.__tela_gerente.input_opcao('Digite o telefone do gerente: ')
            int(telefone)
            self.__gerente_atual = Gerente(nome, idade, cpf, endereco, telefone)
            return self.__tela_gerente.print_opcao('GERENTE CADASTRADO COM SUCESSO!')
        return self.__tela_gerente.print_opcao('JÁ EXISTE UM GERENTE CADASTRADO!')
    
    def exclui_gerente(self):
        cpf = input('Confirme o CPF do gerente para prosseguir: ')
        if  self.__gerente_atual.acesso_administrativo(cpf):
            self.__tela_gerente.print_opcao('Tem certeza que deseja excluir o cadastro do gerente atual?: ')
            confirma = int(input('1 - Sim\n2 - Não:\n'))
            if confirma == 1:
                self.__gerente_atual = None
                return self.__tela_gerente.print_opcao('GERENTE EXCLUIDO COM SUCESSO!')
            return self.__tela_gerente.print_opcao('OPERAÇÃO CANCELADA!')
        return self.__tela_gerente.print_opcao('ACESSO NEGADO!')
    
    def altera_dados(self):
        cpf = input('Confirme o CPF do gerente para prosseguir: ')
        if  self.__gerente_atual.acesso_administrativo(cpf):
            nome = input('Digite o novo nome: ')
            idade = input('Digite a nova idade: ')
            endereco = input('Digite o novo endereço (Rua dos bobos, número 0): ')
            telefone = input('Digite o novo telefone: ')
            self.__gerente_atual.nome = nome
            self.__gerente_atual.idade = idade
            self.__gerente_atual.endereco = endereco
            self.__gerente_atual.telefone = telefone
            return self.__tela_gerente.print_opcao('DADOS ALTERADOS COM SUCESSO!')
        return self.__tela_gerente.print_opcao('ACESSO NEGADO!')
    
    def mostrar_dados(self):
        # cpf = int(input('Confirme o CPF do gerente para prosseguir: '))
        if self.__gerente_atual is None:
            return self.__tela_gerente.print_opcao('SEM GERENTE CADASTRADO!')
        cpf = self.__tela_gerente.input_opcao('Confirme o CPF do gerente para prosseguir: ')
        if  self.__gerente_atual.acesso_administrativo(cpf):
            dados = [f'---------------DADOS DO GERENTE---------------',
                    f'Nome: {self.__gerente_atual.nome}',
                    f'Idade: {self.__gerente_atual.idade}',
                    f'CPF: {self.__gerente_atual.cpf}',
                    f'Endereco: {self.__gerente_atual.endereco}',
                    f'Telefone: {self.__gerente_atual.telefone}',
                    f'-----------FIM DOS DADOS DO GERENTE-----------']
            return self.__tela_gerente.print_opcao('\n'.join(dados))
        return self.__tela_gerente.print_opcao('ACESSO NEGADO!')

    def gera_relatorio_pedidos(self):
        clientes = self.__controlador_cliente.__clientes
        for cliente in clientes:
            for pedido in cliente.pedidos:
                self.__gerente_atual.relatorio_pedido.append(pedido)
        return self.__gerente_atual.relatorio_pedido
    
    def gera_relatorio_ingredientes(self):
        estoque = self.__controlador_sistema.__controlador_armazem.armazem.estoque
        for ingrediente in estoque:
            dados_ingrediente = f'Nome: {ingrediente.nome}\n' + f'Quantidade: {ingrediente.quantidade}\n' + f'Data: {ingrediente.data}\n' + f'Fornecedor: {ingrediente.fornecedor}\n'
            self.__gerente_atual.relatorio_ingredientes.append(dados_ingrediente)
        return self.__gerente_atual.relatorio_ingredientes
    
    def abre_tela_gerente(self):
        switcher = {
            0: self.__controlador_sistema.acessa_tela_sistema,
            1: self.cria_gerente,
            2: self.exclui_gerente,
            3: self.altera_dados,
            4: self.mostrar_dados,
            5: self.gera_relatorio_pedidos,
            6: self.gera_relatorio_ingredientes
        }
        while True:
            opcao = self.__tela_gerente.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()