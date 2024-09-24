lista = []
while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Valor duplicado, não vou adicionar...')
    else:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    while True:
        sn = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if sn == 'N' or sn == 'S':
            break
        if sn != 'S':
            print('Tente novamente.')
    if sn == 'N':
        break

lista.sort()
print('=-' * 30)
print(f'Você digitou os valores {lista}.')
print('=-' * 30)