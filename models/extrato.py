from datetime import datetime

class Extrato:
    def __init__(self, tipo_de_transacao='', valor='',
                 nome_destino='', cpf_destino='', conta_destino=''):

        data_atual = datetime.today()
        data_atual = data_atual.strftime('%d/%m/%Y %H:%M')

        self.tipo_de_transacao = tipo_de_transacao
        self.valor = valor
        self.nome_destino = nome_destino
        self.cpf_destino = cpf_destino
        self.conta_destino = conta_destino
        self.data = data_atual
