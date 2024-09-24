from random import randint

maior_numero = pera = c = 0
menor_numero = 10000

print('Os valores sorteados foram: ', end='')
for c in range(0, 5):
    n = pera
    pera = (randint(0, 10))
    c += 1
    print(pera, end=' ')
    if pera == 10:
        maior_numero = pera
    elif c == 1 and pera == 0:
        menor_numero = pera
    elif c >= 1 and pera < menor_numero:
        menor_numero = pera
    elif maior_numero < pera:
        maior_numero = pera
    elif pera == 0:
        menor_numero = pera
print('\n')
print(f'O maior valor sorteado foi {maior_numero}, e o menor foi {menor_numero}.')

#===========================================================================================================================================

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
#Daria no mesmo praticamente
print(f'Os valores são: {n}')
print(f'O maior é {max(n)} e o menor é {min(n)}.')