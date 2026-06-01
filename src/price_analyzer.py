from median_of_medians import selecionar_k_esimo


def calcular_mediana(precos):
    n = len(precos)

    if n == 0:
        raise ValueError("A lista de preços está vazia.")

    indice_mediana = (n - 1) // 2

    return selecionar_k_esimo(precos, indice_mediana)


def analisar_preco(precos, preco_analisado):
    mediana = calcular_mediana(precos)

    diferenca = preco_analisado - mediana
    percentual = (diferenca / mediana) * 100 if mediana != 0 else 0

    if preco_analisado < mediana * 0.85:
        classificacao = "Barato"
    elif preco_analisado > mediana * 1.15:
        classificacao = "Caro"
    else:
        classificacao = "Dentro da faixa esperada"

    return {
        "mediana": mediana,
        "diferenca": diferenca,
        "percentual": percentual,
        "classificacao": classificacao,
    }


def limpar_precos(texto):
    valores = []

    partes = texto.replace("\n", ",").split(",")

    for parte in partes:
        parte = parte.strip().replace("R$", "").replace(" ", "")

        if not parte:
            continue

        parte = parte.replace(".", "").replace(",", ".")

        try:
            valores.append(float(parte))
        except ValueError:
            raise ValueError(f"Valor inválido: {parte}")

    return valores
