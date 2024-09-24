import random
comp = random.randint(0, 10)
num = int(input('Digite um número de 0 a 50:'))

if num == comp:
    print('O número escolhido foi {}'.format(comp))
    print('------Parabéns!------')
else:
    print('O número escolhido foi {}'.format(comp))
    print('\\\\\\Tente de novo//////')