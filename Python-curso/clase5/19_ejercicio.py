"""
=========
EJERCICIO
=========
Solicitar al usuario datos sobre un producto:
    - nombre
    - precio
    - cantidad
Guardar en un diccionario y mostrar en la consola:
"El producto < > cuesta $< > y su stock es < >."
"""

# Entrada

nombre_producto = input("Ingrese el nombre del producto: ")
precio_producto = float(input("Ingrese el precio del producto: "))
cantidad_producto = int(input("Ingrese la cantidad del producto: "))

# Estructura de datos
producto = {
    "nombre": nombre_producto,
    "precio": precio_producto,
    "cantidad": cantidad_producto,
}

# Salida
print(
    f"El producto {producto['nombre']} cuesta ${producto['precio']} y su stock es {producto['cantidad']}."
)
