import os

from DAO.contaDAO import DaoConta
from models.login import Login
from DAO.loginDAO import DaoLogin
from datetime import datetime
from controllers.cadastrar_conta_controller import CadastrarContaController


class CadastrarLoginController:
    def cadastrar_login(self, nome, usuario_cpf, data_nascimento, senha):
        try:
            self.verifica_existencia_arquivo()

            self.data_nascimento = self.converte_datetime(data_nascimento)

            cad = CadastrarContaController()

            conta = cad.cadastrar(nome, str(usuario_cpf), self.data_nascimento, salvar=False)
            login = Login(conta, senha)
            if self.valida_existencia(login):
                if self.valida_dados(login):
                    DaoConta.salvar(conta)
                    login.conta.data_nascimento = login.conta.data_nascimento.strftime('%d/%m/%Y')
                    DaoLogin.salvar(login)
            return {'success': True, 'message': 'Cadastro feito com sucesso!'}

        except Exception as e:
            return {'success': False, 'error': str(e)}

    def converte_datetime(self, data_nascimento):
        try:
            data_nascimento_str = str(data_nascimento)

            if len(data_nascimento_str) != 8:
                raise Exception('Data de nascimento deve ter 8 digitos, no formato DDMMYYYY!')
            data_formatada = datetime.strptime(data_nascimento_str, '%d%m%Y')

            return data_formatada
        except ValueError:
            raise Exception('Formato de data incorreto! A data deve estar em DDMMYYYY!')

    def valida_dados(self, login: Login):

        maioridade = datetime.now().year - login.conta.data_nascimento.year


        if not isinstance(login.conta.nome, str) or not login.conta.nome.isalpha():
            raise Exception('O campo nome deve conter apenas letras!')
        if not isinstance(login.conta.data_nascimento, datetime):
            raise Exception('O campo deve ser uma data de nascimento valida!')
        if login.conta.data_nascimento > datetime.now():
            raise Exception('A data de nascimento nao pode estar no futuro!')
        if maioridade < 18:
            raise Exception('O usuario deve ser maior de 18 anos!')
        if len(str(login.conta.cpf)) != 11:
            raise Exception('O campo CPF deve conter apenas numeros e apenas 11 digitos!')
        if not str(login.conta.cpf).isdigit():
            raise Exception('O campo CPF deve conter apenas digitos!')
        if not len(str(login.senha)) >= 8:
            raise Exception('O campo senha deve conter 8 caracteres!')

        return True

    def valida_existencia(self, login: Login):
        x = DaoLogin.ler()
        cpf = list(filter(lambda x: x.conta.cpf == str(login.conta.cpf), x))
        conta = list(filter(lambda x: x.conta.numero_da_conta == str(login.conta.numero_da_conta), x))

        if len(cpf) != 0:
            raise Exception('CPF já cadastrado!')
        if len(conta) != 0:
            raise Exception('Numero da conta já existe!')
        return True

    def verifica_existencia_arquivo(self):
            arquivos = ['login.txt', 'contas.txt']
            for arquivo in arquivos:
                if not os.path.exists(arquivo):
                    with open(arquivo, 'w') as arq:
                        arq.write('')  # Cria o arquivo vazio, se necessário
                        print(f"{arquivo} criado.")
