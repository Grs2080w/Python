import pyautogui
import selenium

print(pyautogui.position()) # Pega a posição do mouse. X Y
#x=1288, y=397
#x=538, y=433
#x=959, y=810
#(x=1486, y=34)

pyautogui.moveTo((511, 180)) # Move o mouse para a posição X Y instantaneamente.
pyautogui.click()
pyautogui.moveTo()
pyautogui.click()
#pyautogui.sleep(1) # É um timer em segundos
#pyautogui.moveTo(x=538, y=433)
#pyautogui.sleep(1)
#pyautogui.moveTo(x=959, y=810)
#pyautogui.click() # Clica nas coordenadas XY


