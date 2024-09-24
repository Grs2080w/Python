jogador = dict()
jogador['Nome'] = str(input('Qual o nome do Jogador? '))
jogador['Partidas'] = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
print('=-' * 20)
jogador['Gols'] = []
total = 0
for c in range(1, jogador['Partidas'] + 1):
    gp = int(input(f'Quantos gols na partida {c}? '))
    jogador['Gols'] += [gp]
    total += gp
print('=-' * 20)
print(f'O nome do jogador é igual a {jogador['Nome']}.')
print(f'O total de gols feitos foi de {total}.')
print('=-' * 20)
print(f'{jogador['Nome']} jogou um total de {jogador['Partidas']} partidas.')
print('')

for c in range(0, jogador['Partidas']):
    print('{:^36}'.format(f'=> Na partida {c + 1} ele fez {jogador['Gols'][c]} gols.'))
print('')
print(f'Foi um total de {total} gols. Mas o maior gol dele foi ter conquistado a garota mais linda do mundo, você.')