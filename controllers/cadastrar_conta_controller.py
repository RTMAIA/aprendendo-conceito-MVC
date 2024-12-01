from DAO.contaDAO import DaoConta
from models.conta import Conta
from controllers.conta_controller import ContaController
from controllers.gerar_extrato_controller import GerarExtratoController


class CadastrarContaController:

    def cadastrar(self, nome, cpf, data_nascimento, salvar=True):
        try:
            self.numero_da_conta = ContaController()
            self.nome_extrato = GerarExtratoController.verifica_arquivo()
            dados = Conta(nome, cpf, self.numero_da_conta.gerar_conta(), data_nascimento, self.nome_extrato)
            if self.valida_dados(dados):
                if self.valida_existencia_da_conta(dados):
                    if salvar:
                        DaoConta.salvar(dados)
                    return dados
        except Exception as e:
            return {'success': False, 'error': str(e)}

    @staticmethod
    def valida_dados(dados: Conta):

        if not isinstance(dados.nome, str):
            raise Exception('O campo nome esta incorreto! Digite apenas letras!')
        if len(str(dados.cpf)) != 11 or not dados.cpf.isdigit():
            raise Exception('O campo CPF está incorreto! Deve conter apenas 11 digitos!')
        if len(str(dados.numero_da_conta)) != 6:
            raise Exception('O campo Numero Da Conta está incorrento! Deve contar apenas 6 digitos!')
        if not isinstance(dados.saldo, (int, float)):
            raise Exception('O campo deve ser apenas numeros!')

        return True

    @staticmethod
    def valida_existencia_da_conta(dados: Conta):
        x = DaoConta.ler()
        dados_conta = list(filter(lambda x: x.numero_da_conta == str(dados.numero_da_conta), x))

        if not len(dados_conta) == 0:
            raise Exception('conta ja cadastrada!')

        return True