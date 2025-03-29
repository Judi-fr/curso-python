"""
A partir del siguiente código, crear un carrito de compras,
donde se irán agregando los productos (diccionarios)
que el usuario vaya ingresando.
Preguntar cuántos productos quiere ingresar (for range o while)
Ver la lista de compras.

nombre = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad del producto: "))
producto = {
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad,
}
print(
    f"El producto {producto['nombre']} cuesta ${producto['precio']} y su stock es {producto['cantidad']}."
)
"""

carrito_compras = []

cantidad_productos = int(input("¿Cuántos productos desea agregar al carrito?: "))

for i in range(cantidad_productos):
    print(f"\nProducto {i + 1}:")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
    }
    carrito_compras.append(producto)

print(f"\nLista de compras:")
for producto in carrito_compras:
    print(
        f"{producto['nombre']} - Precio: ${producto['precio']} - Cantidad: {producto['cantidad']}"
    )
