from models.extrato import Extrato

class DaoExtrato:



    @classmethod
    def salvar(cls,nome_arquivo, extrato: Extrato):

        with open(nome_arquivo, 'a') as arq:
            arq.writelines(extrato.tipo_de_transacao + '|' + str(extrato.valor) + '|' + extrato.nome_destino + '|' + str(extrato.cpf_destino) + '|' +
                           str(extrato.conta_destino) + '|' + str(extrato.data))
            arq.writelines('\n')

    @classmethod
    def ler(cls, nome_extrato):
        with open(nome_extrato, 'r') as arq:
            cls.extrato = arq.readlines()
        cls.extrato = list(map(lambda x: x.replace('\n', ''), cls.extrato))
        cls.extrato = list(map(lambda x: x.split('|'), cls.extrato))
        extr = []
        for i in cls.extrato:
            extr.append(Extrato(i[0], i[1], i[2], i[3], i[4]))
        return extr
