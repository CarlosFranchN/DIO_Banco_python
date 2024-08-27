from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500,limite_saques = 3):
        super().__init__(numero,cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        
    def sacar(self, valor: float) -> bool:
        numero_saques = len([transacao for transacao in self.historico.historico if transacao["operacao"] == Saque.__name__])
        
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques
        
        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False
    
    @classmethod
    def nova_conta(cls, cliente: object, numero:int)-> object:
        return cls(numero,cliente)