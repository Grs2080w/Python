sal = int(input('Qual é o seu salario em R$? '))
if sal <= 1250:
    print('Seu salário q era de R${} passa a ser agora de R${}'.format(sal, sal + (sal * 0.15)))
else:
    print('Seu salário que  era de \033[7mR${}\033[m passa a ser agora de \033[7mR${}\033[m'.format(sal, sal + (sal * 0.10)))
