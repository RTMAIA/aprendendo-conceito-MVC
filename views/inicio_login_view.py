from os import system

class InicioLoginView:

    @staticmethod
    def inicio_login_view():
        system('cls||clear')

        print('''
        ----------MENU----------
        1 - DEPOSITAR
        2 - TRANSFERIR
        3 - SACAR
        4 - EXTRATO
        0 - SAIR
        ''')


