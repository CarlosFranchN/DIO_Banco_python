from banco import Banco
from conta import Conta
from cliente import Cliente

Banco = Banco("CarlosBank", "0001")


def interface(banco: object):
    print(f"Bem vindo ao banco {banco.nome}")
    while True:
        print("\nOpções:")
        print(
            """
            1. Para adicionar uma conta;
            2. Para remover uma conta;
            3. Para consultar uma conta;
            4. Para realizar operações na conta;
            0. Para sair da interface...

        """
        )
        menu1 = int(input("->"))
        print()
        match menu1:
            case 1:
                nome = input("Digite aqui o nome do Titular: ")
                data_nascimento = input("Digite sua data de nascimento: ")
                cpf = input("Digite seu cpf: ")
                logradouro = input(
                    "Digite seu logradouro: num - bairro - cidade/sigla estado: "
                )
                cliente = Cliente(
                    nome=nome,
                    data_nascimento=data_nascimento,
                    cpf=cpf,
                    logradouto=logradouro,
                )
                print()

                print(Banco.add_Conta(cliente))
            case 2:
                filtro = int(input("Digite aqui ou id da conta: "))
                print()
                print(Banco.remove_Conta(filtro))
            case 3:
                nome = input("Digite o nome aqui: ")
                lista_das_contas = Banco.acessar_cliente_nome(nome)
                for conta in lista_das_contas:
                    conta.info()
                    print()

            case 4:
                id = int(input("Digite aqui o id da conta: "))
                conta = Banco.acessar_id(id)
                # print(conta)
                if conta is None:
                    print("Conta não encontrada")
                else:
                    conta.operacao()

            case 0:
                print("Obrigado por usar o nosso banco!")
                break
            case _:
                print("Opção invalida, tente novamente!")


interface(Banco)
