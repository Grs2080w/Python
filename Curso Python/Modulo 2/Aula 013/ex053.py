frase = str(input('Digite uma frase: ')).lower()
frase_1 = frase.replace(' ', '')
frase_2 = frase_1[::-1]
if frase_2 == frase_1:
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase não é um palíndromo.')