import random
from time import sleep
import typing
numero = []


def sorteia():
    print(f'Sorteando 5 valores...', end=' ')
    for c in range(0, 5):
        n = random.randint(0, 10)
        numero.append(n)
        print(n, end=' ')
        sleep(0.25)
    print('PRONTO!')


def soma_par():
    s = 0
    for n in numero:
        if n % 2 == 0:
            s += n
        else:
            s += 0

    print(f'Somando os valores pares de {numero}, temos {s}.')


sorteia()
soma_par()






