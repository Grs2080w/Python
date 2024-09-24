valor_casa = float(input('Qual o valor da casa em R$? '))
salario_comprador = float(input('Qual o salário do comprador em R$? '))
anos_emprestimos = int(input('Deseja pagar em quantos anos? '))

meses = anos_emprestimos * 12
#Valor total da casa dividido pelo numero de parcelas
valor_prestacao = valor_casa / (12 * anos_emprestimos)
#Valor máximo da parcela pode ser de até 30% do salario do individuo
valor_prestacao_max = salario_comprador * 0.30

if valor_prestacao > valor_prestacao_max:
    print('\033[7mR${:.2f}\033[m'.format(valor_prestacao))
    print('\033[33mSinto muito, não é possível realizar seu empréstimo no momento!\nPois o valor da parcela excede 30% salário.\033[m')
#Valor das parcelas excede os 30% do salario do individuo
elif valor_prestacao < valor_prestacao_max:
    print('\033[7m----Parabéns, seu empréstimo foi aprovado----\033[m')
    print(' ')
    print('As parcelas serão no valor de \033[7mR${:.2f}\033[m, por um período de \033[7m{}\033[m meses ou \033[7m{}\033[m anos.'.format(valor_prestacao, meses, anos_emprestimos))
