"""
Modificar cada elemento de las canciones,
agregando un número al principio, usando for
Ej:
1. Adicto - Tini
2. Bzrp Music Sessions, Vol. 44 - Tini
3. ...
"""

canciones = [
    "La Gota Fría - Juanes",
    "La Bicicleta - Carlos Vives",
    "La Curandera - Shakira",
    "La Camisa Negra - Juanes",
    "La Vida Es Un Carnaval - Carlos Vives",
    "La Incondicional - Shakira",
    "La Tortura - Shakira",
    "La Llorona - Juanes",
    "La Vida Es Un Carnaval - Carlos Vives",
    "La Incondicional - Shakira",
]

indice = 0

for cancion in canciones:
    canciones[indice] = f"{indice + 1}. {cancion}"
    indice = indice + 1

for cancion in canciones:
    print(cancion)
