def arquivoExiste(nome, show=False):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        if not show:
            return False
        if show:
            print('Aquivo não encontrado!')
    else:
        if not show:
            return True
        if show:
            print('Arquivo encontrado.')


def sn():
    while True:
        sina = str(input('Quer continuar?[S/N] ')).upper()[0]
        if sina == 'S' or sina == 'N':
            break
        else:
            continue
    return sina


def criarArq(nome, show=False):
    arquivo = open(nome, 'wt+')
    arquivo.close()
    if not show:
        return True
    if show:
        print(f'Aquivo {nome} Criado!')


def lerArq(nome):
    try:
        arq = open(nome, 'rt')
    except (FileNotFoundError, FileExistsError):
        print('Erro ao ler o arquivo!')
    else:
        print(arq.read())


def espdrText(c, n, v2=''):
    c += (n - len(c)) * '.' + f'{v2}'
    return c


def inseTxt(arq, cntdo):
    """

    :param arq: Nome do arquivo a ser adicionado
    :param cntdo: Conteúdo a ser copiado para o arquivo
    :return: True se o arquivo foi adicionado, None se houve erro.
    """
    try:
        arquivo = open(arq, 'a')
        arquivo.close()
    except (FileNotFoundError, FileExistsError):
        return None
    finally:
        with open(arq, 'a') as arqui:
            arqui.write(espdrText(arq, cntdo))
            arqui.close()
    return True
