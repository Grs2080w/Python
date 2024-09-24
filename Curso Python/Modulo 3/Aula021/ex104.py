
def leia_int():
    while True:
        num = input('Digite um número inteiro: ')
        if num.isnumeric():
            print('_' * 30)
            print(f'O número digitado foi {num}.')
            break
        else:
            print('\033[31mERRO! Digite um número inteiro Válido!\033[m')


leia_int()


