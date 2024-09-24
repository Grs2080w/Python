""" O interactive help é um comando que no qual você digita help(), e entre os parenteses
você coloca o nome de qualquer função do python, e ele irá mostrar o manual daquela função, ou
o que ela faz. Também pode ser escrito na forma de documento, como 'print(input.__doc__)', essa
função irá retornar a documentação do comando input, o mesmo que em help(), talvez com algo a mais ou
algo a menos. """


def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela.
    :param i: Início da contagem.
    :param f:Fim da contagem.
    :param p:Passo da contagem.
    :return:Sem retorno
    Função criada por Gustavo Guanabara do canal curso em video.
    """
    c = i
    while c <= f:
        print(f'{c}  ', end=' ')
        c += p
    print('FIM')


""" Docstring é o termo usado para nomear o manual de uma função, na docstring, é 
informado ao usuário quais as funções dos parâmetros daquela função, como ela pode ser
usada e até outras coisas. Pra isso, se coloca três aspas duplas na linha abaixo ao
comando def, assim o python criará automaticamente linhas pedindo pra informar a função
de cada parametro da função, e mais outras coisas."""


def somara(a=0, b=0, c=0):
    s = a + b + c
    print(f' A SOMA VALE {s}.')


"""O conceito de parametro opcional se refere ao sinal de igual depois dos
parâmetros dentro da função contador, aquele sinal diz que se aquele parametro na
função não receber valor nenhum, ela vale o valor depois do sinal de igual, isso 
vale pra todos os parâmetros."""


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s  # Retorna um valor para fora do escopo local.


#r1 = somar(6, 5, 4)
#r2 = somar(4, 5)
#r3 = somar(7)

#print(f'Os resultados foram {r1}, {r2} e {r3}.')

"""A função return manda pra fora do escopo local o valor que vem depois dela, então nesse caso a variável s, assim
return s, manda pra fora o valor de s, e quem tá 'fora', nesse caso uma variável que recebe soma, vai receber o
valor de s. Então r1 = somar, a função sera realizada dentro do def, e o return vai retornar a resposta, ou no caso, o
valor de s, para a variável que recebeu a função somar. Dessa forma o print pode ficar fora do def, abrindo novas
oportunidades."""


###################################################################################################################################################


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f # Nesse caso o return retornou um valor numérico vindo de uma variável.


#n = int(input('Digite um número: '))
#print(f'O Fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(6)
f2 = fatorial(4)
f3 = fatorial()

print(f'O fatoriais são {f1}, {f2} e {f3}.')

##############################################################################################################################################


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False # Nesses casos ela retornou a informação de verdadeiro ou falso.


num = int(input('Digite um número: '))
if par(num):
    print(f'{num} é par!')
else:
    print(f'{num} é ímpar!')
