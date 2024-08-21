class Conta:
    def __init__(self, agencia:str,id : int, cliente: object):
        self.agencia = agencia
        self.id = id
        self.cliente = cliente
        self.saldo = 0 
        self.historico = []
        self.saques_diarios = 3
        self.limite_max = 500

    def info(self):
        print(f"Agencia : {self.agencia}")
        print(f"Numero da conta: {self.id}")
        print(f"Nome usuario: {self.cliente.nome}")
        print(f"Saldo : R$ {self.saldo:.2f}")

    def deposito(self, valor):
        self.saldo += valor
        self.historico.append(tuple((valor, "Deposito")))
        return "Deposito realizado com sucesso!"

    def saque(self, valor):
        if valor > self.saldo:
            return "Saque não realizado, valor insuficiente!"
        if self.saques_diarios == 0:
            return "Você atingiu o limite de saques diários!"

        if valor > self.limite_max:
            return "Saque não realizado, valor excede o limite máximo!"

        self.saldo -= valor
        self.saques_diarios -= 1
        self.historico.append(tuple((valor, "Saque")))
        return "Saque realizado com sucesso!"

    def extrato(self):
        if not self.historico:
            return "Não foram realizadas movimentações"
        for valor, op in self.historico:
            print(f"{op} de R$ {valor:.2f} ")
        self.info()
        
    def operacao(self):
        print(
            """
            1. Para Depositar;
            2. Para Sacar;
            3. Para obter extrato;
            """)
        op = int(input("Qual operação deseja realizar? "))
        match op:
            
            case 1:
                print("Voce escolheu depositar...")
                valor = float(input("Qual valor deseja depositar? "))
                print(self.deposito(valor))
            case 2:
                print("Voce escolheu sacar...")
                valor = float(input("Qual valor deseja sacar? "))
                print(self.saque(valor))
            case 3:
                print("Voce escolheu obter extrato...")
                print(self.extrato())
            case _:
                print("Operação invalida")


