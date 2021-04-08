def contar_caracteres(s):
    """Função que conta os caracteres de uma string
    Exemplo:
    >>> contar_caracteres('padilha')
    {'p': 1, 'a': 2, 'd': 1, 'i': 1, 'l': 1, 'h': 1}

    >>> contar_caracteres('banana')
    {'b': 1, 'a': 3, 'n': 2}

    :param s: string a ser contata

    """
    resultado = {}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado


if __name__ == '__main__':
    print(contar_caracteres('padilha'))
    print()
    print(contar_caracteres('banana'))
