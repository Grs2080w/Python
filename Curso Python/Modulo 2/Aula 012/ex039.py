import datetime
from time import sleep

data_atual = str(datetime.date.today().today())
#Mostra a data atual, dd mm aa
dia_atual = int(datetime.date.today().day)
#Mostra o dia atual, dd
mes_atual = int(datetime.date.today().month)
#Mostra a data do mes atual, mm
ano_atual = int(datetime.date.today().year)
#Mostra o ano atual, aa

ano_nas = int(input('Qual seu ano de nascimento? '))
print('-=' * 50)
print(' ')
print('Processando...')
print(' ')
sleep(3)
print('-=' * 50)
print(' ')

idade_ind = ano_atual - ano_nas

#print(ano_atual)
#print(ano_nas)



if idade_ind < 18:
    print('Aguarde \033[7m{}\033[m anos para se alistar no serviço militar.'.format(18 - idade_ind))

elif idade_ind == 18:
    print('Já está na hora de se alistar no serviço militar!')
elif idade_ind > 18:
    print('Você passou \033[7m{}\033[m ano da hr de se alistar.'.format(idade_ind - 18))
    sn = input('Você já se alistou?')
    if sn in 'Sim sim':
        print('Muito bem, tudo certo!')
    elif sn in 'Não não nao Nao':
        print('Voce deve pagar uma multa de R$5.53')

    #Esse foi top ein












