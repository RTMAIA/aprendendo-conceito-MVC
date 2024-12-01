from models.extrato import Extrato
from DAO.extratoDAO import DaoExtrato
from controllers.sacar_saldo_controller import SacarSaldoController
from controllers.depositar_saldo_controller import DepositarSaldoController


class TransferirSaldoController:

    def transferir(self, numero_da_conta, valor, contaDestino):
        try:

            self.a = SacarSaldoController()
            b = DepositarSaldoController()

            self.a.sacar(numero_da_conta, valor, salvar=False)
            b.depositar(contaDestino, valor, salvar=False)

            a = Extrato('Transferencia', valor, b.conta[0].nome, b.conta[0].cpf, b.conta[0].numero_da_conta)
            DaoExtrato.salvar(self.a.conta[0].extrato, a)
            c = Extrato('Transferencia', valor, self.a.conta[0].nome, self.a.conta[0].cpf, self.a.conta[0].numero_da_conta)
            DaoExtrato.salvar(b.conta[0].extrato, c)

            return {'success': True, 'message': 'Transferencia realizada com sucesso!'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
