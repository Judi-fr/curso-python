""" 

"""
nombres = [
    "Juan", "María", "Pedro", "Ana", "Luis", "Carmen", "José", "Laura",
    "Miguel", "Sofía", "Carlos", "Elena", "Fernando", "Lucía", "Javier",
    "Marta", "Alberto", "Isabel", "Raúl", "Patricia"
]
import random
# ~ A) Crear diccionario con nombre desde la lista y nota1 y nota2. estas son valores aleatorias entre 1 y 100.
estudiantes = {nombre: 
                    {
                    "nota1": random.randint(1, 100), 
                    "nota2": random.randint(1, 100)
                    } for nombre in nombres
                } 
print (f"{estudiantes=}")
"""
importar el módulo random: Para generar números aleatorios.
Definir una lista de nombres: Contiene 20 nombres de personas en español.
Crear el diccionario:
Utiliza una comprensión de diccionario para iterar sobre cada nombre en la lista nombres.
Para cada nombre, genera un diccionario con dos claves: "nota1" y "nota2", con valores que son números aleatorios entre 1 y 100.
Imprimir el diccionario: Muestra el resultado del diccionario creado.
"""
estudiantes = {nombre: 
                    {
                    **notas,
                    "promedio": (notas["nota1"] + notas["nota2"]) / 2
                    } for nombre, notas in estudiantes.items()
                } 

print (f"{estudiantes=}")
"""
estudiantes = {nombre:
                    {
                    **notas,
                    "promedio": ……………………,
                    } for nombre, notas in estudiantes.items()
                }  
"""
# Crear listas de estudiantes según su promedio
# Crear listas nombre para cada categoría ordenado por  alfabeticamente
reprobados=sorted([nombre for nombre, notas in estudiantes.items() if notas["promedio"] <= 40])
a_recuperatorio=sorted([nombre for nombre, notas in estudiantes.items() if 40 < notas["promedio"] <= 60])
aprobados=sorted( [nombre for nombre, notas in estudiantes.items() if notas["promedio"] > 60])

print("Reprobados:", reprobados)
print("Recuperatorio:", a_recuperatorio)
print("Aprobados:", aprobados)



