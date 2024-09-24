n = int(input('Quantos termos de Fibonacci você quer? '))-2
N = n + 2
c = 0
s = 1
t = 1
print(' ')
print('Os {} primeiros números de Fibonacci são:\n1 >> 1 >> '.format(N), end='' )
while c != n:
    r = s + t
    #Resultado é igual 2, porque 1 + 1 = 2. No segundo momento, s vale 2, 2 + 1 = 3. Terceiro Momento, 3 + 2 = 5.
    print(r, end='')
    print('.' if c == n - 1 else ' >> ', end='')
    t = s #T recebe 1. Segundo momento, t vale 2. Terceiro momento, t vale 3.
    s = r #S recebe r, q é igual a 2. Segundo momento, S vale 3, Terceiro momento, s vale 5
    c += 1

    # E assim vai até o contador ser igual ao número de termos escolhidos.
    # Programa totalmente original

