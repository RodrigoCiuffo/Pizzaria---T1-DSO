from Entidades.gerente import Gerente


class ControladorGerente():
    def __init__(self, controlador_sistema):
        imports = self.gerencia_imports()
        self.__controlador_sistema = controlador_sistema
        self.__tela_gerente = imports["Tela"](self)
        self.__gerente_atual = None

    def gerencia_imports(self):
        from Telas.tela_gerente import TelaGerente
        return {"Tela": TelaGerente}

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    def cria_gerente(self):
        if self.__gerente_atual is None:
            dados = self.__tela_gerente.cadastra_gerente()
            nome = dados[0]
            idade = dados[1]
            cpf = dados[2]
            int(cpf)
            endereco = dados[3]
            telefone = dados[4]
            # int(telefone)
            self.__gerente_atual = Gerente(
                nome, idade, cpf, endereco, telefone)
            return self.__tela_gerente.print_opcao('GERENTE CADASTRADO COM SUCESSO!')
        return self.__tela_gerente.print_opcao('JÁ EXISTE UM GERENTE CADASTRADO!')

    def exclui_gerente(self):
        # cpf = input('Confirme o CPF do gerente para prosseguir: ')
        # if self.__gerente_atual.acesso_administrativo(cpf):
        
        confirma = self.__tela_gerente.exclui_gerente(
            'Tem certeza que deseja excluir o cadastro do gerente atual?: ')
        if confirma == 1:
            self.__gerente_atual = None
            return self.__tela_gerente.print_opcao('GERENTE EXCLUIDO COM SUCESSO!')
        return self.__tela_gerente.print_opcao('OPERAÇÃO CANCELADA!')
        # return self.__tela_gerente.print_opcao('ACESSO NEGADO!')

    def altera_dados(self):
        # cpf = input('Confirme o CPF do gerente para prosseguir: ')
        # if self.__gerente_atual.acesso_administrativo(cpf):
        if self.__gerente_atual is not None:
            dados = self.__tela_gerente.altera_gerente()
            nome = dados[0]
            idade = dados[1]
            endereco = dados[2]
            telefone = dados[3]
            self.__gerente_atual.nome = nome
            self.__gerente_atual.idade = idade
            self.__gerente_atual.endereco = endereco
            self.__gerente_atual.telefone = telefone
            return self.__tela_gerente.print_opcao('DADOS ALTERADOS COM SUCESSO!')
        return self.__tela_gerente.print_opcao('NÃO EXISTE UM GERENTE CADASTRADO!')
        # return self.__tela_gerente.print_opcao('ACESSO NEGADO!')

    def mostrar_dados(self):
        # cpf = int(input('Confirme o CPF do gerente para prosseguir: '))
        if self.__gerente_atual is None:
            return self.__tela_gerente.print_opcao('SEM GERENTE CADASTRADO!')
        # cpf = self.__tela_gerente.input_opcao(
            # 'Confirme o CPF do gerente para prosseguir: ')
        # if self.__gerente_atual.acesso_administrativo(cpf):
        dados = [f'Nome: {self.__gerente_atual.nome}',
                 f'Idade: {self.__gerente_atual.idade}',
                 f'CPF: {self.__gerente_atual.cpf}',
                 f'Endereco: {self.__gerente_atual.endereco}',
                 f'Telefone: {self.__gerente_atual.telefone}']
        return self.__tela_gerente.print_opcao('\n'.join(dados))
        # return self.__tela_gerente.print_opcao('ACESSO NEGADO!')

    def gera_relatorio_pedidos(self):
        # cpf = self.__tela_gerente.input_opcao(
        #     'Confirme o CPF do gerente para prosseguir: ')
        # if self.__gerente_atual.acesso_administrativo(cpf):
        clientes = self.__controlador_sistema.controlador_cliente.clientes
        valor = 0
        for cliente in clientes:
            for pedido in cliente.pedidos:
                self.__gerente_atual.relatorio_pedidos.append({
                    "Cliente: ": pedido.cliente,
                    "Data :": pedido.data,
                    "Valor :": pedido.valor
                })
                valor += pedido.valor
        self.__tela_gerente.print_opcao(
            self.__gerente_atual.relatorio_pedidos)
        return self.__tela_gerente.print_opcao(f'Valor total dos pedidos: ${valor}')
        # return self.__tela_gerente.print_opcao('ACESSO NEGADO!')

    def gera_relatorio_ingredientes(self):
        # cpf = self.__tela_gerente.input_opcao(
        #     'Confirme o CPF do gerente para prosseguir: ')
        # if self.__gerente_atual.acesso_administrativo(cpf):
        for ingrediente in self.__controlador_sistema.controlador_armazem.armazem.estoque:
            if ingrediente in self.__gerente_atual.relatorio_ingredientes:
                self.__gerente_atual.relatorio_ingredientes[
                    ingrediente]["Quantidade: "] = ingrediente.quantidade
            else:
                self.__gerente_atual.relatorio_ingredientes[ingrediente] = {
                    "Data de entrada: ": ingrediente.data,
                    "Fornecedor: ": ingrediente.fornecedor.razao_social,
                    "Nome do ingrediente: ": ingrediente.nome_ingrediente,
                    "Quantidade: ": ingrediente.quantidade
                }
        return self.__tela_gerente.print_opcao(self.__gerente_atual.relatorio_ingredientes)
        # return self.__tela_gerente.print_opcao('ACESSO NEGADO!')

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
