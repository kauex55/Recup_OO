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
                    pass
                
                case 2:
                    pass
                
                case 3:
                    pass

                case 4:
                    pass

                case 5:
                    pass

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