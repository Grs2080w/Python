tot = 0

num = int(input('Digite um numero: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end= ' ' )
        tot += 1
    else:
        print('\033[m', end=' ')
    print('{}'.format(c), end= ' ')
if tot == 2:
    l = 'Ele é um número primo.'
else:
    l = 'Ele não é primo.'

print(' ')
print('\n', '\033[m=-' * 40)
print('\n\033[mO número {} foi divisível {} vezes. {}'.format(num, tot, l))
