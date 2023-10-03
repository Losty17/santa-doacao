def cadastrar_tipos(doacoes):
    while True:
        tipo_doacao = input("Digite o tipo de doação (ou digite um número para sair): ")

        # Verifica se o usuário digitou um número para sair

        if tipo_doacao.isdigit():
            break

        # Verifica o comprimento mínimo e máximo

        if len(tipo_doacao) < 3:
            print("Nome de doação muito curto. Deve ter pelo menos 3 caracteres.")
            continue
        elif len(tipo_doacao) > 50:
            print("Nome de doação muito longo. Deve ter no máximo 50 caracteres.")
            continue

        # Verifica letras maiúsculas/minúsculas

        tipo_doacao = (
            tipo_doacao.capitalize()
        )  # Converte a primeira letra para maiúscula

        # Verifica se o nome já foi cadastrado

        if tipo_doacao in doacoes:
            print("Este tipo de doação já foi cadastrado.")
        else:
            doacoes.append(tipo_doacao)
