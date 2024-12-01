from os import system
from controllers.cadastrar_login_controller import CadastrarLoginController

class CadastrarLoginView:

    @staticmethod
    def cadastrar_login_view():
        system('cls||clear')

        print('''
        ----------CRIAR CONTA----------
        ''')
        nome = str(input('Nome: '))

        data_nascimento = str(input('Data de nascimento: '))

        usuario = str(input('Usuario (CPF): '))

        senha = str(input('senha: '))

        login = CadastrarLoginController()
        print(login.cadastrar_login(nome, usuario, data_nascimento, senha))