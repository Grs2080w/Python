pessoas = {'nome': 'Gabriel', 'idade': 16, 'sexo': 'M'}
print(f'{pessoas['nome']} é do sexo {pessoas['sexo']} e tem {pessoas['idade']} anos.')
pessoas['nome'] = 'Gabs' # Altera o valor de uma key se ela já existir
pessoas['peso'] = 60 # Adiciona um item ao dicionário se ela não existir
del pessoas['sexo'] #Apaga uma key
for k in pessoas.keys(): # Mostra as keys do dicionario
    print(k)
for k in pessoas.values(): # Mostra os valores do dicionario
    print(k)
for k, v in pessoas.items():  # Mostra os dois
    print(f'{k} = {v}')
#########################################################################################
brasil = []
estado1 = {'uf': 'Goiás', 'sigla': 'GO'}
estado2 = {'uf': 'Mato Grosso', 'Sigla': 'MT'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])
##########################################################################################

estado = {}
brasil = []

for c in range(0, 3):
    estado['uf'] = str(input('Digite o nome do estado: '))
    estado['sigla'] = str(input('Digite a sigla do estado: '))
    brasil.append(estado.copy()) # Copia o que ta dentro do append pra lista.
print(brasil)

for e in brasil: # Mostra todos os elementos de brasil, nesse caso, os estados adicionados
    for k, v in e.items():
        print(f'{k} = {v}.')