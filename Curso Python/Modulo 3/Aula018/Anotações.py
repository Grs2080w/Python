'''teste = list()
teste.append('Gabriel')
teste.append(16)
galera = list()
galera.append(teste[:]) # Adiciona em 'galera' uma cópia de teste, sem interligar as duas.
teste[0] = 'Maria'
teste[1] = 17
galera.append(teste[:])
print(galera)

##########################################################################
pessoas = [['gabriel', 16], ['joao', 20], ['maria', 35]]
for p in pessoas:
    print(f'{p[0]} tem {p[1]} de idade.')'''

###########################################################################
pessoal = list()
dado = list()
mai = men = 0
for c in range(0, 3):
    dado.append(str(input('Digite seu nome: ')))
    dado.append(int(input('Digite sua idade: ')))
    pessoal.append(dado[:])
    dado.clear()
print(pessoal)
print('')
for p in pessoal:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        mai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        men += 1
print('')
print(f'O total de maiores de idade é {mai} e de menores é de {men}.')