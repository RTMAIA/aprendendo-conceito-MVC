from models.conta import Conta
from models.extrato import Extrato
from models.login import Login


class DaoLogin:

    @classmethod
    def salvar(cls, login: Login):

        with open('login.txt', 'a') as arq:
            arq.writelines(str(login.conta.nome) + '|' + str(login.conta.cpf) + '|' + str(login.conta.numero_da_conta)
                           + '|' + str(login.conta.data_nascimento) + '|' + str(login.conta.extrato) + '|' + str(login.conta.saldo) + '|' + str(login.senha))
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('login.txt', 'r') as arq:
            cls.dados = arq.readlines()
        cls.dados = list(map(lambda x: x.replace('\n', ''), cls.dados))
        cls.dados = list(map(lambda x: x.split('|'),cls.dados))
        dado = []
        for i in cls.dados:
            dado.append(Login(Conta(i[0], i[1], i[2], i[3], i[4], i[5]), i[6]))
        return dado
