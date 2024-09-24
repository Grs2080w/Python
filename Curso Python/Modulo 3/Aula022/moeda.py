def metade(n, f=False):
    if f:
        return f'R${n / 2:.2f}'.replace('.', ',')
    if not f:
        return f'{n / 2:.2f}'



def dobro(n, f=False):
    if f:
        return f'R${n * 2:.2f}'.replace('.', ',')
    if not f:
        return f'{n * 2:.2f}'



def aumentando(n, t,  f=False):
    if f:
        return f'R${f'{n + (n * (t/100)):.2f}'}'.replace('.', ',')
    if not f:
        return f'{n + (n * (t/100)):.2f}'



def diminuindo(n, t, f=False):
    if f:
        return f'R${n - (n * (t/100)):.2f}'.replace('.', ',')
    if not f:
        return f'{n - (n * (t/100)):.2f}'



def moeda(n):
    return f'R${n}'.replace('.', ',')


def resumo(p=0, a=0, d=0):
    print('_' * 30)
    print(f'{'RESUMO DO VALOR':^30}')
    print('_' * 30)
    print(f'{'Preço Analisado.':.<20}', f'{moeda(p):>5}')
    print(f'{'Dobro do Preço.':.<20}', f'{dobro(p, f=True):>5}')
    print(f'{'Metade do Preço.':.<20}', f'{metade(p, f=True):>5}')
    print(f'{f"{a}% de Aumento":.<20}', f'{aumentando(p, a, f=True):>5}')
    print(f'{f"{d}% de Redução":.<20}', f'{diminuindo(p, d, f=True):>5}')
    print('_' * 30)
