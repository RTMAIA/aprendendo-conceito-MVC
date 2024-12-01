import os.path
from os import system
from views.logar_view import LogarView
from views.cadastrar_login_view import CadastrarLoginView
from views.inicio_view import InicioView
from views.buscar_por_nome_view import BuscarPorNomeView
from views.mostrar_cadastros_view import MostrarTodosOsCadastros
from views.inicio_login_view import InicioLoginView
from views.depositar_saldo_view import DepositarSaldoView
from views.sacar_saldo_view import SacarSaldoView
from views.transferir_saldo_view import TransferirSaldoView
from views.extrato_view import ExtratoView


if __name__ == '__main__':
    while True:
        InicioView.pagina_inicial()
        opc = int(input('>>'))
        if opc == 1:
            CadastrarLoginView.cadastrar_login_view()
        if opc == 2:
            BuscarPorNomeView.buscar_view()
        if opc == 3:
            MostrarTodosOsCadastros.mostrar_cadastros_view()
        if opc == 4:
            valida = LogarView.logar_view()
            if valida[0]['success']:
                while valida[0].get('success', False):
                    InicioLoginView.inicio_login_view()
                    opc = int(input('>>'))
                    if opc == 1:
                        DepositarSaldoView.depositar_view()
                    if opc == 2:
                        TransferirSaldoView.tranferir_view()
                    if opc == 3:
                        SacarSaldoView.sacar_view()
                    if opc == 4:
                        ExtratoView.extrato_view(valida[1][0].extrato)
                    if opc == 0:
                        break
            continue
        if opc == 0:
            system('cls||clear')
            exit()
