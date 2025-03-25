decimal: float = 10.4
entero: int = 10
lista: list = [1, 2, 3]
tupla: tuple = (1, 2, 3)

tipos_de_datos = [decimal, entero, lista, tupla]

for tipo in tipos_de_datos:
    print(f"{tipo} es de tipo {type(tipo)}")
