l1 = int(input('\033[33mDigite quantos cm tem o lado: '))
l2 = int(input('\033[33mDigite mais um lado: '))
l3 = int(input('\033[33mDigite mais um lado:\033[m '))
isosceles = bool(l1 == l2 or l1 == l3 or l2 == l3)
equilatero = bool(l1 == l2 == l3)
escaleno = bool(l1 != l2 != l3)



if l1 + l2 < l3:
    print(' ')
    print('Usando um lado com {}, outro lado com {} e mais um lado com {},\né possível formar um triângulo.'.format(l1, l2, l3))
    if isosceles == True:
        print(' ')
        print('\033[35mO triângulo é isosceles.')
    elif escaleno == True:
        print(' ')
        print('\033[32mO triângulo é escaleno.')
elif l1 + l3 < l2:
    print(' ')
    print('Usando um lado com {}, outro lado com {} e mais um lado com {},\né possível formar um triângulo.'.format(l1, l2, l3))
    if isosceles == True:
        print(' ')
        print('\033[35mO triângulo é isosceles.')
    elif escaleno == True:
        print(' ')
        print('\033[32mO triângulo é escaleno.')
elif l2 + l3 < l1:
    print(' ')
    print('Usando um lado com {}, outro lado com {} e mais um lado com {},\né possível formar um triângulo.'.format(l1, l2, l3))
    if isosceles == True:
        print(' ')
        print('\033[35mO triângulo é isosceles.')
    elif escaleno == True:
        print(' ')
        print('\033[33mO triângulo é escaleno.')
elif l1 == l2 == l3:
    print('\033[36mUsando os três lados iguais a {}, é possível formar um triangulo equilátero!'.format(l1))
else:
    print(' ')
    print('\033[31m\\\\Não é possível formar um triângulo\033[m//')


#if isosceles == True:
#    print('O triângulo é isosceles')
#elif equilatero == True:
#    print('O triângulo é equilátero')
#elif escaleno == True:
   # print('O triângulo é escaleno')

