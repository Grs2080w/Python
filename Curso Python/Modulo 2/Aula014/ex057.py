sexo = 0
sexo1 = 0
while sexo != 'M':
    sexo = str(input('Qual seu sexo?[M]/[F] ')).upper()
    if sexo == 'F':
        sexo = 'M'
        sexo1 = 'F'
    if sexo != 'M':
        print('Tente novamente')
else:
    if sexo1 == 'F':
        print('Você é Mulher!')
    else:
        print('Você é Homem!')

