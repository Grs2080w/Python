from random import randint           # Teria 30 linhas sem os enfeites e os enters.
from time import sleep

print('=-' * 15)
print('{:^30}'.format('VAMOS COMEÇAR!'))
print('=-' * 15)
sleep(1)
print('{:^30}'.format('JOGANDO DADOS...'))
print('=-' * 15)
sleep(1)
print('{:^30}'.format('<< VALORES SORTEADOS >>'))
print('')

dados = {}
ranking = []

for c in range(1, 5):
    dados[c] = int(randint(0,  6))  # Escolhe os valores de cada jogador

for k, v in dados.items():
    print('{:^30}'.format(f'Jogador {k} tirou {v}'))
    ranking.append(v)
    sleep(0.5)       # Mostra quanto cada jogador tirou
print('')
print('=-' * 15)
print('')

ranking.sort() # Coloca a lista em ordem

t = y = u = i = b = x = v = 0
print('{:^30}'.format('<<< PÓDIO >>>'))
print('')
for c in range(1, 5): # Primeiro lugar
    if t == 0 and dados[c] == ranking[3]:
        print('{:^30}'.format(f'1º lugar ficou jogador {c}'))
        t += 1 # Impede que continue se um número ja foi escolhido
        b += c # Grava o valor escolhido para usar depois
        sleep(0.5)
for c in range(1, 5): # Segundo lugar
    if c != b and t == 1 and y == 0 and dados[c] == ranking[2]:
        print('{:^30}'.format(f'2º lugar ficou jogador {c}'))
        y += 1 # Impede que continue se um número ja foi escolhido
        x += c # Grava o valor escolhido para usar depois
        sleep(0.5)
for c in range(1, 5): # Terceiro lugar
    if x != c and b != c and u == 0 and dados[c] == ranking[1]:
        print('{:^30}'.format(f'3º lugar ficou jogador {c}'))
        u += 1 # Impede que continue se um número ja foi escolhido
        v += c # Grava o valor escolhido para usar depois
        sleep(0.5)
for c in range(1, 5): # Quarto lugar
    if b != c and x != c and v != c and dados[c] == ranking[0]:
        print('{:^30}'.format(f'4º lugar ficou jogador {c}'))
print('')
print('=-' * 15)
print('')
print('{:^30}'.format(f'PROGRAMA FINALIZADO.'))
print('{:^30}'.format(F'PARABÉNS AO JOGADOR {b}!'))