from time import sleep
jogadores = []
jogador = dict()
sg = 0
while True:
    jogador['Nome'] = str(input('Qual o nome do Jogador? ')).capitalize()
    jogador['Partidas'] = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
    print('=-' * 20)
    jogador['Gols'] = []
    for c in range(1, jogador['Partidas'] + 1):
        gp = int(input(f'Quantos gols na partida {c}? '))
        jogador['Gols'] += [gp]
        sg += gp
    jogador['total_de_gols'] = sg
    jogadores.append(jogador.copy())
    jogador.clear()
    sg = 0
    print('=-' * 20)
    sn = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
    print('=-' * 20)
    if sn == 'N':
        break

print('  {:^4}{:^13}{: <40}{:>7}'.format('COD', 'NOME', 'GOLS', 'TOTAL'))
for c in range(0, len(jogadores)):
    print(' {:^5}{:^13}{: <40}{:>7}'.format(f'{c}', f'{jogadores[c]['Nome']}', f'{jogadores[c]['Gols']}', f'{jogadores[c]['total_de_gols']}'))
print('=-' * 20)
print('')

while True:
    na = int(input('Mostrar estatística de qual jogador? (999 para interromper) '))
    print('-' * 30)
    if na == 999:
        break
    if na <= len(jogadores) - 1:
        print(f'Estatística de {jogadores[na]['Nome']} são {jogadores[na]['Partidas']} partidas jogadas e {jogadores[na]['total_de_gols']} gols feitos.')
        print('-' * 30)
    else:
        print(F'ERRO! Não existe jogador com código {na}! TENTE NOVAMENTE.')
        print('-' * 30)

print(' ')
print('=' * 55)
print('FINALIZANDO',end='')
for c in range(0, 6):
    print('.', end='')
    sleep(0.25)
print('')
print('=' * 20)
print('VOLTE SEMPRE >>>')
