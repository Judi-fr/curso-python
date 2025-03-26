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
from time import sleep

lista=[0,1,2,3,4,5]
numero=0

for listarda in lista:
    sleep(0.5)
    print(f"Numero: {listarda}")
    if numero == 3:
        print("ALERTA!")
    numero += 1    