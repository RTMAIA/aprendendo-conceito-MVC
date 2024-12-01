

class Conta:
    def __init__(self, nome, cpf, numero_da_conta, data_nascimento,extrato, saldo=0) -> None:
        self.nome = nome
        self.cpf = cpf
        self.numero_da_conta = numero_da_conta
        self.data_nascimento = data_nascimento
        self.extrato = extrato
        self.saldo = saldo
