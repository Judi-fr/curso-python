class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido

    def caminar(self, pasos=0):
        if pasos < 0:
            print("No puedo caminar para atrás")
        elif pasos == 0:
            print("No he caminado...")
        else:
            print(f"Yo {self.nombre}, he dado {pasos} pasos...")


def main():
    juan = Persona("Juan", "Pérez")
    maria = Persona("María", "Gómez")
    juan.caminar(10)
    maria.caminar(-12)


main()
