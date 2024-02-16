import os
import platform

def limpiar_consola():
    sistema_operativo = platform.system()
    if sistema_operativo == 'Windows':
        print("sd")
        os.system('cls')
    else:
        os.system('clear')