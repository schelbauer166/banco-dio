class ContaIterador:
    def __init__(self, contas):
        self.contas = list(contas.values())
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.contas):
            raise StopIteration
        conta = self.contas[self.index]
        self.index += 1

        return f"\nTitular: {conta.titular}, Conta: {conta.nro_conta}"