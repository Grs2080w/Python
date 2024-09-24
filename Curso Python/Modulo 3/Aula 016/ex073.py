nome_campeonatos = 'Botafogo', 'Fortaleza', 'Flamengo', 'Palmeiras', 'São Paulo', 'Cruzeiro', 'Bahia', 'Athletico-PR', 'Atlético-MG', 'Vasco', 'Bragantino', 'Juventude', 'Grêmio', 'Criciúma', 'Internacional', 'Vitória', 'Corinthians', 'Fluminense', 'Cuiabá', 'Atlético-GO'''
print(len(nome_campeonatos))
print('Os 5 primeiros colocados no Campeonato são:')
for cont in range(1, 5):
    print(f'{cont}º', nome_campeonatos[cont])
print(' ')

print('Os 4 últimos times do Campeonato são:')
for c in range(16, 20):
    print(f'{c + 1}º', nome_campeonatos[c])
print(' ')

toa = sorted(nome_campeonatos)
print(f'Os times em ordem alfabetica fica: {toa}')
print(' ')

ncc = nome_campeonatos.index('Corinthians')
print(f'O Corinthians está na posição {ncc + 1}ª do Campeonato Brasileiro.')
