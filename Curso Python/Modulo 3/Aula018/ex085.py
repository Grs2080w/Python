numeros = [[], []]

for c in range(0, 7):
    n = int(input(f'Digite o {c + 1}º número: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()

print('')
print('=-' * 35)
print(f'Os números pares foram {numeros[0]} e os ímpares foram {numeros[1]}.')
print('=-' * 35)
