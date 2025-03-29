"""
Crear una clase llamada Persona que tenga dos variables de instancia: nombre y apellido
Crear 2 objetos (instancias) de Persona y mostrar sus atributos con print()
"""


class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido


juan = Persona("Juan", "Pérez")
maria = Persona("María", "Gómez")

print(f"Instancia <juan>: Nombre: {juan.nombre}. Apellido: {juan.apellido}")
print(f"Instancia <maria>: Nombre: {maria.nombre}. Apellido: {maria.apellido}")
