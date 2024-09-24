aluno = {'nome': str(input('Nome: '))}
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))
if aluno['media'] >= 6:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
print('')
print(f'Nome é igual a {aluno['nome']}')
print(f'Média é igual a {aluno['media']}')
print(f'Situação é {aluno['situação']}')