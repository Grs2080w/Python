from threading import Thread, active_count
from math import sin


'''def trabalhador(num):
    while True:
        ativas = active_count()-1 # Conta quantos Threads o compultador está usando.
        print(f'Trabalhador {num} de {ativas} threads ativas.')
        return


for i in range(5):
    t = Thread(target=trabalhador, args=(i,))
    t.start()'''

#################################################################################################################
x = int(input('nume:'))
t = u = x


def expo(x):
    resp_expo = x ** 2
    return resp_expo



def mult(t):
    resp_mult = 3 * t
    return resp_mult




def seno(u):
    resp_seno = sin(u)
    return resp_seno


thread1 = Thread(target=expo, args=x)
thread2 = Thread(target=mult, args=t)
thread3 = Thread(target=seno, args=u)
thread1.start()
thread2.start()
thread3.start()

fx = resp_expo + resp_mult + resp_seno
print('Equação f(x) = x**2 + 3*x + sen(x)')
print(f'Resultado para x = {x}: {fx}')



