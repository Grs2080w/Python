sn = 'oI'
while sn != 'NAO':
    N = int(input('Digite um numero: '))
    razao = int(input('Digite outro numero: '))
    n2 = int(input('Quantos termos a serem mostrados na PA? '))
    dez = N + n2 * razao
    t = N
    print('=-' * 40)
    print(' ')
    while t != dez:
        r = t + razao
        print('\033[33m', end='')
        print(t, end='  ')
        print('\033[m', end='')

        t = r
    print('\n')
    print(('=-' * 40), end='')
    sn = input('\nVocê quer continuar? ').upper()
    print('=-' * 40)
print(' ')
print('Processo Finalizado!')