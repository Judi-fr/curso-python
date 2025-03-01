# Entrada
edad = int(input("Ingresa edad: "))

# Operaciones
if edad < 0:
    mensaje = "Edad no válida"
else:
    if edad >= 18:
        mensaje = "Eres mayor de edad"
    else:
        mensaje = "Eres menor de edad"

# Salida
print(mensaje)
