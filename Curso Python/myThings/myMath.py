def fatorial(n):
    """
    Retorna o fatorial de um número.
    :param n: número
    :return:
    """
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


def triplo(n):
    """
    Retorna o triplo de um valor.
    :param n: Valor
    :return:
    """
    return n * 3


def baskara(ca, cb=0, cc=0):
    """
    Retorna os valores X ds fórmula.
    :param ca: coeficiente a
    :param cb: coeficiente b
    :param cc: coeficiente c
    :return: x 'linha' e x '2 linhas'
    """
    delta = cb ** 2 - 4 * ca * cc
    delta2 = delta ** (1 / 2)

    x1 = (-cb + delta2) / 2 * ca
    x2 = (-cb - delta2) / 2 * ca

    return x1, x2


def raizQuad(n):
    """
    Retorna a raiz quadrada.
    :param n:
    :return:
    """
    return n**0.5


def metade(n, f=False):
    """
    Retorna a metade de um valor.
    :param n: Valor
    :param f: se f=False, retorna o valor normal, se f=True, retorna o valor em
    formato de moeda.
    :return:
    """
    if f:
        return f'R${n / 2:.2f}'.replace('.', ',')
    if not f:
        return f'{n / 2:.2f}'



def dobro(n, f=False):
    """
    Retorna o dobro de um valor.
    :param n: Valor
    :param f: se f=False, retorna o valor normal, se f=True, retorna o valor em
    formato de moeda.
    :return:
    """
    if f:
        return f'R${n * 2:.2f}'.replace('.', ',')
    if not f:
        return f'{n * 2:.2f}'



def aumentando(n, t,  f=False):
    """
    Calcula um valor com aumento.
    :param n: Valor inicial
    :param t: taxa de aumento
    :param f: se f=False, retorna o valor normal, se f=True, retorna o valor em
    formato de moeda.
    :return:
    """
    if f:
        return f'R${f'{n + (n * (t/100)):.2f}'}'.replace('.', ',')
    if not f:
        return f'{n + (n * (t/100)):.2f}'



def diminuindo(n, t, f=False):
    """
    Calcula um valor com desconto.
    :param n: Valor inicial
    :param t: taxa de desconto
    :param f: e f=False, retorna o valor normal, se f=True, retorna o valor em
    formato de moeda.
    :return:
    """
    if f:
        return f'R${n - (n * (t/100)):.2f}'.replace('.', ',')
    if not f:
        return f'{n - (n * (t/100)):.2f}'



def moeda(n):
    """
    Retorna o valor em formatação de Moeda(R$)
    :param n:
    :return:
    """
    return f'R${n}'.replace('.', ',')


def resumo(p=0, a=0, d=0):
    """
    Calcula vários valores simultaneamente.
    :param p: Preço
    :param a: Taxa de aumento
    :param d: Taxa de desconto
    :return: Retorna o preço, o dobro do preço, a metade, o aumento com taxa inserida
    e o desconto com a taxa inserida. Não é preciso usar print.
    """
    print('_' * 30)
    print(f'{'RESUMO DO VALOR':^30}')
    print('_' * 30)
    print(f'{'Preço Analisado:':.<20}', f'{moeda(p):>5}')
    print(f'{'Dobro do Preço:':.<20}', f'{dobro(p, f=True):>5}')
    print(f'{'Metade do Preço:':.<20}', f'{metade(p, f=True):>5}')
    print(f'{f"{a}% de Aumento":.<20}', f'{aumentando(p, a, f=True):>5}')
    print(f'{f"{d}% de Redução":.<20}', f'{diminuindo(p, d, f=True):>5}')
    print('_' * 30)


def isNumdecint(p):
    """
Confere se algo digitado é um número, seja inteiro ou com vírgula/ponto.

    :param p: Valor a ser conferido
    :return: Valor, se for inteiro ou float, se não, false.

Não aceita formatações do tipo preço como 1.500,50; nesses casos em que uma vírgula
se repete depois de um ponto ou vice-versa, o código dá erro.
    """
    pr = p.replace(',', '.')
    pre = p.replace('.', '').replace(',', '')
    if pre.isdigit():
        return float(pr)
    else:
        return False
