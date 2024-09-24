import datetime
ano_atual = int(datetime.date.today().year)
c = 0
d = 0
for n in range(7):
    n1 = int(input('Em que ano você nasceu? '))
    if ano_atual-n1 >= 18:
        c += 1
        print(' ')

    else:
        print(' ')
        d += 1

print('=-' * 50)
print(' ')
print('\033[33m{} pessoas são maiores de 18 anos e {} pessoas são menores de 18 anos.'.format(c, d))


