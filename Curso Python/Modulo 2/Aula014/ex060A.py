#Usando o For

import time

num = int(input('Digite um número: '))

t = num
f = 1
print('Calculando Fatorial de {} !.'.format(num))
time.sleep(1)
print('-=' * 40)

for c in range(num, 0, -1):
    print('{}'.format(c), end='')
    print(' = ' if c == 1 else ' x ', end='')
    f *= t
    t -= 1
print('{}'.format(f), end='' '\n')
print('=-' * 40)
