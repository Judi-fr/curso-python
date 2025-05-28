
from __init__ import *
'''
DESAFIO N~''40
 * TRIÁNGULO DE PASCAL
 * Dificultad: MEDIA
 *
 * Enunciado: Crea una función que sea capaz de dibujar el "Triángulo de Pascal" indicándole
 * únicamente el tamaño del lado.
 * - Aquí puedes ver rápidamente cómo se calcula el triángulo:
 *   https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif
'''








class Dibujos:
    def __init__(self):
        pass 

    def make_consola(self):
        lado =""
        #no anda   >while  int(lado) <3 or lado.isdigit() is False
        while lado.isdigit() is False or int(lado) <3 or int(lado) >50:
            lado = input ("por favor ingrese el largo del lado ( entre 3 y 50):")
        # ~ self.lado= int(lado)       
        self.construir(int(lado))
    def make_windows(self):
        pass
    def construir(self,lado):
        
        if not isinstance(self, (TrianguloPascal,RomboPascal,CuboPascal)):
            print (f"no tengo ganas {lado} son muchos para un dia de enero")
        elif isinstance(self, TrianguloPascal):
            print ("*".center(99))#  pos 0
            for vertice in range (1,lado-1,1):
                salida = f"*{' '*(vertice*2-1)}*"
                print (f"{salida.center(99)}")
            print (f"{('* '*lado).center(99)}")

        elif isinstance(self, RomboPascal):
            print ("*".center(99))#  pos 0
            for vertice in range (1,lado,1):
                salida = f"*{' '*(vertice*2-1)}*"
                print (f"{salida.center(99)}")
            for vertice in range (lado-1,0,-1):
                salida = f"*{' '*(vertice*2-1)}*"
                print (f"{salida.center(99)}")
            print ("*".center(99))
            
        elif isinstance(self, CuboPascal):
            print (f"{('* '*lado).center(99)}")
            for vertice in range (1,lado-1,1):
                salida = f"*{' '*(lado*2-3)}*"
                print (f"{salida.center(99)}")
            print (f"{('* '*lado).center(99)}")
        input ("\t\tEnter para continuar.......... ")
    def __str__ (self):
        return "soy simplemente un dibujo caprichoso"
                        
class TrianguloPascal(Dibujos):
    def __str__ (self):
        return "soy un Triangulo"

class RomboPascal(Dibujos):
    def __str__ (self):
        return "soy un Rombo"
class CuboPascal(Dibujos):
    def __str__ (self):
        return "soy un Cubo"
def salir():
    exit()

dic_obj={" ":Dibujos,"T":TrianguloPascal,"R":RomboPascal,"C":CuboPascal,"S":salir}
opcion = ""
while opcion != 'S':
    while opcion not in dic_obj.keys() : 
        limpiar()
        opcion = input(f"""
Que desea dibujar:
    T) para triangulos
    R) para rombos
    C) para cubos
    S) para Salir """).upper()
    if opcion != "S":

        obj = dic_obj[opcion]()
        print (f"{obj}")
        obj.make_consola()  
        opcion=""     
    elif opcion == "S":
        salir()

exit()
# ~ funcion_triangulo_de_Pascal(5)
# ~ funcion_triangulo_de_Pascal(1)
# ~ funcion_triangulo_de_Pascal(0)
# ~ funcion_triangulo_de_Pascal(-5)
# ~ funcion_triangulo_de_Pascal(10)
# ~ funcion_triangulo_de_Pascal(11)
# ~ funcion_triangulo_de_Pascal(12)
# ~ funcion_triangulo_de_Pascal(20)


# ~ exit()
def funcion_triangulo_de_Pascal(size) :
    if size<2:
        print ("imposible")
        return
    print ("*".center(100))
    for row in range(2, size):
        print ("*".rjust(51-row)+"*".rjust((row-1)*2))
    print (("* "*size).center(100))


funcion_triangulo_de_Pascal(5)
funcion_triangulo_de_Pascal(1)
funcion_triangulo_de_Pascal(0)
funcion_triangulo_de_Pascal(-5)
funcion_triangulo_de_Pascal(10)
funcion_triangulo_de_Pascal(11)
funcion_triangulo_de_Pascal(12)
funcion_triangulo_de_Pascal(20)
