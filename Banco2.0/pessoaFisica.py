from cliente import Cliente

class PessoaFisica(Cliente):
    def __init__(self, nome: str, cpf: str, data_nascimento: str,endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        