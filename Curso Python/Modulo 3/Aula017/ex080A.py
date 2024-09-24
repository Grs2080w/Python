lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    lista.append(n)
lista.sort()
print('=-' * 30)
print(f'Os valores em ordem foram: {lista}.')
print('=-' * 30)