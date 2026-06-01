def selecionar_k_esimo(valores, k):
    # Seleção determinística: mediana das medianas (k é zero-indexado)
    if not valores:
        raise ValueError("A lista de valores está vazia.")

    n = len(valores)
    if k < 0 or k >= n:
        raise IndexError("k está fora do intervalo")

    # caso base: lista pequena -- ordenar e pegar
    if n <= 5:
        return sorted(valores)[k]

    # dividir em grupos de 5 e coletar mediana de cada grupo
    medians = []
    for i in range(0, n, 5):
        group = valores[i:i+5]
        medians.append(sorted(group)[len(group)//2])

    # escolher pivot como mediana das medianas recursivamente
    pivot = selecionar_k_esimo(medians, len(medians)//2)

    # particionar em menores, iguais e maiores
    lows = [x for x in valores if x < pivot]
    highs = [x for x in valores if x > pivot]
    pivots = [x for x in valores if x == pivot]

    if k < len(lows):
        return selecionar_k_esimo(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return selecionar_k_esimo(highs, k - len(lows) - len(pivots))
