"""edad=int(input("ingrese edad: "))
print(edad)

edad=int(input("ingresa "))"""
"""
dinero=float(input("ingrese la cantidad de dinero disponible:\n"))
print("los postres que hay en el menu son:\n 1.cheesecake 3$\n 2.flan 1$\n 3.cafe 2$\n ")
eleccion=input(f"cual eligiras?\n")

if eleccion == "flan":
    mensaje="anotado un flan!"
    dinero = dinero - 1

elif eleccion == "cheesecake":
    mensaje="anotado un cheesecake"
    dinero = dinero - 3
    
elif eleccion == "cafe":
    mensaje="sale un cafesito"
    dinero = dinero - 2
else:
    mensaje="ese postre no forma parte de la carta"

print(mensaje)
if dinero >=0:
    print(f"dinero restante ${dinero}")
else:
    print("no te alcanza el dinero para hacer esta compra")

"""
"""
from time import sleep

lista=[0,1,2,3,4,5]
numero=0

for listarda in lista:
    sleep(0.5)
    print(f"Numero: {listarda}")
    if numero == 3:
        print("ALERTA!")
    numero += 1
"""
"""edad = int(input("ingrese su edad:",))
mensaje = "edad invalida"

if edad >= 18:
    mensaje="Eres mayor de edad"

elif edad >= 65:
    mensaje = "Eres un anciano"

elif edad > 0:
    mensaje = "Eres menor de edad"

print(mensaje)
"""

"""
numero_1 = int(input("Dame un numero: "))

if numero_1 % 2 == 0 and numero_1 % 3 == 0:
    print("el numero es divisible por 2 y 3")

"""

"""
lista = ["eze","wenchi","fausto","mate","facundo"]
lista.append("ivan")
lista.remove(lista[2])

print(lista)
"""

"""
nombre1 = int(input("1. Numero: "))
nombre2 = int(input("2. Numero: "))
nombre3 = int(input("3. Numero: "))
nombre4 = int(input("4. Numero: "))
nombre5 = int(input("5. Numero: "))

lista = [nombre1, nombre2, nombre3, nombre4, nombre5]

print(lista)
"""
"""
lista = []

for i in range(5):
    num = int(input(f"Ingresa el {i+1} numero: "))
    lista.append(num)

lista.sort()

print(lista)





Pide al usuario que ingrese 7 números y guárdalos en una lista.
Indica cuántos de esos números son pares y cuántos son impares.
Muestra solo los números que son divisibles por 2 y 3 al mismo tiempo.
Ordena la lista de menor a mayor y muéstrala.
"""
lista = []
divisible = []
i = 0

for i in range(7):
    numero = int(input(f"ingrese el {i+1} numero: "))
    lista.append(numero)
    if lista[i] % 2 == 0 and lista[i] % 3 == 0:
        divisible.append(lista[i])

pares = list(filter(lambda x: x % 2 == 0, lista))
inpares = list(filter(lambda x: x % 2 != 0, lista))

print(pares)
print(inpares)
print(f"Cantidad de numeros pares: {len(pares)}")
print(f"Cantidad de numeros inpares: {len(inpares)}")
print(f"los numeros divisibles por 2 y 3: {divisible}")

