def cadastrar_doacao_dinheiro(ong, valor, *, ongs={}):
    # Pega a ONG atual e adiciona o valor da doação ao saldo
    ong_atual = ongs[ong]
    ong_atual["saldo"] += valor


def cadastrar_doacao_items(ong, lista_items, *, ongs={}):
    ong_atual = ongs[ong]
    estoque: dict = ong_atual["estoque"]

    # Para cada item na lista de items, verifica se há uma entrada
    # no dicionário, se não houver, inclui uma nova, evitando erro
    # de chave não encontrada
    for item in lista_items:
        if not estoque.get(item, False):
            estoque[item] = 1
        else:
            estoque[item] += 1


def cadastrar_doacao(ongs, tipos):
    ong = input("Qual ONG você deseja doar? ")

    # Verifica se a ONG digitada pelo usuário existe,
    # se não existir, mostra uma mensagem de erro e reinicia o cadastro
    if not ongs.get(ong, False):
        print("A ONG digitada não existe")
        return cadastrar_doacao(ongs, tipos)

    print("Você deseja doar dinheiro ou items?")
    print("1. Dinheiro")
    print("2. Items")
    tipo_doacao = input("-> ")  # Pega a opcão digitada pelo usuário

    if tipo_doacao == "1":
        valor = input("Qual o valor da doação? ")
        valor_int = 0

        # Tenta converter o valor em um inteiro, se não conseguir,
        # mostra uma mensagem de erro e reinicia o cadastro
        try:
            valor_int = int(valor)
        except:
            print("O valor digitado não é um número válido")
            return cadastrar_doacao()

        # Se o valor for menor ou igual a zero, mostra uma mensagem de erro
        # e reinicia o cadastro
        if valor_int <= 0:
            print("O valor digitado não é um número válido")
            return cadastrar_doacao()

        # Por fim, chama a função responsável por modificar o saldo
        cadastrar_doacao_dinheiro(ong, valor_int, ongs=ongs)
    elif tipo_doacao == "2":
        lista_items = []

        # Enquanto o usuário não digitar "sair", pede um item para ele
        while True:
            item = input("Qual item você deseja doar? (digite 'sair' para encerrar) ")

            if item.lower() == "sair":
                break

            # Verifica se o item digitado pelo usuário está na lista de tipos
            if item not in tipos:
                print("Nossas ONGs não aceitam esse item")
                continue

            # Se o item estiver na lista de tipos, adiciona ele na lista de items a serem adicionados
            lista_items.append(item)

        # Por fim, chama a função responsável por modificar o estoque
        cadastrar_doacao_items(ong, lista_items, ongs=ongs)

    # Confirma a doação e mostra o estoque e saldo da ONG
    print("Obrigado por doar para a ONG {}".format(ong))
    print("Estoque da ONG: {}".format(ongs[ong]["estoque"]))
    print("Saldo da ONG: {}".format(ongs[ong]["saldo"]))
