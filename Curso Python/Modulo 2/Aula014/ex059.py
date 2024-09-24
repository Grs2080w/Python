import time

escolha = 0
escolha_vdd = 0
num1 = 0
num2 = 0

while escolha != 5:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))

    print('-=' * 30)

    print('Escolha uma opção:')

    escolha = int(input('''
    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos números
    [5]Sair do programa
    
    Opção: '''))

    #Se escolha for igual a 1, então escolha passa a valer 5 para ele sair programa, e a outra variável ser usada la embaixo.'''
    if escolha == 1:
        escolha = 5
        escolha_vdd = 1

    if escolha == 2:
        escolha = 5
        escolha_vdd = 2

    if escolha == 3:
        escolha = 5
        escolha_vdd = 3

    if escolha == 0 or escolha > 5:
        print('Opção inválida, digite novamente.')

    print('-=' * 30)

else:
    print('Finalizando...')
    time.sleep(2)
    print('-=' * 30)

    if escolha_vdd == 1:
        print('A soma de \033[33m{}\033[m e \033[33m{}\033[m é \033[7m{}\033[m'.format(num1, num2, num1 + num2))

    elif escolha_vdd == 2:
        print('A multiplicação de \033[33m{}\033[m e \033[33m{}\033[m resulta em um produto de \033[7m{}\033[m.'.format(num1, num2, num1 * num2))

    elif escolha_vdd == 3 and num1 > num2:
        print('O maior entre \033[33m{}\033[m e \033[33m{}\033[m é \033[7m{}\033[m.'.format(num1, num2, num1))

    elif escolha_vdd == 3 and num2 > num1:
        print('O maior entre \033[33m{}\033[m e \033[33m{}\033[m é \033[7m{}\033[m.'.format(num1, num2, num2))

    elif escolha == 5:
        print('Você escolheu sair do programa!')


