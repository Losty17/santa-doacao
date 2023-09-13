# Cadastrar ONG
# Cadastrar Item
# Cadastrar Doacao

ONGS = {
    'APAE': {
        'estoque': {},
        'saldo': 0,
    },
    'Grupo do Bem': {
        'estoque': {},
        'saldo': 0,
    },
    'Rotary': {
        'estoque': {},
        'saldo': 0,
    },
}

ITENS = ['Tênis', 'Meia', 'Calça', 'Camiseta']

def cadastrar_doacao_dinheiro(ong, valor):
    ong_atual = ONGS[ong]
    ong_atual['saldo'] += valor

def cadastrar_doacao_items(ong, lista_items):
    ong_atual = ONGS[ong]
    estoque = ong_atual['estoque']

    for item in lista_items:
        if not estoque[item]:
            estoque[item] = 1
        else:
            estoque[item] += 1

def iniciar_doacao():
    ong = input("Qual ONG você deseja doar? ")

    print("Você deseja doar dinheiro ou items?")
    print("1. Dinheiro")
    print("2. Items")
    tipo_doacao = input("-> ")

    if tipo_doacao == "1":
        valor = input("Qual o valor da doação? ")
        valor_int = 0

        try:
            valor_int = int(valor)
        except:
            print("O valor digitado não é um número válido")
            return iniciar_doacao()
        
        if valor_int <= 0:
            print("O valor digitado não é um número válido")
            return iniciar_doacao()

        cadastrar_doacao_dinheiro(ong, valor_int)
    elif tipo_doacao == "2":
        lista_items = []
        while True:
            item = input("Qual item você deseja doar? ")

            if item.lower() == "sair":
                break

            if item not in ITENS:
                print("Nossas ONGs não aceitam esse item")
                continue

            lista_items.append(item)

        cadastrar_doacao_items(ong, lista_items)

    print("Obrigado por doar para a ONG {}".format(ong))
    print("Estoque da ONG: {}".format(ONGS[ong]['estoque']))
    print("Saldo da ONG: {}".format(ONGS[ong]['saldo']))

