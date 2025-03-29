"""
A partir del ejercicio anterior, hacer que el programa solicite
al usuario si desea comprar más productos
Si se opta por sí, agregar ese diccionario a la lista de productos comprados.
Si se opta por no, entonces debe mostrar la compra total con sus respectivos datos
*** USAR FUNCIONES ***
"""


def comprar():
    carrito_compras = []
    while True:
        seguir_comprando = input("¿Desea comprar un producto? ('n' para salir): ")
        if seguir_comprando.lower()[0] == "n":
            break  # sale del while
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
        }
        carrito_compras.append(producto)
        continue  # opcional, ya que el while se repite automáticamente
    return carrito_compras


def listar_productos(carrito_compras: list[dict]):
    if len(carrito_compras) == 0:
        print("No hay registros para mostrar.")
        return
    print(f"\nLista de compras:")
    for producto in carrito_compras:
        print(
            f"{producto['nombre']} - Precio: ${producto['precio']} - Cantidad: {producto['cantidad']}"
        )


def main():
    carrito_compras = comprar()
    listar_productos(carrito_compras)


main()
