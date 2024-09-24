
c = op = 0
arquivo = open('ex115.txt', 'r')
while True:
    print('_' * 50)
    print(f'{'MENU PRINCIPAL':^50}')
    print('_' * 50)
    print('''\033[33m1 -\033[m Ver pessoas  cadastradas
\033[33m2 -\033[m Cadastrar nova Pessoa
\033[33m3 -\033[m Sair do programa''')
    print('_' * 50)
    while True:
        try:
            c = 0
            op = int(input('\033[33mSua opção: \033[m'))
        except ValueError:
            print('Tente novamente digitando algumas das opções.')
            c += 1
        if op > 3 or op == 0:
            print('Tente novamente digitando algumas das opções.')
            c += 1

        if c == 0:
            break

    if op == 1:
        with open('ex115.txt', 'r') as arquivo:
            print('_' * 50)
            print(f'{'PESSOAS CADASTRADAS':^50}')
            print('_' * 50)
            linha = arquivo.read()
            while linha:
                print(linha)
                linha = arquivo.read()


    if op == 2:
        print('_' * 50)
        nome = str(input('Nome: '))
        nome += (43 - len(nome)) * '.'
        idade = str(input('Idade: '))
        idade += ' Anos\n'
        with open('ex115.txt', 'a') as arquivo:
            arquivo.write(nome)
            arquivo.write(idade)

    if op == 3:
        break
print('\033[31m_' * 50)
print(f'{'\033[31mFINALIZANDO... ATÉ LOGO!':^50}')
print('_' * 50)

