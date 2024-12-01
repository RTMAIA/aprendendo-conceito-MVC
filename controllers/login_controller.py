from DAO.contaDAO import DaoConta
from DAO.loginDAO import DaoLogin


class LoginController:

    def login(self, usuario_cpf, senha):

        try:
            self.x = DaoLogin.ler()
            self.y = DaoConta.ler()

            self.filtra_cpf = list(filter(lambda x: x.conta.cpf == str(usuario_cpf), self.x))
            self.filtra_senha = list(filter(lambda x: x.senha == str(senha), self.x))
            self.filtra_cpf_senha = list(filter(lambda x: x.conta.cpf == str(usuario_cpf) or x.senha == str(senha), self.x))

            self.filtra_cpf_conta = list(filter(lambda y: y.cpf == str(usuario_cpf), self.y))



            if not len(self.filtra_cpf_senha) >= 1:
                raise Exception('Conta nao existe!')
            if not len(self.filtra_cpf) >= 1:
                raise Exception('CPF incorreto!')
            if not len(self.filtra_senha) >= 1:
                raise Exception('Senha incorreta!')
            if self.filtra_cpf_conta != 0 and self.filtra_cpf != 0:

                return {'success': True, 'message': 'Login realizado com sucesso'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
