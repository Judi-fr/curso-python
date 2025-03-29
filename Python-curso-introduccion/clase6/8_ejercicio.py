"""
Crear una clase llamada Ciudad
tendrá un método que dé la bienvenida a la ciudad
otro que muestre la cantidad de habitantes de la ciudad
"""

lista_ciudades = []


class Ciudad:
    def __init__(self) -> None:
        self.nombre = self.introducir_nombre()
        self.cantidad_habitantes = self.introducir_cantidad_habitantes()
        lista_ciudades.append(self)

    def introducir_nombre(self):
        return input("Nombre de la ciudad: ")

    def introducir_cantidad_habitantes(self):
        return int(input(f"Cantidad de habitantes de {self.nombre}: "))

    def dar_bienvenida(self):
        print(f"Bienvenido a la ciudad de {self.nombre}")

    def mostrar_cantidad_habitantes(self):
        print(f"La cantidad de habitantes es: {self.cantidad_habitantes}")


def main():
    ciudad = Ciudad()
    ciudad = Ciudad()

    for ciudad in lista_ciudades:
        print(ciudad)
        ciudad.dar_bienvenida()
        ciudad.mostrar_cantidad_habitantes()
        print()


main()
