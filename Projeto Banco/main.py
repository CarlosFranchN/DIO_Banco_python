from banco import Banco
from conta import Conta

Banco = Banco("CarlosBank")


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
        match menu1:
            case 1:
                nome = input("Digite aqui o nome do Titular: ")
                saldo = float(input("Digite aqui o saldo inicial: "))
                conta = Conta(nome, saldo)
                print(Banco.add_Conta(conta))
            case 2:
                id = int(input("Digite aqui o id da conta: "))
                print(Banco.remove_Conta(id))
            case 3:
                nome = input("Digite o nome aqui: ")
                print(Banco.consultar_nome(nome))

            case 4:
                id = int(input("Digite aqui o id da conta: "))
                conta = Banco.acessar_conta(id)
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
