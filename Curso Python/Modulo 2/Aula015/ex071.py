print('=' * 54)
print('                         \033[1mBDG\033[m')
print('=' * 54)

while True:
    valor = int(input('Que valor você quer sacar?R$ '))
    qn50 = valor // 50
    qn20 = (valor % 50) // 20
    qn10 = (valor % 20) // 10
    qn1 = (valor % 10) // 1
    if qn50 != 0:
        print(f'Serão R${qn50 * 50} em {qn50} notas de R$50.')
    if qn20 != 0:
        print(f'Serão R${qn20 * 20} em {qn20} notas de R$20.')
    if qn10 != 0:
        print(f'Serão R${qn10 * 10} em {qn10} notas de R$10.')
    if qn1 != 0:
        print(f'Serão R${qn1 * 1} em {qn1} notas de R$1.')
    if qn50 == 0 or qn20 == 0 or qn10 == 0 or qn1 == 0 or qn1 != 0:
        break
print('=' * 54)
print('////VOLTE SEMPRE AO BANCO BDG! TENHA UM BOM DIA!////')
print('=' * 54)
