class Banco:
    def criar_conta(self, nome, saldo_inicial):
        self.nome = nome
        self.saldo_inicial = saldo_inicial

    def sacar(self,conta, valor):
        self.conta = conta
        self.valor = valor

    def depositar(self, conta, valor):
        self.conta = conta
        self.valor = valor

    def transferir(self, origem, destino, valor):
        self.origem = origem
        self.destino = destino
        self.valor = valor

    def saldo(self,conta):
        self.conta = conta