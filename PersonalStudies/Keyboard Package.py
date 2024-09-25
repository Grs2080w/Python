import keyboard as kb
import pyautogui
import time

# Principais comandos Keyboard package

# kb.is_pressed('') > Verifica se a tecla dada como parâmetro foi apertada (RECEBE O VALOR DO DRIVER DO TECLADO, 'kb.press' NÃO É VÁLIDO, risco de crashar o pc.)
# kb.write('') > Escreve o texto dado como parâmetro
# kb.press('') > Pressiona a tecla dada como parâmetro

def ConAnd(f):
    #lista = [f]
    n = len(f)
    for c in range(0, n):
        print(f"'{f[c]}'" + ' and ' ,end='')

#Tranforma uma frase em algo aplicável como parâmetro no kb.is_pressed do While abaixo (Apagar último 'and') (Recomendável Ctrl C Ctrl V).


# t = str(input('Frase:'))
# ConAnd(t)


while True:
    if kb.is_pressed('g' and 'a' and 'b' and 'r' and 'i' and 'e' and 'l'):
        p = pyautogui.position()
        pyautogui.click(p)
        kb.write('Messi is cool')
        print('Function Done')
        break


''' Na função acima é possível usando os comandos explicados, é criado um loop, e ao ser digitada
preditas, é lida a posição do Mouse, click nessa posição, escrito o texto proposto, retornadp
uma resposta e por fim um break  

Detalhe: Pode-se usar uma palavra ou frase parâmetro pro kb.is_pressed, mas é necessário escrever
da forma acima. (Portuguese)

'''


