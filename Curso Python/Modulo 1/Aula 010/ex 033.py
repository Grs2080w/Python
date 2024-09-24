n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
print(' ')
print('Os numeros digitados foram {}, {} e {}'.format(n1, n2, n3))
print(' ')


if n1 > n2 > n3:
    print('O maior é {} e o menor é {}.'.format(n1, n3))
elif n2 > n3 > n1:
    print('O maior é {} e o menor é {}.'.format(n2, n1))
elif n3 > n2 > n1:
    print('O maior numero é {} e o menor é {}.'.format(n3, n1))
elif n1 > n3 > n2:
    print('O maior numero é {} e o menor é {}.'.format(n1, n2))
elif n3 > n1 > n2:
    print('O maior numero é {} e o menor é {}.'.format(n3, n2))
elif n2 > n1 > n3:
    print('O maior numero é {} e o menor é {}.'.format(n2, n3))