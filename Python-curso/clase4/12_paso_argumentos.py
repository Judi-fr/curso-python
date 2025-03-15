lista_de_estudiantes = ["Marcos", "Stefani", "Felipe", "Carlos"]


def preguntar(nombre):
    return f"{nombre}, estás practicando todos los días Python?"


for estudiante in lista_de_estudiantes:
    mensaje = preguntar(estudiante)
    print(mensaje)
