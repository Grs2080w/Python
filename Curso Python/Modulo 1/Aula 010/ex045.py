import random

opc_escolhida = str(input('Voce escolhe pedra, papel ou tesoura? ')).lower()

#Codigo pra fazer o pc escolher pedra papel ou tesoura
pc = 'pedra papel tesoura'.split()
pc1 = random.choice(pc)

if opc_escolhida == 'pedra' and pc1 == 'tesoura' or opc_escolhida == 'papel' and pc1 == 'pedra' or opc_escolhida == 'tesoura' and pc1 == 'papel':
    print('-=' * 50)
    print(' ')
    print('\033[31mEu escolhi {}, você ganhou.\033[m'.format(pc1))
elif pc1 == 'pedra' and opc_escolhida == 'tesoura' or pc1 == 'papel' and opc_escolhida == 'pedra' or pc1 == 'tesoura' and opc_escolhida == 'papel':
    print('-=' * 50)
    print(' ')
    print('\033[35mEu escolhi {}, eu ganhei!'.format(pc1))
elif opc_escolhida == pc1:
    print('-=' * 50)
    print(' ')
    print('\033[34mEmpatamos, aff!')