# ~ from Estructura import *
'''
Escribir un programa que simule el famoso juego del ahorcado.

El programa debe cumplir los siguientes requisitos:
1)  El programa debe preguntar al usuario la palabra a adivinar. 
        A partir de la palabra introducida debe crear una lista con los caracteres de la palabra.
        Después debe ir preguntando al usuario por letras hasta ser ahoracado o hasta que no queden letras en la lista. 
        En ambos casos el programa terminará pero mostrará el mensaje `Perdiste` si se comenten los fallos necesarios para que quede ahorcado y el mensaje `Ganaste` si no quedan palabras en la lista.
        Cada vez que el usuario introduzca una nueva letra, si la letra está en la lista se reemplazara por el guion en la palabra y se mostrará el mensaje `Acierto`, 
            mientras que si la letra no está en la lista mostrará el mensaje `Fallo`. 
        Si la letra está más de una vez en la lista se reemplaza todas las vescas que aparezca en la palabra.


Requisito adicional para un punto extra:
2)  El programa debe guardarse el historico con el nombre ahorcado.py .
3)  Cada vez que el usuario acierte una letra debe mostrar la palabra a adivinar con las letras acertadas hasta el momento y el resto reemplazadas por asteriscos.


Cuando el programa esté terminado, añadir el fichero ahorcado.py a la zona de intercambio temporal y hacer un commit con el mensaje `Añadida respuesta ejercicio 3`.

'''
import os
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')

JUEGO={
1 :["+-----------v       "],
2 :["|           |       "],
3 :["|                   ","|           O       "],
4 :["|                   ","|           M       ","|          \M       ","|          \M/      ","|         ^\M/      ","|         ^\M/^     "],
5 :["|                   ","|           W       "],
6 :["|                   ","|          /        ","|          / \      ","|          / \      ","|         _/ \      ","|         _/ \_     "],
7 :["+----TTTTTTTTTTTTTTT"],
8 :["                    "],}
FIN={
1:["+-----------v       "],
2:["|           |       "],
3:["|           |       "],
4:["|           0       "],
5:["|         _/M\_     "],
6:["|           W       "],
7:["+----TT\   _X_ /TTTT"],
8:["        |      |    "],}

def horca (vida):
    limpiar ()
    # ~ return
    if vida==11:
        del JUEGO[3][0]
    elif vida <=10 and vida>5:
        del JUEGO[4][0]
    elif vida ==5:
        del JUEGO[5][0]
    elif vida <=4 and vida>=1:
        del JUEGO[6][0]
    for linea in JUEGO:
        print(JUEGO[linea][0])



def juego (vida):
    #global vida
    horca (vida)

    mostrarSalida(vida)

    letra = input ("Ingrese una letra: ").lower()

    while (len(letra) > 1 and letra > "a" and letra < "z"):
        letra = input ("Ingrese una letra: ").lower()

    if (letra in DATO):
        aciertos.append(letra)
        limpiar()
    else:
        fallos.append(letra)

        vida = vida -1
        print (vida)
    return vida


def mostrarSalida (vida):
    salida =[]
    print(f"La palabra tiene {len(DATO)} letras")

    for letra in DATO:
        if (letra in aciertos):
            salida.append(letra)
        else:
            salida.append("_")

    print(*salida)
    print(f"Estas letras son incorrectas {fallos} , Teneis {vida} vidas")


palabras = ["hipopotamo","electroencefalograma","ferrocarril","locomotora","matecocido","otorrinolaringologo","abecedario"]

import random

DATO = random.choice(palabras)
aciertos = [DATO [0]]
fallos = []

vida = 12

while vida > 0 and len (set (DATO)- set (aciertos) )> 0:

    vida = juego(vida)

else:
    if vida == 0:
        limpiar ()
        for linea in FIN:
            print(FIN[linea][0])

        print ("perdiste")
    else:
        print ("ganaste")

