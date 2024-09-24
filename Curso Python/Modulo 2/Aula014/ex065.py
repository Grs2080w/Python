s = c = t = maior_numero = menor_numero = 0
resposta = 'Oi'
while resposta != 'NAO':
    n = int(input('Digite um número: '))
    s += n
    c += 1
    g = n
    if c == 2 and t < n:
        menor_numero = t
        maior_numero = n
    if c == 2 and t > n:
        maior_numero = t
        menor_numero = n
    elif c > 2 and n > t:
        g = n
        maior_numero = g
    elif c > 2 and n < t:
        t = n
        menor_numero = t
    t = n
    resposta = str(input('Quer continuar?[S]/[N] ')).upper()
    if resposta == 'N' or resposta == 'Não' or resposta == 'NÃO':
        resposta = 'NAO'
if c == 1:
    print('Foram digitado apenas um valor, {}.'.format(n))
else:
    print('Foram digitados {} valores. A média entre todos os valores foi de {}, o maior foi {} e o menor foi {}.'.format(c, s / c, maior_numero, menor_numero))
