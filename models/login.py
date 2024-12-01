from models.conta import Conta


class Login:
    def __init__(self,conta: Conta, senha):
        self.conta = conta
        self.senha = senha

