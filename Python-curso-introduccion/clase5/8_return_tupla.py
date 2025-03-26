def operar(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division


def main():
    resultado = operar(10, 5)
    suma, resta, multiplicacion, division = resultado
    print(suma)
    print(resta)
    print(multiplicacion)
    print(division)


main()
