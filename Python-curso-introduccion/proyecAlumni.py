from time import sleep

def mostrar_alumnos(lista):
    if(not lista):
        print("No se han ingresado alumnos todavia")
        print()
        sleep(1)
    else:
        print()
        print("Lista de alumnos: ")
        for alumno,materia in lista:
            print(f"{alumno} - {materia} cursos")
            sleep(0.8)
        print()

def añadir(lista):
    nombre=input("Nombre del alumno: ")
    materias=int(input("Cantidad de materias: "))
    print()
    lista.append([nombre,materias])
    return lista

lista_alumnos=[]
print("Ingrese el numero de la operacion que desea ejecutar: ")
print("1 - Añadir un alumno a la lista.")
print("2 - Ver la lista de alumnos.")
print("3 - Salir.")
opcion=int(input(">>> "))

while(opcion!=3):
    if(opcion==1):
        lista_alumnos=añadir(lista_alumnos)
    elif(opcion==2):
        mostrar_alumnos(lista_alumnos)
    else:
        print("La opcion ingresada no es correcta, vuelva a intentarlo")

    print("Ingrese el numero de la operacion que desea ejecutar: ")
    print("1 - Añadir un alumno a la lista.")
    print("2 - Ver la lista de alumnos.")
    print("3 - Salir.")
    opcion=int(input(">>> "))

print("Gracias por utilizar el programa!")

