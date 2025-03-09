cadena = "1234567890"
if cadena.isdecimal():
    print("La cadena es un número decimal")
else:
    print("La cadena no es un número decimal")

cadena = "-1234567890"
if cadena.isdecimal():
    print("La cadena es un número decimal")
else:
    print("La cadena no es un número decimal")

entrada = input("Ingrese un número: ")
if entrada.isdecimal():
    numero = int(entrada)
    print(f"Has introducido el número: {numero}")
else:
    print("La entrada no es un número decimal")
