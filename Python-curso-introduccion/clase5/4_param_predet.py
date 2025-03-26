def saludar(nombre, apellido=""):
    if apellido:  # if apellido != "":
        print(f"Tu nombre es {nombre}.\nTu apellido es {apellido}")
    else:
        print(f"Tu nombre es {nombre}")


saludar("Juan", "Pérez")
print()
saludar("Juan")
