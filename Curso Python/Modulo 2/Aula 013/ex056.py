s = 0
contagem_de_mulheres = 0
idade_homem_maior = 0

for c in range(1, 5):
    print('\033[33m{}º pessoa\033[m'.format(c))
    print('=-'*40)
    nom = input('\033[36mQual seu nome? ').upper().strip()
    ida = float(input('Sua idade? '))
    s += ida
    sx = input('[M/F]? \033[m').upper()
    print('=-'*40)
    if sx == 'F' and ida < 20:
        contagem_de_mulheres += 1
    if sx == 'M' and c == 1:
        idade_homem_maior = ida
    elif sx == 'M' and c > 1 and ida > idade_homem_maior:
        idade_homem_maior = ida
        nome_homem_maior = nom



media_idade = s/4
print('\033[34mA média de idade das 4 pessoas é de {} anos.'.format(media_idade))
print('\033[34mO nome do homem mais velho é {}, e sua idade é de {} anos.'.format(nome_homem_maior, idade_homem_maior))
if contagem_de_mulheres > 0:
    print('\033[34mO número de mulheres que tem menos de 20 anos é de {} mulheres.'.format(contagem_de_mulheres))
elif contagem_de_mulheres == 0:
    print('Nenhuma das mulheres é mais nova que 20 anos, mas não significa que sejam velhas!')
