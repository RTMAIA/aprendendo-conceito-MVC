from os import system
from controllers.mostrar_todos_cadastros_controller import MostrarCadastrosController


class MostrarTodosOsCadastros:

    @staticmethod
    def mostrar_cadastros_view():
        system('cls||clear')

        print('''
        ------MOSTRAR TODOS OS CADASTROS------
        \n\n''')

        a = MostrarCadastrosController()
        a.mostrar_todos_cadastros()
