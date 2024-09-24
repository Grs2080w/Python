listagem = ('Pão', 1, 'Manteiga', 10, 'Garrafa', 30, 'Carne', 60, 'Tapioca', 12, 'Biscoito', 6,
            'Pão de Forma', 12, 'Açúcar', 30)

print('_' * 50)
print(f'{'LISTAGEM DE PREÇOS': ^49}')
print('_' * 50)
c = 0
t = 1
while True:
    print(f'{listagem[c]:.<40}R${listagem[t]:.2f}')
    c += 2
    t += 2
    if c == len(listagem):
        break
print('_' * 50)
