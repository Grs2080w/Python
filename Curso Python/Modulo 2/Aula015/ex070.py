print('_' * 20)
nomeloja = 'LOJA SUPER BARATÃO'
print(f'{nomeloja}')
print('_' * 20)
s = pcmm = c = 0
menor_preco = 1000000000
nome_menor_preco = 'Qualquer um'
sn = 'Qualquer um'
while True:
    nome = str(input('Digite o nome do produto: '))
    print('=-' * 15)
    preco = float(input('Digite o preço do produto:R$ '))
    print('\033[33m=-\033[m' * 15)
    s += preco
    c += 1
    if preco >= 1000:
        pcmm += 1
    if preco < menor_preco:
        menor_preco = preco
        nome_menor_preco = nome
    while True:
        sn = str(input('Deseja adicionar mais algum produto?[S]/[N] ')).upper()
        if sn == 'N':
            break
        if sn == 'S':
            break
        if sn != 'S':
            print('Tente novamente com umas das opções indicadas.')
        if sn != 'N':
            print('Tente novamente com umas das opções indicadas.')
    if sn == 'N':
        break
    print('\033[33m=-\033[m' * 15)
print('\033[36m=-\033[m' * 15)
print('////PROGRAMA FINALIZADO////')
print('\033[36m=-\033[m' * 15)
print(f'O total gasto na compra é de \033[34mR${s:.2f}\033[m.')
print(f'Dos \033[34m{c}\033[m produtos da compra, \033[34m{pcmm}\033[m produtos custam mais de R$1000.')
print(f'O nome do produto mais barato é \033[34m{nome_menor_preco}\033[m e seu preço é de \033[34mR${menor_preco}\033[m.')
