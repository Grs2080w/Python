import random
comp = random.randint(0, 10)
num = 11
c = 0
while num != comp:
    num = int(input('Digite um número: '))
    c += 1
    if num == comp:
        print('Parabens você acertou!!')
    else:
        if num < comp:
            print('Mais um pouco... Tente novamente...')
        elif num > comp:
            print('Menos... Tente novamente...')
if c > 1:
    print('Parabéns você acertou! Mas precisou errar {} vezes até acertar.'.format(c - 1))
elif c == 1:
    print('Parabéns, você acertou de primeira!!!')
