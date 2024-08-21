from conta import Conta
# from cliente import Cliente


class Banco:
    def __init__(self, nome: str, agencia: str) -> None:
        self.nome = nome
        self.agencia = agencia
        self.contas = []  # Lista de objetos agr

    def acessar_conta(self, filtro):
        conta_filtrada = []

        for conta in self.contas:
            if (
                conta.id == filtro
                or conta.cliente.nome == filtro
                or conta.cliente.cpf == filtro
            ):
                conta_filtrada.append(conta)

        if len(conta_filtrada) == 0:
            return None

        return conta_filtrada

    def acessar_cliente_nome(self, cliente_nome:str) -> list:
        conta_filtrada = []

        for conta in self.contas:
            if conta.cliente.nome == cliente_nome:
                conta_filtrada.append(conta)
        if len(conta_filtrada) == 0:
            return None

        return conta_filtrada

    def acessar_id(self, id:int) -> object: 
        conta_filtrada = None

        for conta in self.contas:
            if conta.id == id:
                conta_filtrada = conta

        return conta_filtrada

    def acessar_cpf(self, cpf:str) -> list:
        conta_filtrada = []

        for conta in self.contas:
            if conta.cliente.cpf == cpf:
                conta_filtrada.append(conta)

        if len(conta_filtrada) == 0:
            return None

        return conta_filtrada

    def add_Conta(self, cliente: object):
        agencia = self.agencia
        id = len(self.contas) + 1

        conta = Conta(agencia=agencia, id=id, cliente=cliente)
        conta.info()

        # entrada = {"id": id, "conta": conta}
        self.contas.append(conta)

        return f"Conta de {conta.cliente.nome} registrada com sucesso com o ID = {conta.id}"

    def remove_Conta(self, id):
        filtrado = self.acessar_id(id)
        # print(filtrado)
        if filtrado is None:
            return "Conta não encontrada!"
        self.contas.remove(filtrado)
        return f"Conta removida {filtrado['conta'].nome}"


# BB = Banco("CarlosBank", "0001")

# user1 = Cliente("Carlos", "12/07/1997", "2120")
# user2 = Cliente("Aloy", "31/10/2000", "2829")
# user3 = Cliente("Caldrim", "21/08/2000", 1545)

# print(BB.add_Conta(user1))
# print(BB.add_Conta(user2))
# print(BB.add_Conta(user3))

# print(BB.contas)

# conta = BB.acessar_id(1)
# conta = BB.acessar_cpf("2829")
# conta = BB.acessar_cliente_nome("Carlos")
# print(conta)

# conta1 = Conta("Carlos Franch", 700)
# conta2 = Conta("Aloy", 1700)
# conta3 = Conta("Caldrim", 2100)


# BB.add_Conta(conta1)
# BB.add_Conta(conta3)
# BB.add_Conta(conta2)

# print(BB.contas)

# print(BB.remove_Conta(10))
# print(BB.contas)
