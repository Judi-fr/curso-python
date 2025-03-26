"""
Dada la siguiente lista:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Crear una función que imprima los cuadrados de cada número de la lista
"""


def imprimir_cuadrados():
    for numero in lista:
        cuadrado = numero**2
        print(f"El cuadrado de {numero} es {cuadrado}")


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

imprimir_cuadrados()
