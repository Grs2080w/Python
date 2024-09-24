try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
# except Exception as erro:
#   print(f'Problema encontrado foi {erro.__cause__}')
except (ValueError, TypeError):
    print('Tivemos problemas com os tipos de dados que você digitou :(')
except ZeroDivisionError:
    print('Desculpe, nenhum número pode ser dividido por zero :(')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados :(')
else: # Opicional
    print(f'O resultado é {r:.2f}')
finally: # Opicional
    print('Volte sempre, muito obrigado!')
