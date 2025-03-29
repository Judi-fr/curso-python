class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):  # método de instancia
        print(f"Hola, soy {self.nombre} {self.apellido}")


def main():
    juan = Persona("Juan", "Pérez")
    maria = Persona("María", "Gómez")
    juan.saludar()
    maria.saludar()


main()
