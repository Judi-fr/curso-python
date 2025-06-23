from ascii import bomGia, boaNoite, asci
from voice_config import escuchar_lo_dicho
import os
from time import localtime, sleep
from playsound import playsound
from colorama import Fore, init, Style

"""Hora = localtime()

init()
os.system("cls")
if Hora[3] > 13 and Hora[3] < 18:
    print(Fore.MAGENTA +Style.BRIGHT)
elif Hora[3] > 18 or Hora[3]<6:
    print(Fore.LIGHTYELLOW_EX +Style.NORMAL+boaNoite )
elif Hora[3]>6 and Hora[3]<13:
    print(Fore.MAGENTA +Style.BRIGHT+bomGia )
print(Style.RESET_ALL)"""

init()
os.system("cls")
print(Fore.RED +Style.DIM+asci)

#saludo
init()
#playsound("C:/Users/ezeri/Documents/Python/script/Audios/ezequielio.mp3")
#sleep(1)
print(Fore.RED, Style.DIM, "Bienvenido Ezequiel.")
playsound("C:/Users/ezeri/Documents/Python/script/Audios/bienvenido_ezequiel1.mp3")
print(Style.RESET_ALL)


while True:
    init()
    os.system("pause")
    print()
    
    print(Fore.RED,Style.DIM,"Preparate para hablar..")
    print(Style.RESET_ALL)
    
    for numero in range(3,-1,-1):
        print(f"En {numero}..",end="\r")
        sleep(0.7)
    
    print(Fore.RED,Style.DIM,"escuchando..")
    print(Style.RESET_ALL)

    escuchar_lo_dicho()

"""
import json
with open("script/argentina_states.json","r") as f:
    objeto = json.load(f)
    for objetos in objeto:
        print(f"{objetos["code"]} - {objetos["name"]}")"""

Hora = localtime()

init()

if Hora[3] > 13 and Hora[3] < 18:
    print(Fore.MAGENTA +Style.BRIGHT+boaNoite )
    playsound()
elif Hora[3] > 18 or Hora[3]<6:
    print(Fore.MAGENTA +Style.BRIGHT+boaNoite )
    playsound()
elif Hora[3]>6 and Hora[3]<13:
    print(Fore.MAGENTA +Style.BRIGHT+bomGia )
    playsound()

print(Style.RESET_ALL)
