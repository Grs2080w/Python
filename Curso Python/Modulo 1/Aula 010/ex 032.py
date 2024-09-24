ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    print('{} é um ano bixesto'.format(ano))
else:
    print('{} não é um ano bixesto'.format(ano))