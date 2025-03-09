from conta_corrente import Conta_corrente
from conta_iterador import ContaIterador

contas = {}

print("Bem vindo ao Banco Terminal!")


while True:
    print("\n1 - Criar Conta")
    print("2 - Acessar Conta")
    print("3 - Listar Contas")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")


    match opcao:
        case "1":
            conta = Conta_corrente.criar_conta()
            print("\nConta criada com sucesso!")

            if conta.nro_conta in contas:
                print("Essa conta já existe! Tente outro número.")
            else:
                contas[conta.nro_conta] = conta

        case "2":
            num_conta = input("Digite o número da conta: ")
            if num_conta not in contas:
                print("Conta não encontrada.")
            else:
                conta = contas[num_conta]
                while True:

                    print("\n1 - Depositar")
                    print("2 - Sacar")
                    print("3 - Ver Saldo")
                    print("4 - Listar Transacoes")
                    print("5 - Voltar ao Menu Principal")
                    escolha = input("Escolha uma opção: \n")

                    match escolha:
                        case "1":
                            valor = float(input("\nDigite o valor para depósito: "))
                            conta.depositar(valor)
                        case "2":
                            valor = float(input("\nDigite o valor para saque: "))
                            senha = input("Digite sua senha: ")
                            conta.sacar(valor, senha) 
                        case "3": 
                            senha = input("\nDigite sua senha: ")
                            conta._mostrar_saldo(senha)     
                        case "4":
                            conta.listar_transacoes()    
                        case "5":
                            print("\nSaindo da conta...")
                            break     
                        case _:
                            print("\nOpção inválida. Tente novamente.")

        case "3":
            for conta in ContaIterador(contas):
                print(conta)

        case "4":
            print("\nObrigado por usar o Banco Terminal!")
            break
        case _:
            print("\nOpção inválida. Tente novamente..") 
 