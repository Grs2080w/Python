def mensagem(txt):
    print('=-' * 20)
    print(txt)
    print('=-' * 20)



mensagem('           Gabriel é demais             ')
mensagem('            Rayka é fulera              ')



def soma(a, b):
    som = a + b
    print(som)


soma(8, 92)
soma(9, 91)
soma(73, 27)
soma(2, 98)

soma(b=9, a=5)


def contador(* num):
    tam = len(num)
    print(f'Recebi valores {num} e são {tam} valores.')


contador(6, 7, 8, 9)
contador(2, 3, 4, 5,)

#######################################################################################################################################


def cont():
    c = 0
    numero = []
    while True:
        n = int(input('Digite um número: '))
        if n == 999:
            break
        numero.append(n)
        c += 1
    print(f'Tem {c} números')
    print(f'E foram digitados os números {numero}.')


cont()


############################################################################################################################################

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [1, 2, 3, 4, 5, 6]
dobra(valores)
print(valores)

########################################################################################################################################


def s(* algarismos):
    so = 0
    for n in algarismos:
        so += n
    print(f'Os números foram {algarismos} e a soma deles foi de {so}.')


s(8, 5, 6, 9, 4, 3, 1)