def agregar_elemento(conjunto, elemento):
    """Devuelve un nuevo conjunto con el elemento agregado."""
    return conjunto | {elemento}


def eliminar_elemento(conjunto, elemento):
    """Devuelve un nuevo conjunto sin el elemento, si existe."""
    return conjunto - {elemento}


def unir_conjuntos(conjunto1, conjunto2):
    """Devuelve la unión de dos conjuntos."""
    return conjunto1 | conjunto2


def procesar_colores(colores):
    """Aplica las transformaciones necesarias al conjunto de colores."""
    colores = agregar_elemento(colores, "verde")
    colores = eliminar_elemento(colores, "celeste")
    colores = eliminar_elemento(colores, "violeta")  # No causa error si no existe
    colores = eliminar_elemento(colores, "blanco")

    return colores


def main():
    """Función principal que ejecuta el programa."""
    colores = {"rojo", "celeste", "azul", "blanco", "amarillo"}
    colores_mas = {"naranja", "marrón", "lila", "negro", "rosa"}

    colores_procesados = procesar_colores(colores)
    conjunto_final = unir_conjuntos(colores_procesados, colores_mas)

    print(conjunto_final)


main()

# Imprimir docstring de la función:
print(main.__doc__)
