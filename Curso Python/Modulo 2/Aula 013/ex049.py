num = int(input('Digite um numero: '))
n = num * 10 + 1
s = 0

print('=-' * 50)
for c in range(num, n, num):
    s += 1
    print('{} x {} = {}'.format(num, s, c))

print('=-' * 50)
