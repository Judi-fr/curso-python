def crear_contraseña(contraseña):
    contraseña_creada = contraseña[::-1]
    return contraseña_creada
    # return None
    # return


contraseña_creada = crear_contraseña("usuario")
print(contraseña_creada)

# print(crear_contraseña("usuario"))
