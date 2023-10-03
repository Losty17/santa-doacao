def inserir_mock(ongs: dict, tipos: list):
    for i in range(0, 5):
        ongs[f"ONG{i}"] = {
            "endereco": f"Rua {i}",
            "cnpj": "00000000000",
            "email": f"ong{i}@ongs.gov.br",
            "telefone": "51123456789",
            "saldo": 0,
            "estoque": {},
        }

    tipos.append("Calça")
    tipos.append("Camiseta")
    tipos.append("Cueca")
    tipos.append("Sapato")
    tipos.append("Meia")
    tipos.append("Bolacha")
    tipos.append("Arroz")
    tipos.append("Feijão")
    tipos.append("Macarrão")
