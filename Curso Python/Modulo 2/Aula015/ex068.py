import random

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
#PI = 1, 2
c = 0
while True:
    #valor_computador = random.choice(PI)
    numerocomp = random.randint(0, 10)
    valor = int(input('Digite um valor: '))
    IP = str(input('Par ou Ímpar?[P/I] ')).upper()
    print('_' * 20)
    print(f'Você jogou {valor} e o Compultador jogou {numerocomp}. Total de {valor + numerocomp} ', end='')
    print('Deu par.' if (valor + numerocomp) % 2 == 0 else 'Deu ímpar.')
    print('_' * 20)
    if IP == 'P' and (valor + numerocomp) % 2 == 0:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('-=' * 15)
        c += 1
    elif IP == 'P' and (valor + numerocomp) % 2 == 1:
        print('Você PERDEU!')
        print('=-' * 15)
        break
    elif IP == 'I' and (valor + numerocomp) % 2 == 0:
        print('Você PERDEU!')
        print('=-' * 15)
        break
    elif IP == 'I' and (valor + numerocomp) % 2 == 1:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('-=' * 15)
        c += 1

if c == 0:
    print('GAME OVER!!! Você não venceu nenhuma vez!.')
else:
    print(f'GAME OVER!! Você venceu {c} vezes.')


#IP == 'ÍMPAR' or IP == 'IMPAR'