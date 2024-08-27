from historico import Historico

class Conta:
    def __init__(self,numero: int,cliente: object) -> None:
        self.saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()
    @property
    def saldoTotal(self)->float:
        return self.saldo
    
    
    def depositar(self,valor:float)->bool:
        if valor> 0:
            self.saldo += valor
            return True
        return False
    
    
    def sacar(self,valor:float)->bool:
        saldo = self.saldo
        if valor <= saldo:
            self.saldo -= valor
            # self.historico.registrar("Saque",valor)
            return True
        return False
    
    @classmethod
    def nova_conta(cls, cliente: object, numero:int)-> object:
        return cls(numero,cliente)