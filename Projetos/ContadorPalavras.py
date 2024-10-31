def contadorDePalavras():
    n = 0
    t = input("""'Cole ou digite seu texto aqui: '""")
    print(len(t))
    g = t.replace(' ', '')
    h = g.replace('', '')
    c = t.count(' ')

    print(f'Nesse texto tem {c + 1} palavras')

contadorDePalavras()