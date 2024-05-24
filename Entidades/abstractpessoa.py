from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, idade: int, cpf: str, endereco: str, telefone: str):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__endereco = endereco
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def cpf(self):
        return self.__cpf

    @property
    def endereco(self):
        return self.__endereco

    @property
    def telefone(self):
        return self.__telefone

    @nome.setter
    def nome(self, nome: str):
        if type(nome) == str:
            self.__nome = nome
            return 'Nome alterado com sucesso'
        return 'Digite um texto válido para nome'

    @idade.setter
    def idade(self, idade: int):
        if type(idade) == int:
            self.__idade = idade
            return 'Idade alterado com sucesso'
        return 'Digite um número válido para idade'

    @cpf.setter
    def cpf(self, cpf: str):
        if type(cpf) == str:
            self.__cpf = cpf
            return 'Cpf alterado com sucesso'
        return 'Digite um número válido para cpf'

    @endereco.setter
    def endereco(self, endereco: str):
        if type(endereco) == str:
            self.__endereco = endereco
            return 'Endereco alterado com sucesso'
        return 'Digite um texto válido para endereco'

    @telefone.setter
    def telefone(self, telefone: str):
        if type(telefone) == str:
            self.__telefone = telefone
            return 'Telefone alterado com sucesso'
        return 'Digite um número válido para telefone'
