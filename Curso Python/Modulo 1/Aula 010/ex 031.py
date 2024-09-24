d = int(input('Qual a distancia em Km?'))
if d <= 200:
    print('Sua passagem custará R${}.'.format(d * 0.5))
else:
    print('Sua passagem custará R${}.'.format(d * 0.45))