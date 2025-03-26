# Entrada
edad = int(input("Ingresa edad: "))

# Operaciones
if edad < 0:
    mensaje = "Edad no válida"
else:
    if edad < 13:
        mensaje = "Eres niño"
    else:
        if edad < 18:
            mensaje = "Eres adolescente"
        else:
            if edad < 65:
                mensaje = "Eres adulto"
            else:
                mensaje = "Eres adulto mayor"

# Salida
print(mensaje)
