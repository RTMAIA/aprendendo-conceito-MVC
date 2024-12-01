from os import system
from controllers.cadastrar_conta_controller import CadastrarContaController


class CadastrarContaView:

    @staticmethod
    def cadastrar_view():
        system('cls||clear')

        print('''
        ------CADASTRAR CONTA------
        \n\n''')

        nome = str(input('Nome: '))

        cpf = str(input('CPF: '))

        conta = CadastrarContaController()
        print(conta.cadastrar(nome, cpf))
