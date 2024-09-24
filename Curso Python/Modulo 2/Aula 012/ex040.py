med1 = float(input('Digite sua primeira nota: '))
med2 = float(input('Digite sua segunda nota: '))
media = (med1 + med2) / 2

if media <= 5:
    print(' ')
    print('=' * 40)
    print('Você foi reprovado, tente de novo!')
elif 5 < media < 6.9:
    print(' ')
    print('=' * 40)
    print('Você está de recuperação.')
elif media >= 7:
    print(' ')
    print('=' * 40)
    print('!!!Você foi aprovado!!!')