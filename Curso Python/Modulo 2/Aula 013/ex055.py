maior = 0
menor = 0

for c in range(1, 6):
    p = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = p
    elif p > maior:
        menor = p
        maior = p
    elif p < menor:
        menor = p

print('O maior peso é {}Kg, e o menor é {}Kg.'.format(maior, menor))

#Logica diferente, gostei
