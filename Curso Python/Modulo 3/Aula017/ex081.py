lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    while True:
        sn = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
        if sn == 'N' or sn == 'S':
            break
        else:
            print('Tente Novamente.')
    if sn == 'N':
        break

print('=-' * 40)
print(f'Foram digitados {len(lista)} números.')
print('=-' * 40)
lista.sort(reverse=True)
print(f'A lista em forma decrescente é {lista}.')
print('=-' * 40)
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
print('=-' * 40)