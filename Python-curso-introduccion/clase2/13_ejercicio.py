# Crear una lista del 0 al 5
# iterar la lista con for. Imprimir cada número.
# Si el número es 3, imprimir un mensaje de alerta

from time import sleep as dormidito

lista_numeros = [0, 1, 2, 3, 4, 5]
for numero in lista_numeros:
    dormidito(0.5)
    print(numero)
    if numero == 3:
        print("¡Alerta!")
