import datetime
ano_atual = datetime.date.today().year

pessoa = dict()
pessoa['Nome'] = str(input('Qual seu nome? '))
pessoa['Ano de nascimento'] = int(input('Em que ano você nasceu? '))
pessoa['Idade'] = ano_atual - pessoa['Ano de nascimento']
pessoa['Clt'] = int(input('Número da Carteira de Trabalho:(0 não tem) '))

print('=-' * 20)

if pessoa['Clt'] == 0:
    print(F'Seu nome é {pessoa['Nome']}.')
    print(f'Sua idade é {pessoa['Idade']}.')
    print(f'Sua CLT tem valor 0.')

else:
    pessoa['Ano de contratação'] = int(input('Em que ano foi contratado? '))
    pessoa['Salário'] = int(input('Qual é seu salário?R$ '))
    print('=-' * 20)
    print(F'Seu nome é {pessoa['Nome']}.')
    print(f'Sua idade é {pessoa['Idade']}.')
    print(f'Sua CLT tem valor {pessoa['Clt']}.')
    print(f'Você foi contratado em {pessoa['Ano de contratação']}.')
    print(f'Seu salário é de R${pessoa['Salário']}.')
    pessoa['Aposentadoria'] = (pessoa['Ano de contratação'] - pessoa['Ano de nascimento']) + 35
    print(f'Você irá se aposentar com {pessoa['Aposentadoria']} anos, faltam ainda {pessoa['Aposentadoria'] - pessoa['Idade']} anos .')
