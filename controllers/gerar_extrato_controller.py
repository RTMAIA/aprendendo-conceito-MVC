import os
from DAO.loginDAO import DaoLogin
from DAO.extratoDAO import DaoExtrato
from DAO.contaDAO import DaoConta
from models.extrato import Extrato


class GerarExtratoController:



    @classmethod
    def gerar_extrato(cls, nome_extrato):
        y = DaoExtrato.ler(nome_extrato)
        for i in y:
            print(
                f'''
----------EXTRATO {i.data}----------
        Tp. Transação: {i.tipo_de_transacao}
--------------------------------------------
        Nome Destino: {i.nome_destino}
        CPF Destino: {i.cpf_destino}
        Conta Destino: {i.conta_destino}
--------------------------------------------
        Valor: {i.valor},
--------------------------------------------
        ''')


    @classmethod
    def verifica_arquivo(cls):
        x = DaoConta.ler()
        extr = os.listdir()
        extr = list(filter(lambda nome: nome.startswith('extrato'), extr))
        if len(extr) > 0 :
            for i in extr:
                for j in x:
                    if i == j.extrato:
                        extrato = str(int(i[9:10]) + 1)
                        extrato = i[0:9] + extrato + i[10:14]
                    return extrato
        return 'extrato_00.txt'

