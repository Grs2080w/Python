lanche = 'Hambúrguer', 'Pudim', 'Sorvete', 'Pizza'
nome_campeonatos = 'Botafogo', 'Fortaleza', 'Flamengo', 'Palmeiras', 'São Paulo', 'Cruzeiro', 'Bahia', 'Athletico-PR', 'Atlético-MG', 'Vasco', 'Bragantino', 'Juventude', 'Grêmio', 'Criciúma', 'Internacional', 'Vitória', 'Corinthians', 'Fluminense', 'Cuiabá', 'Atlético-GO'''

#tuplas são imutáveis


for pos, comida in enumerate(lanche): #As variáveis têm que ser nessa posição, respectivamente com os comandos ENUMERATE e LANCHE.
    print(f'Vou comer {comida}, na posição {pos}')

print(' ')
#------------------------------------------------------------------------------------------------------------------------------------------------------------

for cont in range(0, len(lanche)):
    print(lanche[cont]) # Mostra Lanche na posição em que cont está, se cont estiver em 3, ira mostrar o índice 3 de Lanche, ou, Lanche[3].
    # Cont vai de 0 até o número de elementos que compõe a tupla ''Lanche'' .

print(' ')
#------------------------------------------------------------------------------------------------------------------------------------------------------------

for comida in lanche:
    print(comida) # Só mostra os elementos de acordo com à ordem da propria lista

print(' ')

print('Comi pra caramba!')

#-----------------------------------------------------------------------------------------------------------------------------------------

print(sorted(lanche)) #Reorganiza a tupla em ordem alfabética, mas não muda a ordem definitivamente.
print(lanche)

#----------------------------------------------------------------------------------------------------------------------------

a = (0, 0, 1, 2, 3, 4)
b = (5, 6, 7, 8, 9, 10)
c = (11, 12, 13, 14, 15)
g = a + b + c # Pode-se somar quantas variáveis quiser, aparentemente
print(g)

d = 'Gabriel '
e = 'Santos'
f = d + e
print(f)

print(len(g)) # Conta quantos fatores tem na soma das tuplas.
print(g.count(0)) # Conta quantas vezes um número apareceu dentro da soma de duas tuplas.
print(g.index(0, 1)) # index mostra em que posição da tupla o número está, o número depois da vírgula determina a partir de qual posição ele deve começar a contar.
# Tupla com texto em um (print), não resulta em parenteses, com número sim.


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

pessoa = ('Gabriel Santos', 16, 70, 1.65)
print(pessoa)
'''del pessoa # deleta uma Tuple e ela deixa de existir.'''
print(pessoa)

 # Tuplas aceitam strs e números
for c in range(0, 21, - 1):
    print(c)
