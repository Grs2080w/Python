def leiaDinheiro():
    while True:
        p = input('Digite o preço:R$ ')
        pr = p.replace(',', '.')
        pre = p.replace('.', '').replace(',', '')
        if pre.isdigit():
            break
        else:
            print('\033[31mERRO! Digite um preço válido. \033[m')
    return float(pr)


