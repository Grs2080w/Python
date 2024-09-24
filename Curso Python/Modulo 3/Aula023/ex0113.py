r = i = v = c = 0
try:
    # Inteiro
    while True:
        try: # Inteiro
            c = 0
            i = int(input('Digite um número inteiro: '))
        except (TypeError, ValueError):
            print('\033[31mERRO! Digite um valor INTEIRO\033[m')
            c += 1
        except KeyboardInterrupt:
            print('\n')
            print('_' * 34)
            print('Usuário preferiu não continuar :(')
            v = 1
            break
        if c == 0:
            break
# Real
    while True:
        try:
            c = 0
            r = float(input('Digite um número real: '))
        except (TypeError, ValueError):
            print('\033[31mERRO! Digite um valor REAL\033[m')
            c += 1
        except KeyboardInterrupt:
            print('\n')
            print('_' * 34)
            print('Usuário preferiu não continuar :(')
            v = 1
            break
        if c == 0:
            break
finally:
    if v == 1:
        print('Volte sempre! Muito obrigado!')
    else:
        print('_' * 50)
        print(f'O valor inteiro digitado foi {i} e o real foi {r}')
        print('_' * 50)
        print('Volte sempre! Muito obrigado!')