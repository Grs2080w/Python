l1 = int(input('Digite quantos cm tem o lado: '))
l2 = int(input('Digite mais um lado: '))
l3 = int(input('Digite mais um lado: '))

if l1 + l2 < l3:
    print(' ')
    print('Usando um lado com {}, outro lado com {} e mais um lado com {},\né possível formar um triângulo.'.format(l1, l2, l3))
elif l1 + l3 < l2:
    print(' ')
    print('Usando um lado com {}, outro lado com {} e mais um lado com {},\né possível formar um triângulo.'.format(l1, l2, l3))
elif l2 + l3 < l1:
    print(' ')
    print('Usando um lado com {}, outro lado com {} e mais um lado com {},\né possível formar um triângulo.'.format(l1, l2, l3))
else:
    print(' ')
    print('\\\\Não é possível formar um triângulo//')



