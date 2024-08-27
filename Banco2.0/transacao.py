from abc import ABC,abstractclassmethod

class Transacao(ABC):
    @property
    def valor(self):
        pass
    
    @classmethod
    def registrar(self,conta):
        pass
    
class Saque(Transacao):
    def __init__(self,valor:float) -> None:
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor

    def registrar(self,conta):
        sucesso = conta.sacar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)
    
class Deposito(Transacao):
    def __init__(self,valor:float) -> None:
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self,conta):
        sucesso = conta.depositar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)