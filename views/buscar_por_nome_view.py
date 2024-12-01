from os import system
from controllers.buscar_por_nome_controller import BuscarPorNomeController


class BuscarPorNomeView:

    @staticmethod
    def buscar_view():
        system('cls||clear')

        print('''
        ------BUSCAR POR NOME------
        \n\n''')
        nome = str(input('Digite o nome: '))
        buscar = BuscarPorNomeController()
        print(buscar.buscar(nome))
