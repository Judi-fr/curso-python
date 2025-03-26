def obtener_cantidad_invitados():
    while True:
        invitados = input("¿Cuántos invitados vendrán a la fiesta? ")
        if not invitados.isdigit():
            print("Por favor, ingrese un número válido.")
            continue
        else:
            return int(invitados)


def crear_lista_invitados(cantidad):
    lista_invitados = []
    for i in range(cantidad):
        nombre = input(f"Ingrese el nombre del invitado {i + 1}: ")
        lista_invitados.append(nombre)
    lista_invitados.sort()
    return tuple(lista_invitados)


def saludar_invitados(lista_invitados):
    for invitado in lista_invitados:
        print(f"¡Bienvenido {invitado}!")


def main():
    cantidad_invitados = obtener_cantidad_invitados()
    lista_de_invitados = crear_lista_invitados(cantidad_invitados)
    saludar_invitados(lista_de_invitados)


main()
