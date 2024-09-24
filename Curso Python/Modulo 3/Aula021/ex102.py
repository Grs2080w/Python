def fatorial(num=1, show=False):
    """
fatorial(n, show=False)
    :param num: Se refere ao número no qual se quer descobrir o fatorial.
    :param show:(Opicional) Se =False (padrão), mostra apenas o valor, se =True, mostra a conta e o resultado.
    :return: Retorna o fatorial ou a conta e o fatorial
    """
    f = 1
    print('_' * 30)
    if show:
        for c in range(num, 0, -1):

            print(f'{c}', end=' x ' if c > 1 else ' = ')
            f *= c
        print(f)
    if not show:
        for c in range(num, 0, -1):
            f *= c
        print(f'{num}! = {f}')


fatorial(7, show=True)
