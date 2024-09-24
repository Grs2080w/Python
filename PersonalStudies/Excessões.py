try:
    print(1/0)
except:
    raise RuntimeError('Algo deu errado na hora de Dividir...') from None