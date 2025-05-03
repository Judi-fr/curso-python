class Casa:
    def __init__(self, material, cantidad_ambientes):  # método constructor
        self.material = material  # variable de objeto / instancia
        self.cantidad_ambientes = cantidad_ambientes  # variable de objeto / instancia

    def setMaterial(self):
        self.material=input("Nuevo Material: ")

    def setAmbientes(self):
        self.cantidad_ambientes=input("Cantidad de ambientes? ")    

casa_1 = Casa(material="madera", cantidad_ambientes=5)  # se crea un objeto / instancia
casa_2 = Casa("ladrillo", 10)  # se crea un objeto / instancia

print(casa_1.material, casa_1.cantidad_ambientes)
print(casa_2.material, casa_2.cantidad_ambientes)

casa_1.setMaterial()
casa_1.setAmbientes()

print(casa_1.material, casa_1.cantidad_ambientes)
