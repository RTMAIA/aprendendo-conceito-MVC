import os

from models.conta import Conta
from DAO.contaDAO import DaoConta
from DAO.extratoDAO import DaoExtrato
from models.extrato import Extrato


class DepositarSaldoController:

    def depositar(self, numero_da_conta, valor, salvar=True):
        try:

            x = DaoConta.ler()

            self.conta = list(filter(lambda x: x.numero_da_conta == str(numero_da_conta), x))

            if not len(self.conta):
                raise Exception('Conta não encontrada!')
            if not valor > 0:
                raise Exception('Valor tem que ser maior que zero!')
            saldo = float(self.conta[0].saldo)
            saldo += valor

            x = list(map(lambda x: Conta(self.conta[0].nome, self.conta[0].cpf, self.conta[0].numero_da_conta,
                                         self.conta[0].data_nascimento, self.conta[0].extrato, saldo) if(x.numero_da_conta == str(numero_da_conta)) else(x), x))

            with open('contas.txt', 'w') as arq:
                for i in x:
                    arq.writelines(
                        i.nome + '|' + str(i.cpf) + '|' + str(i.numero_da_conta) + '|' + str(i.data_nascimento) + '|' + str(i.extrato) + '|' + str(i.saldo))
                    arq.writelines('\n')
                    arq.flush()

            if salvar == True:
                a = Extrato('Deposito', valor, self.conta[0].nome, self.conta[0].cpf, self.conta[0].numero_da_conta)
                DaoExtrato.salvar(self.conta[0].extrato, a)

            return {'success': True, 'message': 'Deposito realizado com sucesso!'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
