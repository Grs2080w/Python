# Abrir arquivos
# open('nome do arquivo', modo de leitura')

# Uma variável recebe o arquivo, ent
arquivo = open()

"""
'r': modo de leitura (read), usado para ler o conteúdo do arquivo.
'w': modo de escrita (write), usado para escrever dados em um arquivo. Se o arquivo não existir, ele será criado. Se já existir, seu conteúdo será substituído.
'a': modo de anexação (append), usado para adicionar dados ao final de um arquivo existente.
"""

Arquivo.close()

#############################################################################################################################################################################

#with open("exemplo.txt", "r") as arquivo:

""" Se quisermos ler todo o conteúdo de um arquivo de uma só vez, podemos usar o método read(). 
Ele lê o arquivo inteiro e atribui seu conteúdo a uma variável. Podemos então realizar operações nessa variável, 
como imprimir ou manipular os dados."""

#Aqui está um exemplo:

with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

"""No código acima, o método read() lê todo o conteúdo do arquivo e o atribui à variável conteudo. 
Em seguida, podemos realizar operações nessa variável, como imprimir ou manipular os dados."""


##############################################################################################################################################

# Leitura Linha por Linha

with open("exemplo.txt", "r") as arquivo:
    linha = arquivo.readline()
    while linha:
        print(linha)
        linha = arquivo.readline()

# No código acima, o método readline() é chamado dentro de um loop para ler cada linha até que não haja mais
# linhas no arquivo.


########################################################################################################################################################


# Leitura de um Número Específico de Caracteres


"""Se quisermos ler um número específico de caracteres de um arquivo, podemos usar o método read(n), 
#em que n especifica o número de caracteres a serem lidos. Aqui está um exemplo:"""

with open("exemplo.txt", "r") as arquivo:
    caracteres = arquivo.read(10)
    print(caracteres)

# No código acima, o método read(10) lê os primeiros 10 caracteres do arquivo e os imprime.


##########################################################################################################################################################


# Escrita em arquivos===========================

###Escrita de um Único Texto
'''Se quisermos escrever um único texto em um arquivo, podemos usar o método write(). 
Ele escreve o texto especificado no arquivo.'''

with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!")

#No código acima, o método write() é usado para escrever o texto "Olá, mundo!" no arquivo "exemplo.txt".
#Se o arquivo já existir, seu conteúdo será substituído pelo novo texto. Se o arquivo não existir, ele será criado.


###Escrita de várias linhas===============================

""" Se quisermos escrever várias linhas em um arquivo, podemos usar o método writelines(). Ele recebe uma lista de strings, 
em que cada string representa uma linha a ser escrita no arquivo."""

linhas = ["Primeira linha\n", "Segunda linha\n", "Terceira linha\n"]

with open("exemplo.txt", "w") as arquivo:
    arquivo.writelines(linhas)

#No código acima, usamos o método writelines() para escrever as linhas especificadas na lista
# linhas no arquivo "exemplo.txt"




# https://www.covildodev.com.br/artigo/arquivos-python