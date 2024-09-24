print('=-' * 15)
print('IDADE ------ SEXO')
print('=-' * 15)

ci = ch = cmm20 = 0
while True:
    print('CADASTRE UMA PESSOA')
    print('=-' * 15)
    idade = int(input('Qual sua idade? '))
    print('_' * 15)
    while True:
        sexo = str(input('Qual seu sexo?[M]/[F] ')).upper()
        if sexo == 'M' or sexo == 'F':
            break
    print('_' * 15)
    if idade >= 18:
        ci += 1
    if sexo == 'M' or sexo == 'Masculino' or sexo == 'MASCULINO':
        ch += 1
    if sexo == 'F' or sexo == 'FEMININO' and idade < 20:
        cmm20 += 1
    sn = str(input('Quer continuar?[S]/[N] ')).upper()
    print('¨¨' * 15)
    if sn == 'N':
        break
print(f'O total de pessoas com mais de 18 anos foi de: {ci} pessoas')
print(f'Ao todo temos {ch} homens cadastrados.')
print(f'E temos {cmm20} mulheres com menos de 20 anos.')