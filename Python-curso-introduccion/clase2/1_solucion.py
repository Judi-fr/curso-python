"""
Ejercicio:
Pedir al usuario su edad.
Si es mayor o igual a 18, imprimir "eres mayor de edad"
De lo contrario, imprimir "eres menor de edad"
"""

# Entrada
edad = int(input("Ingresa edad: "))

# Operaciones
if edad >= 18:
    mensaje = "Eres mayor de edad"
else:
    mensaje = "Eres menor de edad"

# Salida
print(mensaje)
