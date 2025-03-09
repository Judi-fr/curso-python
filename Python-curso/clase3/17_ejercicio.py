"""
A partir de la siguiente lista, aumentar el precio de cada producto un 10%
y mostrar el resultado en pantalla:

lista_sublistas_producto_precio = [
    ["vaso", 100],
    ["plato", 200],
    ["tenedor", 300],
    ["cuchara", 400],
    ["cuchillo", 500],
]
"""

lista_sublistas_producto_precio = [
    ["vaso", 100],
    ["plato", 200],
    ["tenedor", 300],
    ["cuchara", 400],
    ["cuchillo", 500],
]

for sublista in lista_sublistas_producto_precio:
    precio = sublista[1]
    precio_aumentado = precio * 1.10
    sublista[1] = round(precio_aumentado, 2)
print(lista_sublistas_producto_precio)

lista_precios_aumentados = []
for producto, precio in lista_sublistas_producto_precio:
    precio_aumentado = round(precio * 1.10, 2)
    lista_precios_aumentados.append([producto, precio_aumentado])

print(lista_precios_aumentados)
