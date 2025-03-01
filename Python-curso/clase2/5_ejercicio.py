"""
Ejercicio:

Crear un programa que muestre 3 postres como menú.
El usuario debe escribir uno.
Si el nombre coincide con el menú, imprimir "Pedido recibido",
de lo contrario, imprimir "<tal cosa> no está en el menú"
"""

print("Menú:")
print("1. Tiramisú")
print("2. Flan")
print("3. Helado")
pedido = input("Ingresa tu pedido: ")

if pedido == "1":
    print("Pedido recibido: Tiramisú")
elif pedido == "2":
    print("Pedido recibido: ")
elif pedido == "3":
    print("Pedido recibido")
else:
    print("Lo siento, no está en el menú")
