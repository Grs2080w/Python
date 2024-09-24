lista = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0:
        lista.append(num)
        print('Adicionado ao final da lista...')
    elif c == 1 and num < lista[0]:
        lista.insert(0, num)
        print('Adicionado na posição 0 da lista...')
    elif c == 1 and num > 0:
        lista.append(num)
        print('Adicionado ao final da lista...')
    elif c == 2 and lista[0] < num < lista[1]:
        lista.insert(1, num)
        print('Valor adicionado na posição 1...')
    elif c == 2 and num < lista[0]:
        lista.insert(0, num)
        print('Valor adicionado a posição 0...')
    elif c == 2 and num > lista[1]:
        lista.append(num)
        print('Adicionado ao final da lista...')
    elif c == 3 and num < lista[0]:
        lista.insert(0, num)
        print('Valor adicionado a posição 0...')
    elif c == 3 and num > lista[2]:
        lista.append(num)
        print('Adicionado ao final da lista...')
    elif c == 3 and lista[2] > num > lista[1]:
        lista.insert(2, num)
        print('Valor adicionado a posição 2...')
    elif c == 3 and lista[2] > num > lista[1]:
        lista.insert(1, num)
        print('Valor adicionado a posição 1...')
    elif c == 3 and lista[1] > num > lista[0]:
        lista.insert(1, num)
        print('Valor adicionado a posição 1...')
    elif c == 4 and num > lista[3]:
        lista.append(num)
        print('Adicionado ao final da lista...')
    elif c == 4 and lista[3] > num > lista[2]:
        lista.insert(3, num)
        print('Valor adicionado a posição 3...')
    elif c == 4 and lista[2] > num > lista[1]:
        lista.insert(2, num)
        print('Valor adicionado a posição 1...')
    elif c == 4 and lista[1] > num > lista[0]:
        lista.insert(1, num)
        print('Valor adicionado a posição 1...')
    elif c == 4 and num < lista[0]:
        lista.insert(0, num)
        print('Valor adicionado a posição 0...')
print('=-' * 30)
print(f'Os valores em ordem foram: {lista}.')
print('=-' * 30)
