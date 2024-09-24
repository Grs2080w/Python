import time

def timer(f, *args, **kwargs):
    def modificada():
        start = time.time()
        f()
        end = time.time()
        print(f'Essa função demorou `{end - start} segundos')
    return modificada()


def funcao1():
    for i in range(200000):
        print(i)


def funcao2():
    for i in range(100000):
        print(i)


