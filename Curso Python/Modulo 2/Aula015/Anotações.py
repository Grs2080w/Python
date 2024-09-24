s = c = 0
while True:
    print(c, end= '-> ')
    c += 1
    if c == 1000:
        break
    s += c
print('\n')
print(f'A soma foi igual de {s}.')