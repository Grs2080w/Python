s = 0

for c in range(1, 10000, 2):
    if c % 3 == 0:
        g = c
        s += g
print(' ')
print('A soma dos números impares divisíveis por 3 de 1 a 10.000 é {}.'.format(s))
