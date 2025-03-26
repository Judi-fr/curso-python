"""
Crear tres funciones:
a) Una que imprima "¡Bienvenido!"
b) Otra que imprima "¡Adiós!".
c) Una tercera función llame a las dos funciones anteriores.

Debes invocar (o llamar) solamente a la tercera función
para que se ejecuten las dos primeras.
"""

a = 1000


def dar_bienvenida():
    print("Bienvenido!")


def dar_despedida():
    print("Adiós!")


def principal():
    dar_bienvenida()
    dar_despedida()


principal()
