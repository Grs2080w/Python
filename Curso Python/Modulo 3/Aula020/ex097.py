def escreva(txt):
    n = len(txt) + 2
    print('~' * n)
    print(f' {txt}')
    print('~' * n)


escreva('Oi, meu nome é gabriel e eu tenho 16 anos')
escreva('Meu nome é gabriel')
escreva('Rayka é uma boboca')
escreva('O gabriel é o melhor, vai virar programador em 6 meses, espero q dos bons!')


# Com cores personalizáveis
def escreva2(txt, p=0, s=0, t=0):
    n = len(txt) + 2
    print(f'\033[{p}:{s}:{t}m~' * 117)
    print(f' {txt:^110}')
    print('~' * 117)