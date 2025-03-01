# listas en Python

lista = [12, 3.14, "cadena", True, [1, 2, 3]]
longitud_lista = len(lista)
print(f"La lista tiene {longitud_lista} elementos.")

lista_de_frutas = ["manzana", "banana", "naranja"]
existe_manzana = "manzana" in lista_de_frutas
if existe_manzana:
    print("La fruta está en la lista.")
else:
    print("La fruta no está en la lista.")

lista_vacia = []
print(lista_vacia)
print(len(lista_vacia))
