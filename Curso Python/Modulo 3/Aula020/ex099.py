def maior(*num):
    from time import sleep
    print('=' * 60)
    print('Analisando os valores passados...')
    for n in num:
        print(n, end=' ')
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo. ')
    m = max(num)
    print(f'O maior valor informado é {m}.')


maior(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
maior(3, 6, 9, 12, 15)
maior(2, 4, 6, 8, 10)