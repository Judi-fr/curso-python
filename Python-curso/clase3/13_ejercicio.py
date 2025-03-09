"""
Modificar el código para que:
- Si el usuario no llega a ingresar un número válido, se vuelve a
solicitar la entrada de datos

tabla = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultados = []

entrada = input("Dame un número y te daré su tabla de multiplicación: ")

caso_positivo = entrada.isdecimal()
caso_negativo = entrada[0] == "-" and entrada[1:].isdecimal()


if caso_positivo or caso_negativo:
    numero = int(entrada)
    for i in tabla:
        multiplicacion = i * numero
        resultados.append(multiplicacion)
else:
    print("No has ingresado un número")


print(tabla)
print(resultados)
"""

tabla = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultados = []

while True:
    entrada = input("Dame un número y te daré su tabla de multiplicación: ")
    if entrada == "":
        continue
    caso_positivo = entrada.isdecimal()
    caso_negativo = entrada[0] == "-" and entrada[1:].isdecimal()
    if caso_positivo or caso_negativo:
        break
    else:
        print("No has ingresado un número")
        continue

numero = int(entrada)
for i in tabla:
    multiplicacion = i * numero
    resultados.append(multiplicacion)

print(tabla)
print(resultados)
