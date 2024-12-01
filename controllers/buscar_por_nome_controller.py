from DAO.loginDAO import DaoLogin
from models.login import Login


class BuscarPorNomeController:
    def buscar(self, nome):
        x = DaoLogin.ler()
        conta = list(filter(lambda x: x.conta.nome == nome, x))
        for i in conta:
            return self.formartar(i)

    @staticmethod
    def formartar(login: Login):

        formatado = f'''
            'Nome': {login.conta.nome}, 
            'CPF': {login.conta.cpf}, 
            'Numero da conta': {login.conta.numero_da_conta}, 
            'Saldo': {float(login.conta.saldo): .2f}, 
            -----------------------------------
'''
        return formatado
