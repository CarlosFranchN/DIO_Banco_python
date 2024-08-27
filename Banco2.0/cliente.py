class Cliente:
    def __init__(self, endereco:str):
        self.endereco = endereco
        self.contas = []
        
    def realizar_transacao(self,conta:object,transacao:object):
        transacao.registrar(conta)
        return "Transação realizada"
        
    
    def adicionar_conta(self,conta:object):
        self.contas.append(conta)
        return "Conta adicionada"