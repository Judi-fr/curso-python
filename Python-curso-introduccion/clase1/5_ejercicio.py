"""
Consigna: Crear un programa que solicite el nombre
y el apellido
Devolver un saludo con de la siguiente forma:
Bienvenido <apellido>, <nombre>
"""

nombre = input("Nombre: ")
apellido = input("Apellido: ")
nombre_completo = f"{apellido}, {nombre}"
print("Bienvenido", nombre_completo)
