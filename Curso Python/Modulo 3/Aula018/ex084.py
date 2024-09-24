pessoas = []
pessoa = []
pesos = []
nomes = []
while True:
    nome = str(input('Digite seu nome: '))
    peso = int(input('Digite seu peso: '))
    pessoa.append(nome)
    pessoa.append(peso)
    pessoas.append(pessoa[:])
    pessoa.clear()

    while True:
        sn = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
        if sn == 'S' or sn == 'N':
            break
        else:
            print('Tente novamente.')
    if sn == 'N':
        break
if len(pessoas) < 2:
    print(f'{pessoas[0][0]} tem {pessoas[0][1]}Kgs.')
else:
    for c in range(0, len(pessoas)):
        p = pessoas[c][1]
        pesos.append(p)
        n = pessoas[c][0]
        nomes.append(n)
    maior_peso = max(pesos)
    menor_peso = min(pesos)

    print('')
    print(f'Ao todo você cadastrou {len(nomes)} pessoas.')
    print(F'A pessoa com maior peso foi \033[33m{nomes[pesos.index(maior_peso)]}\033[m com \033[33m{maior_peso}Kgs.\033[m')
    print(F'A pessoa com maior peso foi \033[33m{nomes[pesos.index(menor_peso)]}\033[m com \033[33m{menor_peso}Kgs\033[m.')