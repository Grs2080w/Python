numeros = []
posmax = []
posmin = []

for c in range(0, 5):
    numeros.append(int(input('Digite um número: ')))

print(' ')
print('=-' * 30)
print(f'Os valores escolhidos foram {numeros}')
print('=-' * 30)

maior_numero = max(numeros)
menor_numero = min(numeros)

print('')

for t in range(0, 5):
    if numeros[t] == maior_numero:
        posmax.append(t+1)

for c in range(0, 5):
    if numeros[c] == menor_numero:
        posmin.append(c+1)

print(f'O maior número é {maior_numero} e está na posição(ões): {posmax}')
print(f'O menor número é {menor_numero} e está na posição(ões): {posmin}')
