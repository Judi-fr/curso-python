
'''
DESAFIO N~'18
 * TRES EN LINEA
 * Dificultad: DIFÍCIL
 *
 Enunciado: Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
  - "X" si han ganado las "X"
  - "O" si han ganado los "O"
  - "Empate" si ha habido un empate
  - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. O si han ganado los 2.
 Nota: La matriz puede no estar totalmente cubierta. Se podría representar con un vacío "", por ejemplo.
'''



import functools
import tkinter as tk
from tkinter import ttk

print ("Tres_en_linea")


def crear_windows():
    global ventana
    global frame
    global boton3x3
    global boton5x5
    global matriz_juego
    global matriz_botones
    # ~ global boton5x5
    # ~ global boton5x5
    jugador=True
    jugando=False
    matriz_juego=[]
    matriz_botones=[]

    etiqueta= tk.Label(text=f"Jugador 1",bg="#FF0000")
    etiqueta.place(x=200, y=75, width=150,height=25)
    boton3x3=tk.Button(text='3 x 3',command=lambda : tipo(3))
    boton3x3.place(x=200, y=125, width=75,height=25)
    boton5x5=tk.Button(text='5 x 5',command=lambda : tipo(5))
    boton5x5.place(x=275, y=125, width=75,height=25)
    frame= tk.Frame(ventana)
    frame.place(x=125, y=175, width=325,height=450)
    salir=tk.Button(frame,text='salir',command=exit)
    salir.place(x=225, y=300, width=75,height=25)
    ventana.mainloop()
def tipo(cant):
    global salir
    global frame
    global cantidad
    global matriz_juego
    global matriz_botones
    global inicioX
    global jugando
    boton3x3.destroy()
    boton5x5.destroy()
    frame.destroy()
    frame= tk.Frame(ventana)
    frame.place(x=125, y=175, width=325,height=450)
    salir=tk.Button(frame,text='reiniciar',command=crear_windows)
    salir.place(x=225, y=300, width=75,height=25)
    cantidad=int(cant)
    matriz_juego  =[[f"{chr(65+columnas)}{fila+1}" for columnas in range(0,cantidad) ] for fila in range(0,cantidad) ]
    matriz_botones=[["" for columnas in range(0,cantidad) ] for fila in range(0,cantidad) ]
    # ~ print(f"{matriz_juego}")
    # ~ print(f"{matriz_botones}")
    inicioX=0 if cantidad==5 else 50
    jugando=True
    crear_tablero()
def crear_tablero():
    for columna in range(0,cantidad):
        for fila in range(0,cantidad):
            matriz_botones[fila][columna]=tk.Button(frame,text=f"{chr(65+columna)}{fila+1}", command=  functools.partial(jugar,(f"{chr(65+columna)}{fila+1}")))
            matriz_botones[fila][columna].place(x=25+inicioX+(columna*50),y=0+(fila*50), width=50,height=50)
def jugar():

    if jugando is True:
        c,f =list(ubicacion)
        columna=ord(c)-65#codigo ASCII de la 'A' es 65, 'B' es 66,  'C' es 67
        fila=int(f)-1
        # ~ print( f"{columna=}\t{fila=}")
        # ~ print (matriz_juego)
        if matriz_juego[fila][columna]==ubicacion:
            jugada="X" if jugador is True else "0"
            matriz_juego[fila][columna]=jugada
            matriz_botones[fila][columna].config(text=jugada,bg="#FF0000" if jugador is True else "#0000FF")
            regreso=chequear()
            if regreso is False:
                jugador=not jugador
                texto='Jugador 1' if jugador is True else 'Jugador 2'
                color="#FF0000" if jugador is True else "#0000FF"
                etiqueta.config(text=texto,bg=color)

        # ~ else:
        # ~ print ("error, ubicacion ya jugada")

def chequear():
    # ~ print (matriz_juego)
    estado=False
    suma_diag1=0
    suma_diag2=0
    libres=0
    for fila in range(0,cantidad):
        suma_fila=0
        suma_col=0

        for columna in range(0,cantidad):
            # ~ print( f'{ matriz_juego[fila][columna]=}')
            suma_fila =suma_fila + 1 if matriz_juego[fila][columna]==jugada else 0
            suma_col  =suma_col  + 1 if matriz_juego[columna][fila]==jugada else 0
            if matriz_juego[fila][columna] not in ["X","0"]:
                libres+=1

        if suma_fila==cantidad or suma_col==cantidad:
            gano()
            return True
        suma_diag1=suma_diag1+ 1 if matriz_juego[fila][fila]==jugada else 0
        suma_diag2=suma_diag2+ 1 if matriz_juego[fila][cantidad-1-fila]==jugada else 0
    # ~ print (f"{suma_diag1=}")
    # ~ print (f"{suma_diag2=}")
    if suma_diag1==cantidad or suma_diag2==cantidad:
        gano()
        return True

    if libres==0:
        jugando=False
        jugador=""
        gano()
        return True
    return False
def gano():
    jugando=False
    texto=f"Ganador {'Jugador 1' if jugador is True else  'Jugador 2' if jugador is False else 'Empate' }"
    color="#FF0000" if jugador is True else  "#0000FF" if jugador is False else '#00FF00'
    etiqueta_ganador_=tk.Label(frame,text=texto, bg=color)
    # ~ etiqueta_ganador.config( bg=fondo)
    etiqueta_ganador_.place(x=75, y=250, width=150,height=25)
    etiqueta.destroy()
    continuar=tk.Button(frame,text='continuar',command=crear_windows)
    continuar.place(x=0, y=300, width=75,height=25)
    salir=tk.Button(frame,text='salir',command=exit)
    salir.place(x=225, y=300, width=75,height=25)



    # ~ print(sum([1 if matriz_juego[fila][columna]==jugada else 0 for fila in range(0,cantidad) for columna in range(0,cantidad)]))
    # ~ if sum([1 if matriz_juego[fila][columna]==jugada else 0 for fila in range(0,cantidad) for columna in range(0,cantidad)]) ==3:
        # ~ print ('gano')




print("*"*50)
ventana = tk.Tk()
ventana.geometry("600x600")
crear_windows()

