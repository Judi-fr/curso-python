

'''
crea un programa que ingrese un dato en una lista de str o int o float según corresponda.
utiliza funciones
conceptos de pila : FIFO/ LIFO

'''
'''
archivo externo
    leer y grabar
'''
'''
crea un menu
selecciona la pila a utilizar
pilas
    Agrega elemento a la pila seleccionada: 
        Función que recibe una cadena de caracteres y una pila, y añade la cadena a la pila,
        si no está llena. si esta llena muestra un mensaje de error.
    Borra elemento de la pila seleccionada:
        Función que recibe una pila y devuelve el último elemento añadido y lo borra de la pila. 
        Si la pila está vacía muestra un mensaje de error.
    Modifica elemento de la pila seleccionada:
    Mostrar pila
        Pila_vacia: Función que recibe una pila y que devuelve si la pila está vacía, no tiene elementos.
        Longitud de la pila:  Función que recibe una pila y devuelve el número de elementos que tiene.
        Función que recibe una pila y muestra en pantalla los elementos de la pila.
        
'''
pila = []
pila_cantidad_elementos =10
def funcion_agregar(string,pila):
    if len(pila)<=(pila_cantidad_elementos-1):
        pila.append(string)
        return pila
    else:
        print ("no hay mas lugar en la pila")
        return pila
def funcion_borrar(pila):
    if len(pila)!=0:
        pila.pop()#ultimo
        return pila
    else:
        print ("no hay mas elementos para borrar en la pila")
        return pila

def funcion_modificar(index,pila,string):
    if index<len(pila)-1:
        pila[index]=string
        return pila
    else:#index>=len(pila):
        print (f"no hay mas elementos para modificar en el index {index} en la pila")
        return pila
def funcion_mostrar(pila):
    print (f"El contentenido de la pila es {pila}")
    if len(pila)>0:
        print (f"La cantidad de elementos de la pila es de {len(pila)}")
    else:
        print (f"pila vacia")
        

pila = []
opcion =""
while opcion !='S':
    opcion = input ("""Ingrese:
    1) para agregar datos
    2) para borrar datos
    3) para modificar datos
    4) para mostrar datos
    S) para salir
    """)
    match (opcion):
        case '1':
            string = input("ingrese el string a agregar:")
            pila = funcion_agregar(string,pila)
            print("*"*54)
            print("*","elemento agregado".center(50),"*")
            print("*"*54)
            print (f"actualización = { pila}")
        case '2':
            pila = funcion_borrar(pila)
            print("*"*54)
            print("*","elemento borrado".center(50),"*")
            print("*"*54)
            print (f"actualización = { pila}")
        case '3':
            index = ''
            while index.isdigit() is False:
                index = input("ingrese el index (numero entero) del elemento a modificar:")
            index = int(index)
            string = input("ingrese el nuevo string para modificar:")
            pila = funcion_modificar(index,pila,string)
            print("*"*54)
            print("*","elemento modificado".center(50),"*")
            print("*"*54)
            print (f"actualización = { pila}")
        case '4':
            print("*"*54)
            print("*","elemento en pantalla".center(50),"*")
            print("*"*54)
            funcion_mostrar(pila)

        case 'S':
            break
        case otrer:
            print ("opción no valida")


