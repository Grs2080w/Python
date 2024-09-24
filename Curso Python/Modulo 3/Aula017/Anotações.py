num = [0, 1, 2, 4]
let = ['a', 'c', 'b', 'd']
num[2] = 3 # Modifica o elemento conforme o índice.
num.append(5) # Adiciona um elemento no fim da lista, sempre.
num.sort() # Coloca os elementos em ordem, seja número ou letra.
num.sort(reverse=True)  # Coloca os elementos em ordem decrescente.
num.insert(2, 3) # Adiciona um elemento na posição informada. Núm, = índice e ,Núm=elemento a ser trocado, não substitui nada.
num.pop() #Apaga o ultimo índice da lista ou o índice indicado se tiver algo dentro dos parenteses.
num.remove() # Remove o elemento indicado no parenteses, se tiver mais que um, ele elimina o primeiro e deixa o segundo.

print(let)
print(num)
print(f'A lista "Num" tem {len(num)} elementos e a lista "Let" tem {len(let)} elementos.')


if 4 in num:
    num.remove(4)
    print('O 4 foi removido.')
else:
    print('Na lista não tinha 4.')

#########################################################################################################################################################################

Valores = []

#Valores.append(5)
#Valores.append(6)
#Valores.append(7)

#for v in Valores:
#    print(f'{v}...', end='') Mostra os elementos na lista até acabar.

print(' ')

#for cont in range(0, 4):
#    Valores.append(int(input('Digite um valor: '))) # Adiciona valores conforme com o range.


for c, v in enumerate(Valores):
    print(f'O número {v} está na posição {c}!') # Mostra o número e a posição.
print('Cheguei ao final da lista.')

print(' ')
######################################################################################################################################################

a = [0, 1, 2, 3, 4]
c = a[:] # C vira uma cópia de A.
b = a
b[2] = 4 # Altera as duas listas, A e B, porque estão ligadas.

print(f'Lista A; {a}')
print(f'Lista b; {b}')
print(f'Lista c; {c}')