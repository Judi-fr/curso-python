# Tupla
# Es una colección de elementos ordenados e inmutables.

tupla = (1, 2, 3, 4, 5)

print(tupla)
print(type(tupla))
print(len(tupla))
print(tupla[0])

primero, *medio, ultimo = tupla

print(primero, medio, ultimo)
