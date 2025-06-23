"""lista = [1,2,3,4,5,6,7,8,7]
suma = (lambda lista: (lista.pop(), sum(lista)))
print(lista)
ultimo,sumita=suma(lista)
print(lista)
print(f"el numero eliminado fue el {ultimo}, la suma sin el es de {sumita}")
"""

"""
lista = [1,2,3,4,5,6,7,8,7]

inpares = [numero for numero in lista if numero % 2 != 0]

print(inpares)

"""
"""
opcion = input("desea ver la lista? (s/n) ").upper()
print(opcion)
lista = [1,2,3,4,5,6,7,8,9]

while opcion[0]=="S":
    for x in range(len(lista)):
        print(lista)
        print(f"Borro el {lista[0]}")
        lista.pop(0)
                

    opcion="N"

print(lista)

"""
"""
def fib(tam):
    if tam <2:
        print("La cantidad debe ser mayor a 2")
        return
    
    lista =[0,1]

    for x in range(2,tam):
        c=lista[x-1]+lista[x-2]
        lista.append(c)


    return lista

print(fib(1))"""

"""
resultado = [x for x in range(50) if x % 3 == 0]

print(resultado)
"""
"""palabras = ["auto", "barco", "isla", "elefante", "tren", "oso", "nube"]

inicia_con_vocal=[x for x in palabras if x[0] in "aeiou"]

print(inicia_con_vocal)"""

"""palabras = ["auto", "barco", "isla", "elefante", "tren", "oso", "nube"]

vocales =[palabra for palabra in palabras if palabra[0] in "aeiou" and len(palabra) >= 4 ]

print(vocales)"""


#A RESOLVEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEER
"""precios = ["100", "250", "399", "149"]

resultado=list(map(lambda precio: round(int(precio)*1.21 ,2),precios))

print(resultado)"""

"""palabras = ["árbol", "sol", "mariposa", "luz", "nube", "montaña"]

consonantes = list(filter(lambda x: x[0] in "tsbvf" and len(x) < 4 , palabras))

print(consonantes)"""

"""numeros = [10, 15, 21, 30, 41, 50]

resultado = list(map(lambda x: str(x) +" pts",filter(lambda x: x > 10, numeros)))
print(resultado)
""""""

lista = ["2", "4", "6", "8"]

lista=list(map(lambda x: int(x)*2,lista))

print (lista)

palabras = ["python", "", "map", "", "filter", "lambda"]

palabras = list(filter(lambda x: len(x)>0, palabras ))

print(palabras)
"""
#_____________________________________________________________________________
"""primera = [7, 5, 10, 9, 8, 1, 3, 5, 6, 3, 8, 0, 10, 9, 2]
segunda = [6, 9, 3, 7, 9, 10, 5, 10, 7, 4, 5, 3, 2, 10, 2]
tercera=[]

lista = list(filter(lambda x: x in segunda, primera))
print(lista)
for x in lista:
    if x not in tercera:
        tercera.append(x) 
print(tercera)"""
#______________________________________________________________________________
"""
personas = ["Susana","Tamara","Ana","Susana","Susana","Tomas","Ana","Hernesto","estebanquito","armando","armando","tomas","Tomas"]
diccionario={}

for persona in personas:
    if persona in diccionario:
        diccionario[persona]+=1
    else:
        diccionario[persona]=1

print(diccionario)"""

"""
def conversion(segundos):
    
    minutos=segundos//60
    segundos=segundos%60
    horas=minutos//60
    minutos=minutos%60

    print(f"{horas}:{minutos}:{segundos}")

conversion(15491)

"""
"""cubo=lambda x: x**2
lista=[1,2,3,4,5,6,7,8,9]
nueva_lsita=[]
def superior(funcion,lista):
    for num in lista:
        nueva_lsita.append(funcion(num))
    
superior(cubo,lista)
print(nueva_lsita)
"""
"""def operaciones(a,b):
    suma=lambda a,b:a+b
    resta=lambda a,b: a-b
    multiplicacion=lambda a,b:a*b
    if b is not 0:
        division=lambda a,b:a/b
        return suma(a,b), resta(a,b), multiplicacion(a,b), division(a,b)
    else: 
        print("No enviaremos la division, no se puede dividir por 0")
        return suma(a,b), resta(a,b), multiplicacion(a,b), 0"""
"""
bool=True

while(bool==True):
    try:
        num1=int(input("Primer numero: "))
        num2=int(input("Segundo numero: "))
    except:
        print()
        print("Los strings no son numeros, vuelve a ingresarlos")
        print()
        continue
    a,b,c,d=operaciones(num1,num2)
    print(f"suma: {a}, resta: {b}, multiplicacion: {c}, division: {d}")
    bool=False
    """

print("Fin do programa, porra 🐱‍🏍")
"""
paises = {
 "ar": "Argentina",
 "es": "España",
 "us": "Estados Unidos",
 "fr": "Francia"
}

def recorrerDicc(x):
    try:
        print(f"{x} : {paises[x]}")
    except:
        print("no esta el pais bobalicon")


paises = {
 "ar": "Argentina",
 "es": "España",
 "us": "Estados Unidos",
 "fr": "Francia"
}

x=input("ingreso: ")
recorrerDicc(x)
""""""
lista=["juan salvo","henry courtney","elizabeth bennet","marge simpson"]

nueva_lista=list(map(lambda x: x.title(), lista))

print(nueva_lista)

import os
def limpiar():
    os.system("cls" if os.name in ("nt","ce","dos") else "clear")

from functools import reduce
"""
"""class Solution(object):
    def twoSum(self, nums, target):
       for i in range(len(nums)):
           for j in range(i+1,len(nums)):
               if nums[i] + nums[j] == target:
                   return i, j
        

Numeros=[]
while(True):
    entrada=input("Ingrese un numero (termina ingreso con 0) ")
    try:
        numero = int(entrada)
        if numero == 0:
            break
        Numeros.append(numero)
    except:
        print("error")

target=int(input("ingresa el target "))

sol = Solution()
Numeros=sol.twoSum(Numeros,target)
print(Numeros)
"""
"""
f = open("Archive.txt", "w")
f.write("so un capo pibe, lo lograste campeon, champion of the wor, ")

with open("Archive.txt", "r") as p:
    texto=p.read()

print(texto)

f.close()

with open("Archive.txt", "a") as f:
    f.write("ueeepa lo volvite a abri, y ensima a escribi, ai can beliv, ai can flai, ai can touch the skai, nigga")
    f.close()

with open("Archive.txt", "r") as p:
    texto=p.read()

p.close()

print(f"\a{texto}")"""

import from 
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def nombre_completo(self):
        print(f"{self.nombre} {self.apellido}")

class Estudiante(Persona):
    def setCarrera(self,carrera):
        self.carrera = carrera
    def mostrar(self):
        print(f"{self.nombre} {self.apellido} {self.carrera}")
#p = Persona("ezequiel","rieznik")
e = Estudiante("ezequielito","reiznik")
e.setCarrera("bostero")
e.nombre_completo()
e.mostrar()
