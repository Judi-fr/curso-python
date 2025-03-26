"""
Crear una función que reciba una cadena y devolver la cadena convertida en mayúsculas
y mostrar el resultado fuera de la función.

Si el resultado es una cadena vacía, mostrar un mensaje indicando que la cadena está vacía.
De lo contrario, mostrar la cadena.
"""


def convertir_mayúsculas(cadena):
    return cadena.upper()


entrada = input("Escribe algo > ")
devolucion = convertir_mayúsculas(entrada)

if devolucion == "":
    print("La cadena está vacía")
else:
    print(devolucion)