pausa()
limpiar()
#######################################################################################################
'''

Ejercicio 1
script con funciones que pida un número y calcule su factorial (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120),
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 2
script con funciones que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había generado.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 3
script con funciones  que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 4
script con funciones que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 5
script con funciones que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un espacio.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 6
script con funciones que imprima todos los números pares entre dos números que se le pidan al usuario.

Ejercicio 7
script con funciones que muestre la tabla de multiplicar de un número introducido por teclado.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 8
script con funciones que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir. A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:

La suma de los números que están dentro del intervalo (intervalo abierto).
Cuantos números están fuera del intervalo.
He informa si hemos introducido algún número igual a los límites del intervalo.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 9
script con funciones que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 10
script con funciones que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 11
script con funciones que diga si un número introducido por teclado es o no primo. Un número primo es aquel que sólo es divisible entre él mismo y la unidad. Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 12
Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada mes.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 13
Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días) y requiere determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 14
Una persona se encuentra en el kilómetro 70 de una carretera, otra se encuentra en el km 150, los coches tienen sentido opuesto y tienen la misma velocidad. Realizar un programa para determinar en qué kilómetro de esa carretera se encontrarán.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 15
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 u$s, el segundo 15 u$s, el tercero 20 u$s y así sucesivamente. Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 16
Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, además, calcule cuánto pagó la empresa por los N empleados.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 17
Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. Para esto, se registran los días que trabajó y las horas de cada día. Realice un algoritmo para determinar el sueldo semanal de N trabajadores y además calcule cuánto pagó la empresa por los N empleados.

Ejercicio 18
Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 19
Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de “Salir”.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 20
Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicios de funciones
Ejercicio 21
script con funciones EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado en pantalla (suponiendo una anchura de 80 columnas; pista: deberás escribir 40 - longitud/2 espacios antes del texto). Además subraya el mensaje utilizando el carácter =.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 22
script con funciones que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. script con funciones EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 23
Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 24
script con funciones “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. script con funciones principal donde se use dicha función.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 25
script con funciones “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. script con funciones que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 26
script con funciones que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 27
Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.

Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 28
Crear una función recursiva que permita calcular el factorial de un número. Realiza un programa principal donde se lea un entero y se muestre el resultado del factorial.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 29
Crear una función que calcule el MCD de dos número por el método de Euclides. El método de Euclides es el siguiente:

Se divide el número mayor entre el menor.
Si la división es exacta, el divisor es el MCD.
Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
script con funciones principal que lea dos números enteros y muestre el MCD.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 30
Escribir dos funciones que permitan calcular:

La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
script con funciones principal con un menú donde se pueda elegir la opción de convertir a segundos, convertir a horas,minutos y segundos o salir del programa.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 31
El día juliano correspondiente a una fecha es un número entero que indica los días que han transcurrido desde el 1 de enero del año indicado. Queremos crear un programa principal que al introducir una fecha nos diga el día juliano que corresponde. Para ello podemos hacer las siguientes subrutinas:

LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
EsBisiesto: Recibe un año y nos dice si es bisiesto.
Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 32
Vamos a mejorar el ejercicio anterior haciendo una función para validar la fecha. De tal forma que al leer una fecha se asegura que es válida.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 33
Queremos crear un programa que trabaje con fracciones a/b. Para representar una fracción vamos a utilizar dos enteros: numerador y denominador.

Vamos a crear las siguientes funciones para trabajar con funciones:

Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador. Cuando leas una fracción debes simplificarla.
Escribir_fracción: Esta función escribe en pantalla la fracción. Si el dominador es 1, se muestra sólo el numerador.
Calcular_mcd: Esta función recibe dos número y devuelve el máximo común divisor.
Simplificar_fracción: Esta función simplifica la fracción, para ello hay que dividir numerador y dominador por el MCD del numerador y denominador.
Sumar_fracciones: Función que recibe dos funciones n1/d1 y n2/d2, y calcula la suma de las dos fracciones. La suma de dos fracciones es otra fracción cuyo numerador=n1*d2+d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
Restar_fracciones: Función que resta dos fracciones: numerador=n1*d2-d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
Multiplicar_fracciones: Función que recibe dos fracciones y calcula el producto, para ello numerador=n1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente, para ello numerador=n1*d2 y denominador=d1*n2. Se debe simplificar la fracción resultado.
Crear un programa que utilizando las funciones anteriores muestre el siguiente menú:

Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el resultado.
Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la resta.
Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra la producto.
Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra la cociente.
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 34
Vamos a crear un programa para trabajar con una pila. Una pila es una estructura de datos que nos permite guardar un conjunto de variables. La característica fundamental es que el último elemento que se añade al conjunto es el primero que se puede sacar.

Para representar una pila vamos a utilizar una lista de cadenas de caracteres.

Vamos a crear varias funciones para trabajar con la pila:

LongitudPila: Función que recibe una pila y devuelve el número de elementos que tiene.
EstaVaciaPila: Función que recibe una pila y que devuelve si la pila está vacía, no tiene elementos.
EstaLlenaPila: Función que recibe una pila y que devuelve si la pila está llena.
AddPila: función que recibe una cadena de caracteres y una pila, y añade la cadena a la pila, si no está llena. si esta llena muestra un mensaje de error.
SacarDeLaPila: Función que recibe una pila y devuelve el último elemento añadido y lo borra de la pila. Si la pila está vacía muestra un mensaje de error.
EscribirPila: Función que recibe una pila y muestra en pantalla los elementos de la pila.
Realiza un programa principal que nos permita usar las funciones anterior, que nos muestre un menú, con las siguientes opciones:

Añadir elemento a la pila
Sacar elemento de la pila
Longitud de la pila
Mostrar pila
'''
pausa()
limpiar()
#######################################################################################################
'''
Ejercicio 35
Vamos a realizar un programa similar al anterior para trabajar con una cola. Una cola es una estructura de datos que nos permite guardar un conjunto de variables. La característica fundamental es que el primer elemento que se añade al conjunto es el primero que se puede sacar.

En realizada nos sirven todas las funciones del ejercicio anterior menos la función SacarDeLaCola que es la que tienes que modificar.
'''
pausa()
limpiar()
#######################################################################################################
'''
'''
