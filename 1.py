
"""import sys
import time

tiempo_actual = time.localtime()
print(f"{tiempo_actual[2]}/{tiempo_actual[1]}/{tiempo_actual[0]}")
print(f"{tiempo_actual[3]}:{tiempo_actual[4]}")

nombre = sys.argv[1:]

if nombre:
    for name in nombre:
        print(f"Que tal {name}! Bienvenide a la terminal!")

print(sys.platform)
print(sys.version)
print(sys.path)
"""

import sys
import os
from colorama import init, Fore, Back, Style

"""ruta=sys.argv[1]
tipo_dato = sys.argv[2]

lista=os.listdir(ruta)

if ruta:
    for archivo in lista:
        if archivo.endswith(tipo_dato):
            print(archivo)
else:
    print("no se especifico una ruta")
"""    

dibujo_noche = r"""
██████╗ ██╗   ██╗███████╗███╗   ██╗ █████╗ ███╗   ██╗ █████╗ ████████╗███████╗███████╗
██╔══██╗██║   ██║██╔════╝████╗  ██║██╔══██╗████╗  ██║██╔══██╗╚══██╔══╝██╔════╝██╔════╝
██████╔╝██║   ██║█████╗  ██╔██╗ ██║███████║██╔██╗ ██║███████║   ██║   █████╗  ███████╗
██╔═══╝ ██║   ██║██╔══╝  ██║╚██╗██║██╔══██║██║╚██╗██║██╔══██║   ██║   ██╔══╝  ╚════██║
██║     ╚██████╔╝███████╗██║ ╚████║██║  ██║██║ ╚████║██║  ██║   ██║   ███████╗███████║
╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝

           ¡Que descanses bien, nos vemos mañana!

  ____                _   _       _      _     _ 
 | __ )  ___   __ _  | \ | | ___ (_) ___| |__ (_)
 |  _ \ / _ \ / _` | |  \| |/ _ \| |/ __| '_ \| |
 | |_) | (_) | (_| | | |\  | (_) | | (__| | | | |
 |____/ \___/ \__,_| |_| \_|\___/|_|\___|_| |_|_|

 
     ____                 _   __      _      __    _ 
   / __ )____  ____ _   / | / /___  (_)____/ /_  (_)
  / __  / __ \/ __ `/  /  |/ / __ \/ / ___/ __ \/ / 
 / /_/ / /_/ / /_/ /  / /|  / /_/ / / /__/ / / / /  
/_____/\____/\__,_/  /_/ |_/\____/_/\___/_/ /_/_/   
                                                    
                                                 
"""
init()
#python ejercicio_scripts.py
#Style.BRIGHT
print(Fore.GREEN +Style.BRIGHT+ dibujo_noche)
print(Style.RESET_ALL)