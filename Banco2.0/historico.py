import datetime


class Historico:
    def __init__(self):
        self.historico = []
         
    def transacoes(self):
        return self.historico
    def adicionar_transacao(self, transacao: object):
        op = {
            'operacao' : transacao.__class__.__name__,
            'valor': transacao.valor,
            'data': datetime.date.today(),
        }
        self.historico.append(op)
        return "Transação realizada com sucesso"