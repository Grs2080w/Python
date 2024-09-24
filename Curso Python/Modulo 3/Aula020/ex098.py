def contagem(i, f, p):
    from time import sleep
    print('=-' * 20)

    i = 1
    f = 11
    p = 1

    print('Contagem de 1 até 10 de 1 em 1')
    for c in range(1, 11, 1):
        print(c, end=' ')
        sleep(0.4)

    print('FIM!')

    print('=-' * 20)
    print('Contagem de 10 até 0 de 2 em 2')

    i = 10
    f = 0
    p = 2

    for d in range(10, -1, -2):
        print(d, end=' ')
        sleep(0.40)

    print('FIM!')

    print('=-' * 20)
    print('Agora é sua vez de personalizar a contagem!')

    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))

    if p == 0 and f < 0:
        p = (-1)
    elif p == 0 and f > 0:
        p = 1

    print('=-' * 20)
    print(F'Contagem de {i} até {f} de {p * (-1) if p < 0 else p} em {p * (-1) if p < 0 else p}')

    if i > f:
        f -= 1
    else:
        f += 1
    if i > f and p > 0:
        p = p * -1
    if i < f and p < 0:
        p = p * -1

    for f in range(i, f, p):
        print(f, end=' ')
        sleep(0.20)
    print('Fim!')
    print('=-' * 20)


contagem(4, 5, 8)