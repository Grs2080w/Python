s = c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Foram {c} valores e a soma desses valores é igual a {s}.')