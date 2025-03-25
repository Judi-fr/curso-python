def imprimir_nombre(nombre, apellido):
    nombre_completo = f"{apellido.upper()}, {nombre.capitalize()}"
    print(nombre_completo)


def crear_datos():
    persona_1 = ["juan", "Pérez"]
    persona_2 = ["maría", "Gómez"]
    persona_3 = ["carlos", "López"]
    return [persona_1, persona_2, persona_3]


def main():
    lista_personas = crear_datos()
    for persona in lista_personas:
        nombre, apellido = persona
        imprimir_nombre(nombre, apellido)


main()
