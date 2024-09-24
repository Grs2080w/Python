lista = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    while True:
        sn = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
        if sn == 'N' or sn == 'S':
            break
        else:
            print('Tente novamente.')
    if sn == 'N':
        break
print('=-' * 35)
print(f'Os números digitados foram: {lista}.')
print('=-' * 35)
print(f'Os números pares digitados foram; {par}.')
print('=-' * 35)
print(f'Os números ímpares digitados foram: {impar}')
print('=-' * 35)