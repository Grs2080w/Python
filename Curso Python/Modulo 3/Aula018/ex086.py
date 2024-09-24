Matriz = [[], [], []]
for c in range(0, 3):
    for t in range(0, 3):
        n = int(input(f'Digite um número para [{c}, {t}]: '))
        Matriz[c].append(n)
print('')
print('=-' * 10)
print(f'[ {Matriz[0][0]} ][ {Matriz[0][1]} ][ {Matriz[0][2]} ]')
print(f'[ {Matriz[1][0]} ][ {Matriz[1][1]} ][ {Matriz[1][2]} ]')
print(f'[ {Matriz[2][0]} ][ {Matriz[2][1]} ][ {Matriz[2][2]} ]')
print('=-' * 10)