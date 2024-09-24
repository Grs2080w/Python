nome = str(input('Qual seu nome? '))
if nome == 'Gabriel':
    print('Que nome bonito Gabriel')
elif nome == 'Rayka':
    print('Seu nome é mais ou menos.')
elif nome in 'Pedro João Maria Lucas':
    print('Seu nome é bem comum!')

print('Tenha um Bom dia, \033[33m{}!'.format(nome))