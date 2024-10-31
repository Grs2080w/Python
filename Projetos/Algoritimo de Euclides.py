

def euclides(a, b):
    if a == b:
        return a
    elif b > a:
        return euclides(a, b-a)
    elif a > b:
        return euclides(b, a-b)


c = int(input('Digite um número: '))
d = int(input('Digite outro número: '))

print(f'O Maior divisor comum entre {c} e {d} é ({euclides(c, d)}).')

# Algorítimo de Euclides utilizando o conceito de função Recursiva.
