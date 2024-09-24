palavras = ('python', 'teclado', 'computador', 'celular', 'garrafa', 'cubo', 'adesivo', 'fone', 'ventilador', 'tampa', 'cama', 'casaco', 'bolsa', 'mochila', 'caderno', 'tinta')
c = 0
while True:
    print('\n'f'Na palavra {palavras[c]} temos:', end=' ')
    if palavras[c].count('a') >= 1:
        print('a', end=' ')
    if palavras[c].count('e') >= 1:
        print('e', end=' ')
    if palavras[c].count('i') >= 1:
        print('i', end=' ')
    if palavras[c].count('o') >= 1:
        print('o', end=' ')
    if palavras[c].count('u') >= 1:
        print('u', end=' ')
    c += 1
    if c == len(palavras):
        break
print('\n')
print('Processo Finalizado!')
