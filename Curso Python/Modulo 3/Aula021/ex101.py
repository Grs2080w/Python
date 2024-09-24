import datetime
ano_atual = datetime.date.today().year


def voto(n):
    idade = ano_atual - n

    if idade < 16:
        return 'NEGADO'

    elif 16 <= idade < 18 or idade >= 65:
        return 'OPICIONAL'

    else:
        return 'OBRIGATÓRIO'


print('_' * 30)
num = int(input('Digite seu ano de nascimento: '))
print(f'Com {ano_atual - num} anos: VOTO {voto(num)}.')
