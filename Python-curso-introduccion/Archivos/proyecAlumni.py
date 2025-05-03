class Postulante:

    def __init__(self):
        self.nombre=input("nombre: ")
        self.edad=int(input("edad: "))
        self.puesto=input("puesto: ")
        self.experiencia=int(input("años de experiencia: "))
    
    def get(self):
        """print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")
        print(f"puesto: {self.puesto}")
        print(f"experiencia: {self.experiencia}")"""
        return self.nombre, self.edad, self.puesto, self.experiencia
        
    def evaluar(self, edadMin, edadMax, puestos, experiencia):
        self.evaluado="Pasó"
        if not(self.edad >= edadMin and self.edad <=edadMax):
            self.evaluado="No Pasó"
            self.razon+="No cumple con la edad deseada.\n "
        elif self.puesto != puestos[0] and self.puesto != puestos[1] and self.puesto != puestos[2]:
            pass


def main():
    i=0
    lista_postu=[]

    print("1. Agregar un postulante")
    print("2. Evaluar a 1 postulante")
    print("3. Evaluarlos a todos")
    print("0. Salir")
    print()
    opcion=int(input(">>> "))

    while(opcion!=0):

        if(opcion==1):
            postulantes=Postulante()
            lista_postu.append(postulantes.get())
            print("estudiante agregado!")
        elif(opcion==2):
            nombre=input("indique el nombre del postulante que desea evaluar: ")
            for tupla in lista_postu:
                if tupla[i]==nombre:
                    print("coincidio el nombre!")
                    pass
                else:
                    i+=1

        elif(opcion==3):
            pass
        else:
            exit()

        print("1. Agregar un postulante")
        print("2. Evaluar a 1 postulante")
        print("3. Evaluarlos a todos")
        print("0. Salir")
        print()
        opcion=int(input(">>> "))


main()
