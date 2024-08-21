# from conta import Conta


class Banco:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.contas = []

    def add_Conta(self, conta: object):
        id = len(self.contas) + 1

        entrada = {"id": id, "conta": conta}
        self.contas.append(entrada)

        return f"Conta de {conta.nome} registrada com sucesso com o ID = {id}"

    def remove_Conta(self, id):
        filtrado = next((conta for conta in self.contas if conta["id"] == id), None)
        # print(filtrado)
        if filtrado is None:
            return "Conta não encontrada!"
        self.contas.remove(filtrado)
        return f"Conta removida {filtrado['conta'].nome}"

    def consultar_nome(self, nome):
        conta_filtrada = None
        for conta in self.contas:
            if conta["conta"].nome == nome:
                conta_filtrada = conta

        if conta_filtrada is None:
            return "Conta não encontrada..."

        return f"Seu id é : {conta_filtrada['id']}"
    def acessar_conta(self, id):
        conta_filtrada = None
        for conta in self.contas:
            if conta["id"] == id:
                conta_filtrada = conta["conta"]        
        return conta_filtrada
    
    
        


# BB = Banco()

# conta1 = Conta("Carlos Franch", 700)
# conta2 = Conta("Aloy", 1700)
# conta3 = Conta("Caldrim", 2100)


# BB.add_Conta(conta1)
# BB.add_Conta(conta3)
# BB.add_Conta(conta2)

# print(BB.contas)

# print(BB.remove_Conta(10))
# print(BB.contas)
