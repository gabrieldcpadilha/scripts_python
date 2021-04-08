def contar_caracteres(s):
    """Função que CONTA e ORDENA os caracteres de uma string
    Exemplo:
    >>> contar_caracteres('padilha')
    a: 2
    d: 1
    h: 1
    i: 1
    l: 1
    p: 1

    >>> contar_caracteres('banana')
    a: 3
    b: 1
    n: 2

    :param s: string a ser contata

    """
    caracteres_ordenados = sorted(s)
    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')
            caracter_anterior = caracter
            contagem = 1
    print(f'{caracter_anterior}: {contagem}')


if __name__ == '__main__':
    contar_caracteres('padilha')
    print()
    contar_caracteres('banana')
