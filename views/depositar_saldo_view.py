import os

from controllers.depositar_saldo_controller import DepositarSaldoController

class DepositarSaldoView:

    @staticmethod
    def depositar_view():
        print('----------DEPOSITAR----------')

        numero_da_conta = int(input('Numero da conta: '))
        valor = float(input('Valor: '))
        a = DepositarSaldoController()
        print(a.depositar(numero_da_conta, valor))

