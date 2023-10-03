from pprint import pprint

from cadastrar_ong import cadastrar_ong
from cadastrar_tipos import cadastrar_tipos
from cadastrar_doacao import cadastrar_doacao
from inserir_mock import inserir_mock

ONGS = {}
TIPOS = []


def menu():
    escolha = None

    while True:
        if escolha == -1:
            # espera apertar alguma tecla pra continuar
            input("\nAperte Enter para continuar...")

        print("\n\n")
        print("|=-=-=-=-=-=-=-=-=-=-=-=-=|")
        print("|  1 - Cadastrar ONG      |")
        print("|  2 - Cadastrar Item     |")
        print("|  3 - Cadastrar Doação   |")
        print("|  4 - Listar ONGs        |")
        print("|  5 - Listar Itens       |")
        print("|  6 - Iniciar teste      |")
        print("|  0 - Sair               |")
        print("|=-=-=-=-=-=-=-=-=-=-=-=-=|\n")

        escolha = int(input("Qual opção você deseja acessar? "))

        if escolha == 1:
            cadastrar_ong(ONGS)
        elif escolha == 2:
            cadastrar_tipos(TIPOS)
        elif escolha == 3:
            cadastrar_doacao(ONGS, TIPOS)
        elif escolha == 4:
            pprint(ONGS)
        elif escolha == 5:
            pprint(TIPOS)
        elif escolha == 6:
            inserir_mock(ONGS, TIPOS)
        elif escolha == 0:
            break
        else:
            print("Opção inválida")

        escolha = -1


if __name__ == "__main__":
    menu()
