class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido


def listar_personas(personas):
    for persona in personas:
        print(f"Nombre: {persona.nombre}. Apellido: {persona.apellido}")


def main():
    juan = Persona("Juan", "Pérez")
    maria = Persona("María", "Gómez")
    personas = [juan, maria]
    listar_personas(personas)


main()
