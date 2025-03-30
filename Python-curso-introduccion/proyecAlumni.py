from time import sleep

def mostrar_alumnos(lista):
    if(not lista):
        print("No se han ingresado alumnos todavia")
        print()
        sleep(1)
    else:
        print()
        print("Lista de alumnos: ")
        for diccionario in lista:
            print(f"{diccionario["nombre"]} - {diccionario["materias"]} cursos")
            sleep(0.8)
        print()

def añadir(lista):
    
    nombre=input("Nombre del alumno: ")
    materias=int(input("Cantidad de materias: "))
    diccionario={
        "nombre":nombre,
        "materias":materias,
    }
    lista.append(diccionario)
    print("Alumno agregado!")
    return lista

def buscar_alumno(lista):
   alumno=input("Que alumno queres saber? ")
   for diccionario in lista:
       if(alumno==diccionario["nombre"]):
           print(f"Materias: {diccionario["materias"]}")


lista_alumnos=[]
print("Ingrese el numero de la operacion que desea ejecutar: ")
print("1 - Añadir un alumno a la lista.")
print("2 - Ver la lista de alumnos.")
print("3 - Ver las materias de un alumno.")
print("4 - Salir.")
opcion=int(input(">>> "))

while(opcion!=4):
    if(opcion==1):
        lista_alumnos=añadir(lista_alumnos)
    elif(opcion==2):
        mostrar_alumnos(lista_alumnos)
    elif(opcion==3):
        buscar_alumno(lista_alumnos)
    else:
        print()
        print("La opcion ingresada no es correcta, vuelva a intentarlo")

    sleep(2)
    print()
    print("Ingrese el numero de la operacion que desea ejecutar: ")
    print("1 - Añadir un alumno a la lista.")
    print("2 - Ver la lista de alumnos.")
    print("3 - Ver las materias de un alumno.")
    print("4 - Salir.")
    opcion=int(input(">>> "))

print("Gracias por utilizar el programa!")

