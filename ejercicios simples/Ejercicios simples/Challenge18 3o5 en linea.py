
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

class Tres_en_linea: 

    def __init__(self): 
        self.ventana = tk.Tk()
        self.ventana.geometry("600x600")
        self.crear_windows()


        
    def crear_windows(self):
        self.jugador=True
        self.jugando=False
        self.matriz_juego=[]
        self.matriz_botones=[]

        self.etiqueta= tk.Label(text=f"Jugador 1",bg="#FF0000")
        self.etiqueta.place(x=200, y=75, width=150,height=25)
        self.boton3x3=tk.Button(text='3 x 3',command=lambda : self.tipo(3))
        self.boton3x3.place(x=200, y=125, width=75,height=25)
        self.boton5x5=tk.Button(text='5 x 5',command=lambda : self.tipo(5))
        self.boton5x5.place(x=275, y=125, width=75,height=25)
        self.frame= tk.Frame(self.ventana)
        self.frame.place(x=125, y=175, width=325,height=450)
        self.salir=tk.Button(self.frame,text='salir',command=exit)
        self.salir.place(x=225, y=300, width=75,height=25)
        self.ventana.mainloop()
    def tipo(self,cant):
        del self.matriz_juego
        del self.matriz_botones
        self.boton3x3.destroy()
        self.boton5x5.destroy()
        self.frame.destroy()
        self.frame= tk.Frame(self.ventana)
        self.frame.place(x=125, y=175, width=325,height=450)
        self.salir=tk.Button(self.frame,text='reiniciar',command=self.crear_windows)
        self.salir.place(x=225, y=300, width=75,height=25)
        self.cantidad=int(cant)
        self.matriz_juego  =[[f"{chr(65+columnas)}{fila+1}" for columnas in range(0,self.cantidad) ] for fila in range(0,self.cantidad) ]
        self.matriz_botones=[["" for columnas in range(0,self.cantidad) ] for fila in range(0,self.cantidad) ]
        # ~ print(f"{self.matriz_juego}")
        # ~ print(f"{self.matriz_botones}")
        self.inicioX=0 if self.cantidad==5 else 50
        self.jugando=True
        self.crear_tablero()
    def crear_tablero(self):
        for columna in range(0,self.cantidad):
            for fila in range(0,self.cantidad):
                self.matriz_botones[fila][columna]=tk.Button(self.frame,text=f"{chr(65+columna)}{fila+1}", command=  functools.partial(self.jugar,(f"{chr(65+columna)}{fila+1}")))
                self.matriz_botones[fila][columna].place(x=25+self.inicioX+(columna*50),y=0+(fila*50), width=50,height=50)
    def jugar(self,ubicacion):
        if self.jugando is True:
            c,f =list(ubicacion)
            self.columna=ord(c)-65#codigo ASCII de la 'A' es 65, 'B' es 66,  'C' es 67
            self.fila=int(f)-1          
            # ~ print( f"{self.columna=}\t{self.fila=}")
            # ~ print (self.matriz_juego)
            if self.matriz_juego[self.fila][self.columna]==ubicacion:
                self.jugada="X" if self.jugador is True else "0"
                self.matriz_juego[self.fila][self.columna]=self.jugada
                self.matriz_botones[self.fila][self.columna].config(text=self.jugada,bg="#FF0000" if self.jugador is True else "#0000FF")
                regreso=self.chequear()
                if regreso is False:
                    self.jugador=not self.jugador
                    texto='Jugador 1' if self.jugador is True else 'Jugador 2'
                    color="#FF0000" if self.jugador is True else "#0000FF"
                    self.etiqueta.config(text=texto,bg=color)

            # ~ else:
            # ~ print ("error, ubicacion ya jugada")
             
    def chequear(self):
        # ~ print (self.matriz_juego)
        estado=False
        suma_diag1=0
        suma_diag2=0
        libres=0
        for fila in range(0,self.cantidad):
            suma_fila=0
            suma_col=0

            for columna in range(0,self.cantidad):
                # ~ print( f'{ self.matriz_juego[fila][columna]=}')
                suma_fila =suma_fila + 1 if self.matriz_juego[fila][columna]==self.jugada else 0
                suma_col  =suma_col  + 1 if self.matriz_juego[columna][fila]==self.jugada else 0
                if self.matriz_juego[fila][columna] not in ["X","0"]:
                    libres+=1
                
            if suma_fila==self.cantidad or suma_col==self.cantidad:
                self.gano()
                return True
            suma_diag1=suma_diag1+ 1 if self.matriz_juego[fila][fila]==self.jugada else 0
            suma_diag2=suma_diag2+ 1 if self.matriz_juego[fila][self.cantidad-1-fila]==self.jugada else 0      
        # ~ print (f"{suma_diag1=}")
        # ~ print (f"{suma_diag2=}")
        if suma_diag1==self.cantidad or suma_diag2==self.cantidad:
            self.gano()
            return True
            
        if libres==0:
            self.jugando=False
            self.jugador=""
            self.gano()
            return True
        return False
    def gano(self):
        self.jugando=False
        texto=f"Ganador {'Jugador 1' if self.jugador is True else  'Jugador 2' if self.jugador is False else 'Empate' }"
        color="#FF0000" if self.jugador is True else  "#0000FF" if self.jugador is False else '#00FF00'
        self.etiqueta_ganador_=tk.Label(self.frame,text=texto, bg=color)
        # ~ self.etiqueta_ganador.config( bg=fondo)
        self.etiqueta_ganador_.place(x=75, y=250, width=150,height=25)
        self.etiqueta.destroy()
        self.continuar=tk.Button(self.frame,text='continuar',command=self.crear_windows)
        self.continuar.place(x=0, y=300, width=75,height=25)
        self.salir=tk.Button(self.frame,text='salir',command=exit)
        self.salir.place(x=225, y=300, width=75,height=25)
        
        
        
        # ~ print(sum([1 if self.matriz_juego[self.fila][self.columna]==self.jugada else 0 for fila in range(0,self.cantidad) for columna in range(0,self.cantidad)]))
        # ~ if sum([1 if self.matriz_juego[self.fila][self.columna]==self.jugada else 0 for fila in range(0,self.cantidad) for columna in range(0,self.cantidad)]) ==3:
            # ~ print ('gano')
                
                
                
                
print("*"*50)
obj = Tres_en_linea()

