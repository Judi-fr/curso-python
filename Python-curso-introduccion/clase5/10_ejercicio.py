"""
A partir del siguiente código, utilizar range() para preguntar cuántos invitados
vendrán a la fiesta.
Luego, utilizar un bucle for para preguntar el nombre de cada uno
y guardarlo en una lista. Ordenarlos alfabéticamente (opcional)
Finalmente, convertir la lista en una tupla
y mostrar la lista de invitados iterando sobre ellos

def saludar(nombre):
    print(f"¡Bienvenido {nombre}!")


lista_de_invitados = []

for invitado in lista_de_invitados:
    saludar(invitado)

"""


def saludar(nombre):
    print(f"¡Bienvenido {nombre}!")


lista_de_invitados = []
cantidad_invitados = int(input("¿Cuántos invitados vendrán a la fiesta? "))

for i in range(cantidad_invitados):
    nombre = input(f"Ingrese el nombre del invitado {i + 1}: ")
    lista_de_invitados.append(nombre)

lista_de_invitados.sort()

lista_de_invitados = tuple(lista_de_invitados)

for invitado in lista_de_invitados:
    saludar(invitado)
