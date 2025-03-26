# Entrada
edad = int(input("Ingresa edad: "))

# Operaciones
if edad < 0:
    mensaje = "Edad no válida"
elif edad < 13:
    mensaje = "Eres niño"
elif edad < 18:
    mensaje = "Eres adolescente"
elif edad < 65:
    mensaje = "Eres adulto"
else:
    mensaje = "Eres adulto mayor"

# Salida
print(mensaje)
