from math import hypot

co = float(input('Quantos centímetros tem o cateto oposto?'))
ca = float(input('Quantos centímetros tem o cateto adjacente?'))
#hip = ((co ** 2) + (ca ** 2)) ** 0.5 forma antiga de fazer
hip = hypot(co, ca)#Aqui é usando a biblioteca math, modulo apenas para calcular hipotenusa.

print('A hipotenusa do triangulo vale {} centímetros'.format(hip))
