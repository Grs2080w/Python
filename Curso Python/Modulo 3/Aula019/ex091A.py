from random import randint
from time import sleep
import operator

jogadores = {'jogador 1': randint(0, 6),
             'jogador 2': randint(0, 6),
             'jogador 3': randint(0, 6),
             'jogador 4': randint(0, 6)}

print('=-' * 15)
print('{:^30}'.format('VAMOS COMEÇAR!'))
print('=-' * 15)
sleep(1)
print('{:^30}'.format('JOGANDO DADOS...'))
print('=-' * 15)
sleep(1)
print('{:^30}'.format('<< VALORES SORTEADOS >>'))
print('')

ranking = []

for k, v in jogadores.items():
    print('{:^30}'.format(f'{k} tirou {v}'))
    ranking.append(v)
    sleep(0.5)

ranking = sorted(jogadores.items(), key=operator.itemgetter(1), reverse=True)
# Ranking recebe ja de forma organizada, os items de 'jogadores'.
# Dos items de 'jogadores' o critério para a organização é o local 1, ou seja, o valor, dentro de items.
# Se fosse ao invés de 1, 0, o critério seria o valor de jogadores.

''' O 'key' indica de qual valor ele vai se basear para a organização da lista, 
'operator.itemgetter()' retorna um valor dentro do dicionário, que tá dentro da lista, então
se 'operator.itemgetter()' e itemgetter(1), ele vai pegar o segundo valor como referência, ou seja,
o valor do item, se itemgetter(0), ele pega a chave do item e usa como critério pra organização.
Então traduzindo o comando, de cada dicionário dentro da lista, ele vai pegar o segundo bloco, 
ou seja, o valor do dicionário, se fosse, 0, pegaria o primeiro bloco, ou seja, 
a chave a quem o valor é atribuído'''

# O reverse=True é um comando que retorna ao sorted se a ordem é decrescente ou não. Se reverse=True, então é decrescente.
print('')
print('=-' * 15)
print('')
print('{:^30}'.format('<<< PÓDIO >>>'))
print('')

for c in range(0, 4):
    print('{:^30}'.format(f'{c + 1}º lugar ficou {ranking[c][0]}'))
    sleep(0.5)

print('')
print('=-' * 15)
print('')
print('{:^30}'.format(f'PROGRAMA FINALIZADO.'))
print('{:^30}'.format(F'PARABÉNS AO JOGADOR {ranking[0][0]}!'))