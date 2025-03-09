from datetime import datetime

class TransacoesMixin:
    def __init__(self):
        self.transacoes = []

    def registrar_transacoes(self, tipo, valor):
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transacoes.append(f'{data_hora} - {tipo}: R${valor:.2f}')

    def listar_transacoes(self):
        if not self.transacoes:
            print("Nenhuma transação realizada ainda.")
            return     
        else:
            print("\nPara saque - digite 1")
            print("Para deposito - digite 2")
            escolha = input("\nqual tipo de transação?\n")
            
            match escolha:
                case "1":
                    print("Transacoes de Saque: \n")
                    saque = [t for t in self.transacoes if "Saque" in t]
                    for transacoes in saque:
                        print(transacoes)
                case "2":
                    print("Transacoes de Deposito: \n")
                    deposito = [t for t in self.transacoes if "Deposito" in t]
                    for transacoes in deposito:
                        print(transacoes)
                case _:
                    print("Opção inválida. Tente novamente.")       