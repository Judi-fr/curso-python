# Las tuplas son una colección de elementos inmutables

mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla)
print(type(mi_tupla))  # <class 'tuple'>
print(len(mi_tupla))  # 5

tupla_un_elemento = (1,)  # Si no se pone la coma, se considera un entero
print(tupla_un_elemento)  # (1,)
print(type(tupla_un_elemento))  # <class 'tuple'>

tupla_vacia = ()
print(tupla_vacia)  # ()
print(len(tupla_vacia))

mi_tupla = (1, 2, 3, 4, 5)
conversion_lista = list(mi_tupla)
conversion_lista.append(6)
mi_tupla = tuple(conversion_lista)
print(mi_tupla)

print(mi_tupla[0])
print(mi_tupla[-1])
print(mi_tupla[0:3])  # (1, 2, 3)
print(mi_tupla[::-1])  # (5, 4, 3, 2, 1)

nueva_tupla = ("casa", "perro", "gato")
# casa = nueva_tupla[0]
# perro = nueva_tupla[1]
# gato = nueva_tupla[2]
casa, perro, gato = nueva_tupla  # desempacar
print(casa, perro, gato)
