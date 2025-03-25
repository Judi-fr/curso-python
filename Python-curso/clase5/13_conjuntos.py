# Set: Conjunto de elementos desordenados y únicos


conjunto = {1, 1, "a", "b", (1, 2), True, "b"}
print(conjunto)

# conjunto[0] = 2 # Esto dará un error, ya que los conjuntos no son indexables
print(type(conjunto))

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
inteseccion_a_b = set_a.intersection(set_b)
diferencia_simetrica_a_b = set_a.symmetric_difference(set_b)
print(inteseccion_a_b)
print(diferencia_simetrica_a_b)
print()
set_a.add(6)  # Agrega un elemento al conjunto
set_a.remove(1)  # Elimina un elemento del conjunto, si no existe, lanza un error
set_a.discard(1)  # Elimina un elemento del conjunto, si no existe, no hace nada
print(set_a)
