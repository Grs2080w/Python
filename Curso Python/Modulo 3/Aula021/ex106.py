

def escreva2(txt, p=0, s=0, t=0):
    #n = len(txt) + 2
    print(f'\033[{p}:{s}:{t}m~' * 117)
    print(f' {txt:^110}')
    print('~' * 117)


def hellp():
    while True:
        escreva2('SISTEMA DE AJUDA HELLpG', 0, 30, 45)
        fun = input('\033[m''Função ou Biblioteca > ').lower().strip()
        if fun == 'fim':
            break
        escreva2(f'Acessando o manual do comando "{fun}" ', 0, 30, 46)
        print('\033[3:43m'), help(fun)

    escreva2('\033[M''ATÉ LOGO!', 3, 30, 41)


hellp()
