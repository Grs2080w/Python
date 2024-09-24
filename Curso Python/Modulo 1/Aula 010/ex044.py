from unidecode import unidecode

#Essa biblioteca tira todos os acentos de uma string


preco_normal = float(input('Qual o preço do produto?R$ '))
forma_de_pagamento = str(input('O valor vai ser pago À vista, À vista no cartão, Em até 2x no cartão\nOu em 3x no cartão? '))
forma_de_pagamento1 = unidecode(forma_de_pagamento).lower()
#Aqui o 'unidecode' vai tirar todos os acentos para eliminar todas as possibilidades de se escrever a resposta.
#O lower deixa tudo em minusculo pelo mesmo motivo.

if forma_de_pagamento1 == 'a vista':
    print(' ')
    print('Você ganhou um cheque de 10% de desconto!')
    print(' ')
    print('O valor a ser pago será de R${}.'.format(preco_normal - (preco_normal * 0.10)))
elif forma_de_pagamento1 == 'a vista no cartao':
    print(' ')
    print('Você ganhou um cheque de 5% de desconto!')
    print(' ')
    print('O valor a ser pago será de R${}.'.format(preco_normal - (preco_normal * 0.05)))
elif forma_de_pagamento1 == '2x no cartao':
    print(' ')
    print('O preço a pagar será o valor de R${}.'.format(preco_normal))
    print(' ')
elif forma_de_pagamento1 == '3x no cartao':
    print(' ')
    print('O preço a pagar será o valor de R${}.'.format(preco_normal + (preco_normal * 0.20)))
    print(' ')