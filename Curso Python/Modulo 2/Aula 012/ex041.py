import datetime

ano_nascimento = int(input('Em que ano vc nasceu? '))
data_atual = str(datetime.date.today())
ano_atual = int(data_atual[0:4])
idade = ano_atual - ano_nascimento

print('=-' * 50)

print(' ')
print('Idade :{} '.format(idade))
print(' ')

if idade <= 5:
    print('Você está na categoria MIRIM!')
elif 5 < idade < 14:
    print('Você está na categoria INFANTIL!')
elif 14 < idade < 19:
    print('Você está na categoria JUNIOR!')
elif 19 <= idade <= 20:
    print('Você está na categoria SÊNIOR!')
elif idade > 20:
    print('Você está na categoria MASTER!')