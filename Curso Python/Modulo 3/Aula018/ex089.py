ALUNOS = []
ALUNO = []

while True:
    no = str(input('Nome: '))
    ALUNO.append(no)
    n1 = float(input('Nota 1: '))
    ALUNO.append(n1)
    n2 = float(input('Nota 2: '))
    ALUNO.append(n2)
    ALUNOS.append(ALUNO[:])
    ALUNO.clear()
    while True:
        sn = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
        if sn == 'S' or sn == 'N':
            break
        else:
            print('Tente novamente.')
    if sn == 'N':
        break
print(' ')
print('=' * 26)
print('  {:^5}{:<13}{:^4}'.format('Nº', 'NOME', 'MÉDIA'))

for c in range(0, len(ALUNOS)):
    print(' {:^5}{:<13}{:>5}'.format(c, ALUNOS[c][0], (ALUNOS[c][1] + ALUNOS[c][2]) / 2))
print('=' * 26)
print('')

while True:
    na = int(input('Mostrar notas de qual aluno? (999 para interromper) '))
    if na == 999:
        break
    else:
        print(f'Notas de {ALUNOS[na][0]} são {ALUNOS[na][1:]}')
        print('=' * 22)

print(' ')
print('=' * 55)
print('FINALIZANDO...')
print('VOLTE SEMPRE >>>')


