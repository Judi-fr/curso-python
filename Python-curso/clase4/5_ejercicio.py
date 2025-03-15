"""
A partir del siguiente código, llevar la pregunta a una nueva función.
Crear otra función principal que llame a preguntar_nombre y luego
a saludar_con_nombre

def saludar_con_nombre(nombre):
    print(f"¡Hola {nombre}!")


nombre = input("Dime tu nombre: ")
saludar_con_nombre(nombre)
"""


def saludar_con_nombre(nombre):
    print(f"¡Hola {nombre}!")


def preguntar_nombre():
    nombre = input("Dime tu nombre: ")


def main():
    preguntar_nombre()
    saludar_con_nombre(nombre)


main()
