from DAO.loginDAO import DaoLogin
from .buscar_por_nome_controller import BuscarPorNomeController


class MostrarCadastrosController:

    def mostrar_todos_cadastros(self):
        x = DaoLogin.ler()
        for i in x:
            self.dado = BuscarPorNomeController.formartar(i)
            print(self.dado)