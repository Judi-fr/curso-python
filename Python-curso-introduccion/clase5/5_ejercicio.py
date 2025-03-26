"""
Ejercicio con funciones con parámetros predeterminados
Crear una función dividir que reciba dos parámetros, uno opcional y otro obligatorio,
y devuelva el resultado de la división de ambos. Si se pasa un solo argumento,
dividir / 1.
"""


def dividir(dividendo, divisor=1):
    return dividendo / divisor


print(dividir(10, 2))
print(dividir(12))  # ✨
