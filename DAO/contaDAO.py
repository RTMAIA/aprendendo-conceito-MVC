import os

from models.conta import Conta



class DaoConta:
    @classmethod
    def salvar(cls, conta: Conta):
        with open('contas.txt', 'a') as arq:
            arq.writelines(str(conta.nome) + '|' + str(conta.cpf) + '|' + str(conta.numero_da_conta) + '|' + str(conta.data_nascimento) + '|' + str(conta.extrato) + '|' + str(conta.saldo))
            arq.writelines('\n')


    @classmethod
    def ler(cls):
        with open('contas.txt', 'r') as arq:
            cls.conta = arq.readlines()
        cls.conta = list(map(lambda x: x.replace('\n', ''),cls.conta))
        cls.conta = list(map(lambda x: x.split('|'), cls.conta))
        cont = []
        for i in cls.conta:
            cont.append(Conta(i[0], i[1], i[2], i[3], i[4], i[5]))
        return cont
