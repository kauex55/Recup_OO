class Banco:
    def __init__(self):
        self.clientes = {}

    def criar_conta(self, cliente):
        self.clientes[cliente.cpf] = cliente
        print(f"Cliente {cliente.nome} cadastrado com sucesso.")

    def sacar(self,conta, valor):
        self.conta = conta
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente.")

    def depositar(self, conta, valor):
        self.conta = conta
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    def transferir(self, origem, destino, valor):
            self.origem = origem
            if self.saldo >= valor:
                self.saldo -= valor
                destino.deposito(valor)
                print(f"Transferência de R${valor:.2f} realizada para {destino.nome}. Novo saldo: R${self.saldo:.2f}")
            else:
                print("Saldo insuficiente para a transferência.")

    def saldo(self,conta):
        self.conta = conta
