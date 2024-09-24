print('-=' * 35)
lista = [input('Digite a expressão: ')]
print('-=' * 35)
lista_2 = []
t = len(lista[0])

for c in range(0, t):
    lista_2.append(lista[0][c])

num_pare_dir = lista_2.count('(')
num_pare_esqr = lista_2.count(')')

if num_pare_esqr == num_pare_dir:
    print('A expressão é válida!')
else:
    print('Sua expressão está errada!')

print('-=' * 35)

