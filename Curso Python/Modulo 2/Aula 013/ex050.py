s = 0

for n in range(1, 7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        s += num
print('A soma dos números pares é de {}.'.format(s))
