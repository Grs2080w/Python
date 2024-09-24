nome = str(input('Qual é seu nome?')).strip()

print('Seu nome com as letras maiusculas fica: {}'.format(nome.upper()))
print('Seu nome com as letras minúsculas fica: {}'.format(nome.lower()))
print('Seu nome possui {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
