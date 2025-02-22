"""
Crea un programa que realice una suma, una resta,
multiplicación y división,
a partir de dos números ingresados por el usuario,
y luego mostrar el resultado por pantalla
"""

# Entrada
numero_1 = float(input("Ingrese el primer número: "))
numero_2 = float(input("Ingrese el segundo número: "))

# Proceso
suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2
division = numero_1 / numero_2

# Salida
print(f"{numero_1} + {numero_2} = {suma}")
print(f"{numero_1} - {numero_2} = {resta}")
print(f"{numero_1} * {numero_2} = {multiplicacion}")
print(f"{numero_1} / {numero_2} = {division}")
