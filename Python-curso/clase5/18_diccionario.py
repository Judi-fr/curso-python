diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

print("nombre" in diccionario)

print(diccionario["edad"])
ciudad = diccionario["ciudad"]
print(ciudad)

persona = diccionario
persona["peso"] = 70

print(persona)
persona["peso"] = 75
print(persona)
del persona["ciudad"]
print(persona)
print(diccionario)
