from log import GerarLog
from trasacoes_mixin import TransacoesMixin
from conta_iterador import ContaIterador
from datetime import datetime



class Conta_corrente(TransacoesMixin):
    def __init__(self, titular, nro_conta, senha):
        super().__init__()
        self.titular = titular
        self.nro_conta = nro_conta
        self._saldo = 0
        self.__senha = senha

    
    @classmethod
    @GerarLog()
    def criar_conta(cls):
        """Método construtor alternativo para criar uma conta"""
        titular = input("Digite o nome do titular: ")
        numero_conta = input("Digite o número da conta: ")
        senha = input("Crie uma senha para a conta: ")
        return cls(titular, numero_conta, senha)


    @GerarLog()
    def _mostrar_saldo(self, senha):
        if senha != self.__senha:
            print("Senha incorreta! Não foi possível realizar o saque.")
            return
        self.registrar_transacoes("Consulta saldo", self._saldo)
        print(self._saldo)    

    @GerarLog()
    def depositar(self, valor):
        if valor is not None and valor > 0:
            self.registrar_transacoes("Deposito", valor)
            self._saldo += valor
            print(f"\nDepósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("\nValor inválido para depósito.\n")

    @GerarLog()    
    def sacar(self, valor, senha):
        if senha != self.__senha:
            print("Senha incorreta! Não foi possível realizar o saque.")
            return
        
        if self._saldo >= valor:
            self._saldo -= valor
            self.registrar_transacoes("Saque", valor)
            print(f"\nSaque de R${valor:.2f} realizado com sucesso!")
        else:
            print("\nSaldo insuficiente ou valor inválido.")


    def transacoes_hoje(self):
        hoje = datetime.now().date()
        trasacoes_hoje = [t for t in self.transacoes if str(hoje) in t]
        return len(trasacoes_hoje)
        
    def limite_transacoes(self, tipo, limite = 3):
        if self.transacoes_hoje() >= limite:
            print("Você excedeu o limite diário de 10 transações.")
            return False
        return True