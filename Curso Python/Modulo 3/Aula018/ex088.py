import random
import time
numer = []
c = 0
print('_' * 40)
print('{:^40}'.format('JOGO DA MEGA SENA'))
print('_' * 40)

nj = int(input('Quantos jogos você quer que eu sorteie? '))
print('_' * 40)
print('')
print('{:^40}'.format('=-=-= < SORTEANDO JOGOS > =-=-='))
for t in range(0, nj):
    for c in range(0, 6):
        n = random.randint(0, 60)
        numer.append(n)
    numer.sort()
    time.sleep(1)
    print(f'    Jogo {t + 1}: {numer}')
    numer.clear()
print('{:^40}'.format('=-=-=-=- < BOA SORTE > =-=-=-=-'))
print('')
print('_' * 40)
print('')
print('Caso algum número tenha se repetido em um jogo,\nsorteie outras opções de jogos.')



