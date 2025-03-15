"""
Crear 4 funciones: sumar, restar, multiplicar y dividir
que impriman el resultado

Crear una lista de funciones
invocarlas con 2 números fijos (no con input)
"""


def sumar(a, b):
    print(a + b)


def restar(a, b):
    print(a - b)


def multiplicar(a, b):
    print(a * b)


def dividir(a, b):
    if b != 0:
        print(a / b)
    else:
        print("Error: No se puede dividir por cero")


def main():
    operaciones = [sumar, restar, multiplicar, dividir]
    for operacion in operaciones:
        operacion(10, 5)


main()
