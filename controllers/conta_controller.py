from random import randint


class ContaController:

    def gerar_conta(self):
        conta = ''
        for i in range(1, 7):
            self.numeros_da_conta = randint(1, 9)
            conta += str(self.numeros_da_conta)
        return conta
