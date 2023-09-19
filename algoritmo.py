from classes import *

def main():

    sair = False
    while sair == False:
        try:
            print("---MENU---")
            print("1 - Criar conta")
            print("2 - Sacar")
            print("3 - Depositar")
            print("4 - Transferir")
            print("5 - Ver saldo")
            print("0 - SAIR")


            print("Qual opção deseja?")
            menu = int(input(">> "))

            match menu:
                case 1:
                    nome = input("Digite o nome do cliente: ")
                    cpf = int(input("Digite o CPF do cliente: "))
                    cliente = Banco(nome, cpf)
                    Banco.criar_conta(cliente)
                
                case 2:
                    Banco.conta = input("Digite seu cpf: ")
                    valor = float(input("Digite o valor do saque: "))
                    Banco.saque(valor)
                
                case 3:
                    valor = float(input("Digite o valor do depósito: "))
                    Banco.deposito(valor)

                case 4:
                    Banco.origem = input("Digite seu cpf: ")
                    Banco.destino = input("Digite o destinatário: ")
                    valor = float(input("Digite o valor da transferência: "))     
                    Banco.transferir               

                case 5:
                    Banco.conta = (input("Digite seu cpf: "))
                    print(Banco.saldo)

                case 0:
                    print("SAINDO ...")
                    print("------")
                    sair = True
                
                case _:
                    ("Valor inválido")

        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)
            print("")