N = int(input('Digite um numero: '))
razao = int(input('Digite outro numero para saber os 10 primeiros termos dessa PA: '))
print(' ')
print('Os 10 primeiros termos dessa PA são:')
print('=-' * 20)
print(' ')

dez = N + 10 * razao
t = N

while t != dez:
    r = t + razao
    print(t, end='  ')
    t = r
print('\n')
print('=-' * 20)
print(' Processo finalizado!')