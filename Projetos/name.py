from time import sleep
import random
from colorama import Fore
txt = """
                         88                       88              88
                         88                       ""              88
                         88                                       88
 ,adPPYb,d8  ,adPPYYba,  88,dPPYba,   8b,dPPYba,  88   ,adPPYba,  88
a8"    `Y88  ""     `Y8  88P'    "8a  88P'   "Y8  88  a8P_____88  88
8b       88  ,adPPPPP88  88       d8  88          88  8PP"""""""  88
"8a,   ,d88  88,    ,88  88b,   ,a8"  88          88  "8b,   ,aa  88
 `"YbbdP"Y8  `"8bbdP"Y8  8Y"Ybbd8"'   88          88   `"Ybbd8"'  88
 aa,    ,88
  "Y8bbdP"
  """


#print('                          88                       88              88')
#sleep(0.2)
#print('                          88                       ""              88')
#sleep(0.2)
#print('                          88                                       88')
#sleep(0.2)
#print('  ,adPPYb,d8  ,adPPYYba,  88,dPPYba,   8b,dPPYba,  88   ,adPPYba,  88')
#sleep(0.2)
#print(""" a8"    `Y88  ""     `Y8  88P'    "8a  88P'   "Y8  88  a8P_____88  88""" )
#sleep(0.2)
#print(' 8b       88  ,adPPPPP88  88       d8  88          88  8PP"""""""  88')
#sleep(0.2)
#print('  8a,   ,d88  88,    ,88  88b,   ,a8"  88          88  "8b,   ,aa  88')
#sleep(0.2)
#print("""  `"YbbdP"Y8  `"8bbdP"Y8  8Y"Ybbd8"'   88          88   `"Ybbd8"'  88'""" )
#sleep(0.2)
#print('  aa,    ,88')
#sleep(0.2)
#print('  "Y8bbdP"')
#sleep(0.2)



#def print_ascii_delayed(text):
#    for line in text.splitlines():
#        for char in line:
#            print(Fore.RED + char, end='')
#            sleep(0.009)  # Delay aleatório entre 0.05 e 0.2 segundos
#        print()  # Pula para a próxima linha após imprimir todas as letras da linha
#    Fore.RESET



def print_ascii_delayed(text):
    for line in text.splitlines():
        for char in line:
            print(Fore.RED + char, end='')  # Substitua GREEN por outras cores
            sleep(0.01)
            print(Fore.RESET, end='')
        print()
        

print_ascii_delayed(txt)