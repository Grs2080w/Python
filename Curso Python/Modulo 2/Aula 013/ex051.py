N = int(input('Digite um numero: '))
razao = int(input('Digite outro numero; '))

print('=-' * 50)
print('Os 10 primeiros termos dessa P.A. são: ')
print('=-' * 50)

for c in range(N, 10 * razao, razao):
    print(c, end= ' - ')
print('ACABOU')