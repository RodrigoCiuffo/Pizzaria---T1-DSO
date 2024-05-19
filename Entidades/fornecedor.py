class Fornecedor():
    def __init__(self, razao_social: str, cnpj: int, email: str, telefone: int):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__email = email
        self.__telefone = telefone

    @property
    def razao_social(self):
        return self.__razao_social

    @razao_social.setter
    def razao_social(self, nova_razao):
        self.__razao_social = nova_razao

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, novo_cnpj):
        self.__cnpj = novo_cnpj

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, novo_email):
        self.__email = novo_email

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        self.__telefone = novo_telefone



