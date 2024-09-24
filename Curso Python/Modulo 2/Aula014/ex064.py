n = s = c = 0
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um número: '))
print('A quantidade de números digitados foi de {}, e a soma desses números foi de {}.'.format(c - 1, s))