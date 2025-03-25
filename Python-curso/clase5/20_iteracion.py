produtos_lácteos = [
    {"nombre": "Leche", "precio": 1.5, "cantidad": 10},
    {"nombre": "Yogur", "precio": 0.5, "cantidad": 20},
    {"nombre": "Queso", "precio": 2.5, "cantidad": 5},
    {"nombre": "Manzana", "precio": 0.8, "cantidad": 30},
]


for producto in produtos_lácteos:
    print("-------------------------------------")
    for clave, valor in producto.items():
        if clave == "precio":
            print(f"{clave.upper()}: ${valor}")
        else:
            print(f"{clave.upper()}: {valor}")
