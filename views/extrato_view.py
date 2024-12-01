from os import system
from controllers.gerar_extrato_controller import GerarExtratoController



class ExtratoView:

    @staticmethod
    def extrato_view(nome_extrato):
        system('cls||clear')
        print('---------------EXTRATO---------------')
        GerarExtratoController.gerar_extrato(nome_extrato)
