#Usando o while

from time import sleep

'''import math
num = int(input('Digite um número: '))
r = math.factorial(num)
print('{}! é igual a {}.'.format(num, r))'''


num = int(input('Digite um número: '))
c = num
f = 1
print('Calculando {}!.'.format(num))
sleep(2)

while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f), end='')
