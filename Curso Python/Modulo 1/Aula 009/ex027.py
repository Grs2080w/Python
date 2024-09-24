nome = str(input('Qual seu nome?'))
print('Prazer em te conhecer!')

n = str.split(nome)

print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))