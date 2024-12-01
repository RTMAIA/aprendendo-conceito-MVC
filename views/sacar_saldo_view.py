from controllers.sacar_saldo_controller import SacarSaldoController

class SacarSaldoView:

    @staticmethod
    def sacar_view():
        print('----------SACAR----------')

        numero_da_conta = int(input('Numero da conta: '))
        valor = float(input('Valor: '))
        a = SacarSaldoController()
        print(a.sacar(numero_da_conta, valor))