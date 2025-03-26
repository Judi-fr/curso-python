def devolver_datos():
    return "hola", 123, True


devolucion = devolver_datos()
print(devolucion[0])
print(devolucion[1])
print(devolucion[2])
cadena, numero, booleano = devolver_datos()
print(cadena, numero, booleano)
