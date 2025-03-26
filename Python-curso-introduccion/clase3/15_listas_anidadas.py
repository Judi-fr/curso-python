lista_de_compras = [
    ["arroz", 2000],
    ["pan", 3000],
    ["leche", 2500],
]

arroz = lista_de_compras[0]
print(arroz)
nombre_arroz = arroz[0]
precio_arroz = arroz[1]
print(f"{nombre_arroz}: ${precio_arroz}")

# Otra forma de hacerlo
print(f"{lista_de_compras[0][0]}: ${lista_de_compras[0][1]}")
print(lista_de_compras[2][0])
