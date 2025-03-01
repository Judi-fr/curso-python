"""
A partir de siguiente código:

- Poner precio a cada producto y que se muestre en el mensaje
- Crear una billetera con saldo (usar input)
- Debitar de la billetera el precio del producto seleccionado
- Mostrar el saldo restante de la billetera

presentacion = (
    "Bienvenidos a las Pastelería de la Abuela\n"
    "Menú:\n"
    "1. Tarta de Manzana\n"
    "2. Pastel de Chocolate\n"
    "3. Flan de Coco\n"
)
print(presentacion)

pedido = input("¿Qué postre desea pedir? ")

if pedido == "1":
    mensaje = "Pedido recibido: Tarta de Manzana"
elif pedido == "2":
    mensaje = "Pedido recibido: Pastel de Chocolate"
elif pedido == "3":
    mensaje = "Pedido recibido: Flan de Coco"
else:
    mensaje = f"{pedido} no está en el menú"

print(mensaje)
"""

# Declaración de variables

precio_tarta = 5
precio_pastel = 3
precio_flan = 2
mensaje = "Pedido no recibido"
saldo = float(input("¿Cuánto dinero tenés?: "))


presentacion = (
    "Bienvenidos a las Pastelería de la Abuela\n"
    "Menú:\n"
    f"1. Tarta de Manzana ${precio_tarta}\n"
    f"2. Pastel de Chocolate ${precio_pastel}\n"
    f"3. Flan de Coco ${precio_flan}\n"
)
print(presentacion)

pedido = input("¿Qué postre desea pedir? ")

if pedido == "1":
    if saldo >= precio_tarta:
        mensaje = "Pedido recibido: Tarta de Manzana"
        saldo = saldo - precio_tarta
    else:
        print("No hay saldo suficiente.")
elif pedido == "2":
    if saldo >= precio_pastel:
        mensaje = "Pedido recibido: Pastel de Chocolate"
        saldo = saldo - precio_pastel
    else:
        print("No hay saldo suficiente.")
elif pedido == "3":
    if saldo >= precio_flan:
        mensaje = "Pedido recibido: Flan de Coco"
        saldo = saldo - precio_flan
    else:
        print("No hay saldo suficiente.")
else:
    mensaje = f"{pedido} no está en el menú"

print(mensaje)
print(f"Tu saldo quedó en: ${saldo}")
