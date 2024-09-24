def menupri():
    print('_' * 50)
    print(f'{'MENU PRINCIPAL':^50}')
    print('_' * 50)
    print('''\033[33m1 -\033[m Ver pessoas  cadastradas
\033[33m2 -\033[m Cadastrar nova Pessoa
\033[33m3 -\033[m Sair do programa''')
    print('_' * 50)


def opc():
    menupri()
    op = 0
    while True:
        try:
            v = 0
            op = int(input('\033[33mSua opção: \033[m'))
        except ValueError:
            print('Tente novamente digitando algumas das opções.')
            v = 1
            continue
        if op > 3 or op == 0:
            print('Tente novamente digitando algumas das opções.')
            v = 1
            continue

        if v == 0:
            break
    return op


def inseTxtex115(arq):
    while True:
        print('_' * 50)
        nome = str(input('Digite um nome: '))
        idade = str(input('Digite uma idade: '))
        try:
            arquivo = open(arq, 'a')
            arquivo.close()
        except (FileNotFoundError, FileExistsError):
            print('Arquivo não encontrado!')
        finally:
            with open(arq, 'a') as arqui:
                arqui.write(espdrText(nome, 43))
                arqui.write(espdrText(idade, 0)+' Anos\n')
                print(f'Novo registro de {nome} adicionado!')
                print('_' * 50)
                arqui.close()
        if sn() == 'N':
            break


def sn():
    while True:
        sina = str(input('Quer continuar?[S/N] ')).upper()[0]
        if sina == 'S' or sina == 'N':
            break
        else:
            continue
    return sina


def espdrText(c, n, v2=''):
    c += (n - len(c)) * '.' + f'{v2}'
    return c


def lerArq(nome):
    try:
        arq = open(nome, 'rt')
    except (FileNotFoundError, FileExistsError):
        print('Erro ao ler o arquivo!')
    else:
        print(arq.read())


arqu = 'ex115.txt'
while True:
    o = opc()
    if o == 1:
        with open('ex115.txt', 'r') as arquivo:
            print('_' * 50)
            print(f'{'PESSOAS CADASTRADAS':^50}')
            print('_' * 50)
            lerArq(arqu)
    if o == 2:
        inseTxtex115(arqu)
    if o == 3:
        break
print('\033[31m_' * 50)
print(f'{'\033[31mFINALIZANDO... ATÉ LOGO!':^50}')
print('_' * 50)