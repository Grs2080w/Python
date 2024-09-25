import pyautogui, keyboard as kb


n = pyautogui.position()
print(n)

while True:
    n = pyautogui.position()
    pyautogui.click(n)
    if kb.is_pressed('f'):
        break

# Ao ser ativado, clica infinitamente (Mesmo se mover o mouse) até que se aperte a tecla 'f'