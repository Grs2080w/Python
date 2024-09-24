grupo = []
pessoa = {}
c = i = 0
while True:
    pessoa['Nome'] = str(input('Qual seu nome? '))
    pessoa['Sexo'] = str(input('Qual seu sexo?[M/F] ')).upper().strip()[0]
    pessoa['Idade'] = int(input('Qual sua idade? '))
    grupo.append(pessoa.copy())
    i += pessoa['Idade']
    c += 1
    pessoa.clear()
    while True:
        sn = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
        if sn == 'S' or sn == 'N':
            break
        else:
            print('Tente novamente.')
    if sn == 'N':
        break

print('=-' * 30)
print(f'Foram cadastradas {c} pessoas.')
print('-' * 40)

media_de_idade = i / c
print(f'A média de idade do grupo é de {media_de_idade:.2f} anos.')
print('-' * 40)

print(f'As mulheres são: ', end='')
for p in grupo:
    if p['Sexo'] == 'F':
        print(p['Nome'], end=' ')
print('\n')
print('-' * 40)

print('{:^40}'.format(f'As pessoas com idade acima da  média são: '))
print('')
for c in range(0, len(grupo)):
    if grupo[c]['Idade'] > media_de_idade:
        print('{:^40}'.format(f'{grupo[c]['Nome']} com {grupo[c]['Idade']} anos.'))
print('')
print('{:^40}'.format('<< ENCERRADO >>'))