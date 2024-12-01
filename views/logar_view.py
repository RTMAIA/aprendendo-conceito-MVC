from os import system
from controllers.login_controller import LoginController



class LogarView:

        @classmethod
        def logar_view(cls):
            system('cls||clear')

            print('''
                    ----------LOGIN----------
                    ''')
            usuario_cpf = str(input('CPF: '))

            senha = str(input('Senha: '))

            login = LoginController()

            print(login.login(usuario_cpf, senha))

            return login.login(usuario_cpf, senha), login.filtra_cpf_conta

