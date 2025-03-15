"""
Crear una lista de invitados.
A cada uno saludarlo de la misma forma, pero personalizando el saludo con su nombre.
"""


def saludar_invitado(nombre):
    print(f"Hola {nombre}, te doy la bienvenida a la conferencia")


def main():
    lista_de_invitados = ["Marcos", "Stefani", "Felipe", "Carlos"]
    for invitado in lista_de_invitados:
        saludar_invitado(invitado)


main()
