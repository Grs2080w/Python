def ficha():
    """
    Txt recebe o nome do jogador e coloca a primeira letra em maiúsculo.
    Se txt não receber nada, ou txt == '', txt vale <desconhecido>.
    N recebe o número de gols, se n não receber nada, n = 0

    No final é mostrado o print com o nome e o número de gols.
    """
    print('_' * 30)
    txt = str(input('Nome do jogador: ')).capitalize()
    if txt == '':
        txt = '<desconhecido>'
    n = input('Número de Gols: ')
    if n == '':
        n = 0
    print(f'O jogador {txt} fez {n} gol(s) no campeonato.')


ficha()