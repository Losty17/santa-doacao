def cadastrar_ong(ongs):
    # Solicitar dados ao usuário
    nome = input("Digite o nome da ong: ")
    endereco = input("Digite o endereço da ong: ")
    cnpj = input("Digite o CNPJ da ong: ")
    email = input("Digite o email da ong: ")
    telefone = input("Digite o telefone da Ong: ")

    # Criar dicionário com os dados da ong
    nova_ong = {
        "endereco": endereco,
        "cnpj": cnpj,
        "email": email,
        "telefone": telefone,
        "saldo": 0,
        "estoque": {},
    }

    # Inserir o novo dicionario no dicionario que armazena as ongs
    ongs[nome] = nova_ong
