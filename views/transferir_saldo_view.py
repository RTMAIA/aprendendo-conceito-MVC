from controllers.transferir_saldo_controller import TransferirSaldoController


class TransferirSaldoView:

    @staticmethod
    def tranferir_view():
        print('----------TRANSFERIR----------')

        numero_da_conta = int(input('Conta origem: '))
        valor = float(input('Valor: '))
        contaDestino = int(input('Conta destino: '))

        a = TransferirSaldoController()

        print(a.transferir(numero_da_conta , valor, contaDestino))
