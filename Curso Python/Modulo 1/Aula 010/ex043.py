peso = float(input('Qual seu peso?'))
altura = float(input('Qual sua altura? '))
i_m_c = float(peso / (altura ** 2))

if i_m_c < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 < i_m_c < 25:
    print('Você está no peso ideal.')
elif 25 <= i_m_c < 30:
    print('Voce está com sobrepeso.')
elif 30 <= i_m_c < 40:
    print('Voce está obeso(a).')
elif i_m_c > 40:
    print('Voce está com obesidade mórbida.')

