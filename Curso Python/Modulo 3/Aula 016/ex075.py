tupla_num = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

tupla_sec = (int(input('Digite um numero de 0 a 10: ')),
            int(input('Digite um numero de 0 a 10: ')),
            int(input('Digite um numero de 0 a 10: ')),
            int(input('Digite um numero de 0 a 10: ')))

print(' ')
print('=-' * 20)
print(f'Os valores escolhidos foram: {tupla_sec}')
print('=-' * 20)

print('\n')

if tupla_sec.count(9) >= 1: # Ou: If 9 in tupla_sec:
    print(f'Na sequência o número 9 aparece {tupla_sec.count(9)} vez(es).')
else:
    print('Na sequência não tem nenhum 9.')
print(' ')
if tupla_sec.count(3) >= 1: # Ou: If 3 in tupla_sec:
    print(f'O número 3 foi digitado pela primeira vez na posição {tupla_sec.index(3)}.')
else:
    print('O número 3 não apareceu nenhuma vez.')
print(' ')


if tupla_sec[0] % 2 == 0 or tupla_sec[1] % 2 == 0 or tupla_sec[2] % 2 == 0 or tupla_sec[3] % 2 == 0:
    print('Os números pares são: ', end='')
else:
    print('Sem números pares.')

c = 0
while True:
    if tupla_sec[c] % 2 == 0:
        print(tupla_sec[c], end=' ')
    c += 1
    if c == 4:
        break
print(' ')

'''if tupla_sec[0] % 2 == 0:
    print(tupla_sec[0], end=' ')
if tupla_sec[1] % 2 == 0:
    print(tupla_sec[1], end=' ')
if tupla_sec[2] % 2 == 0:
    print(tupla_sec[2], end=' ')
if tupla_sec[3] % 2 == 0:
    print(tupla_sec[3], end=' ')'''
# Para voce lembrar de onde voce veio




