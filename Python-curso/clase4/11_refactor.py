def introducir_datos():
    entrada = input("Escribe algo > ")
    return entrada


def convertir_mayúsculas(cadena):
    return cadena.upper()


def mostrar_datos(cadena_en_mayúsculas):
    if cadena_en_mayúsculas:
        print(cadena_en_mayúsculas)
    else:
        print("La cadena está vacía")


def main():
    entrada = introducir_datos()
    cadena_en_mayúsculas = convertir_mayúsculas(entrada)
    mostrar_datos(cadena_en_mayúsculas)


main()
