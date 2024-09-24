import math

num = int(input('Digite um angulo:'))

ang = math.radians(num)
sen = math.sin(ang)
cos = math.cos(ang)
tag = math.tan(ang)

print('O seno de {} é {}, \nO cosseno é {}, \nA tangente é {}'.format(num, sen, cos, tag))

