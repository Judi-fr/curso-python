"""edad=int(input("ingrese edad: "))
print(edad)

edad=int(input("ingresa "))"""
"""
dinero=float(input("ingrese la cantidad de dinero disponible:\n"))
print("los postres que hay en el menu son:\n 1.cheesecake 3$\n 2.flan 1$\n 3.cafe 2$\n ")
eleccion=input(f"cual eligiras?\n")

if eleccion == "flan":
    mensaje="anotado un flan!"
    dinero = dinero - 1

elif eleccion == "cheesecake":
    mensaje="anotado un cheesecake"
    dinero = dinero - 3
    
elif eleccion == "cafe":
    mensaje="sale un cafesito"
    dinero = dinero - 2
else:
    mensaje="ese postre no forma parte de la carta"

print(mensaje)
if dinero >=0:
    print(f"dinero restante ${dinero}")
else:
    print("no te alcanza el dinero para hacer esta compra")

"""
"""
from time import sleep

lista=[0,1,2,3,4,5]
numero=0

for listarda in lista:
    sleep(0.5)
    print(f"Numero: {listarda}")
    if numero == 3:
        print("ALERTA!")
    numero += 1
"""
"""edad = int(input("ingrese su edad:",))
mensaje = "edad invalida"

if edad >= 18:
    mensaje="Eres mayor de edad"

elif edad >= 65:
    mensaje = "Eres un anciano"

elif edad > 0:
    mensaje = "Eres menor de edad"

print(mensaje)
"""

"""
numero_1 = int(input("Dame un numero: "))

if numero_1 % 2 == 0 and numero_1 % 3 == 0:
    print("el numero es divisible por 2 y 3")

"""

"""
lista = ["eze","wenchi","fausto","mate","facundo"]
lista.append("ivan")
lista.remove(lista[2])

print(lista)
"""

"""
nombre1 = int(input("1. Numero: "))
nombre2 = int(input("2. Numero: "))
nombre3 = int(input("3. Numero: "))
nombre4 = int(input("4. Numero: "))
nombre5 = int(input("5. Numero: "))

lista = [nombre1, nombre2, nombre3, nombre4, nombre5]

print(lista)
"""
"""
lista = []

for i in range(5):
    num = int(input(f"Ingresa el {i+1} numero: "))
    lista.append(num)

lista.sort()

print(lista)





Pide al usuario que ingrese 7 números y guárdalos en una lista.
Indica cuántos de esos números son pares y cuántos son impares.
Muestra solo los números que son divisibles por 2 y 3 al mismo tiempo.
Ordena la lista de menor a mayor y muéstrala.
"""
"""
lista = []
divisible = []
i = 0

for i in range(7):
    numero = int(input(f"ingrese el {i+1} numero: "))
    lista.append(numero)
    if lista[i] % 2 == 0 and lista[i] % 3 == 0:
despues contador 0+        divisible.append(lista[i])

pares = list(filter(lambda x: x % 2 == 0, lista))
inpares = list(filter(lambda x: x % 2 != 0, lista))

print(pares)
print(inpares)
print(f"Cantidad de numeros pares: {len(pares)}")
print(f"Cantidad de numeros inpares: {len(inpares)}")
print(f"los numeros divisibles por 2 y 3: {divisible}")
"""

"""
from time import sleep

contador=10
while contador > 0:
    print(contador)
    sleep(1)
    contador -= 1

print("¡BOOOOOM!")
"""    
"""
Modificar cada elemento de las canciones,
agregando un número al principio, usando for
Ej:
1. Adicto - Tini
2. Bzrp Music Sessions, Vol. 44 - Tini
3. ...
"""

"""
canciones = [
    "La Gota Fría - Juanes",
    "La Bicicleta - Carlos Vives",
    "La Curandera - Shakira",
    "La Camisa Negra - Juanes",
    "La Vida Es Un Carnaval - Carlos Vives",
    "La Incondicional - Shakira",
    "La Tortura - Shakira",
    "La Llorona - Juanes",
    "La Vida Es Un Carnaval - Carlos Vives",
    "La Incondicional - Shakira"
]

indice=0

for caracter in canciones:
    canciones[indice] = f"{indice+1}. {canciones[indice]}"
    print(canciones[indice])
    indice += 1

"""

"""
Modificar el código para que:
- Si el usuario no llega a ingresar un número válido, se vuelve a
solicitar la entrada de datos
"""
"""while True:
    tabla = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    resultados = []
    entrada = input("Dame un número y te daré su tabla de multiplicación: ")
    caso_positivo = entrada.isdecimal()
    caso_negativo = entrada[0] == "-" and entrada[1:].isdecimal()
    caso_complejo = entrada[0] == " " and entrada[0] = not "-"
     

    if caso_positivo or caso_negativo:
        break
    
    else:
        print("No has ingresado un número")

numero = int(entrada)
for i in tabla:
    multiplicacion = i * numero
    resultados.append(multiplicacion)
print(tabla)
print(resultados)
"""
"""
lista_producto_precio = [
    ["vaso", 100],
    ["plato", 200],
    ["tenedor", 300],
    ["cuchara", 400],
    ["cuchillo", 500],
]

lista_final=[]

for producto, precio in lista_producto_precio:
    resultado = lista_producto_precio[indice][1]  * 10 /100
    lista_producto_precio[indice][1].append(resultado)

"""
#EJERCISIOS CLASE 4
"""
def preguntar_nombre():
    name=input("cual es tu nombre: ")
    return name
        
def saludar_con_nombre(nombre):
    print(f"¡Hola {nombre}!")

def funcion_principal():
    nombre=preguntar_nombre()
    saludar_con_nombre(nombre)
    
funcion_principal()"""

"""
Dada la siguiente lista:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Crear una función que imprima los cuadrados de cada número de la lista
"""
"""
def elevado_al_cuadrado():
    for numero in lista:
        cuadrados = numero **2
        print(f"el {numero} elevado al cuadrado es {cuadrados}")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elevado_al_cuadrado()    """

"""
Crear una función que reciba una cadena y devolver la cadena convertida en mayúsculas
y mostrar el resultado fuera de la función.
Si el resultado es una cadena vacía, mostrar un mensaje indicando que la cadena está vacía.
De lo contrario, mostrar la cadena.
"""
"""
def conv_mayusculas(lista):
    return lista.upper()
    
listarda=input("ingrese una cadena > ")
mayuscula=conv_mayusculas(listarda)

if mayuscula=="":
    print("la cadena esta vacia")

else:
    print(mayuscula)"""

#forma correcta de programar es creando funciones y ejecutandolas en el main este programa deberia ser asi:
#def ingresar_cadena()
#def convertir_a_mayuscula()
#def mostrar_cadena()
#def main()
#en este ultimo se tiene que ejecutar funcion por funcion para poder conformar el programa
#esta es la forma correcta de 


#PRODUCTO MINIMO VIABLE? GOOGLEAR
#SPRIN

"""
Crear una lista de invitados.
A cada uno saludarlo de la misma forma, pero personalizando el saludo con su nombre.
"""


"""
lista_de_invitado = ["ezequiel","esteban", "hernesto"]

def saludo(lista):
    for nombre in lista:
        print(f"Hola {nombre} te doy la bienvenida a la conferencia, te quiero mucho, sos unico para mi, te amo <3")

saludo(lista_de_invitado)"""


"""def sumar(a,b):
    resultado=a+b
    return resultado

def restar(a,b):
    resultado=a-b
    return resultado

def multiplicar(a,b):
    resultado=a*b
    return resultado

def dividir(a,b):
    resultado=a/b
    return resultado

lista=[sumar,restar,multiplicar,dividir]

def main():
    for operacion in lista:
        resultado=operacion(5,5)
        print(resultado)

main()"""

#EJERCITACION CASERA CLASE 4

"""Contar vocales:
Crea una función que reciba una cadena y devuelva la cantidad de vocales que contiene."""

"""def vocales(lista):
    indice=0
    vocalez="aeiouAEIOU"
    for letra in lista:
        if letra in vocalez:
            indice+=1

    print(f"las cantidad de vocales en {lista} son: {indice}")
    indice=0

list="ezequielito es un capito"
vocales(list)"""

"""Inversión de cadenas:
Haz una función que reciba una cadena y devuelva la cadena invertida."""

"""def cadena_invertida(cadena):
    cadena=cadena[::-1]
    return cadena

tamaño = int(input("Dime el tamaño de la lista: "))
lista=[]

while len(lista) < tamaño:
    numero=int(input(f"{len(lista)+1}. Numero en el indice "))
    lista.append(numero)

cadena_final=cadena_invertida(lista)
print(cadena_final)
print("😎")
"""


"""def palindromo(palabra):
    capicua = palabra[::-1]
    if palabra == capicua:
        print("Holly fokin shet, es un palindromo")
    else:
        print("mandame un palindromo, soquete")

word="so"

palindromo(word)"""

"""def factorial (numero):
    factorizado = 0
    #si numero es 5 indice tiene que ser 1 menos osea 4
    indice = numero - 1
    #factorizado = 5 * 4
    factorizado += numero * indice
    #la proxima vez que se multiplique el indice sera uno menos osea 3
    indice-=1
    while indice !=0:
        factorizado = factorizado * indice
        indice -= 1
    return factorizado

def main():
    a = 6
    resultado = factorial(a)
    print(resultado)

main()"""

"""Contar palabras:
Crea una función que reciba una frase y devuelva cuántas palabras tiene.

def cant_palabras(frase):
    spliteado=frase.split()
    return len(spliteado)


poema = ""
cantidad=cant_palabras(poema)
print(cantidad)"""


"""def suma_enteros(numero):
    divididos = numero.split()
    resultado_suma = divididos[0] + divididos[1]
    return resultado_suma

num = 22
resultado = suma_enteros(num)
print(resultado)

"""

"""
Ejercicio con funciones con parámetros predeterminados
Crear una función dividir que reciba dos parámetros, uno opcional y otro obligatorio,
y devuelva el resultado de la división de ambos. Si se pasa un solo argumento,
dividir / 1.
"""
"""
def dividir(a,b=1):
    c=a/b
    return c

a=4, b=2

resultado=dividir(a,b)
print=resultado
"""
"""ALGO PARA MEJORAR ES EN LA FUNCION HACER LA OPERACION DE LA DIVISION EN EL RETURN Y NO ES NECESARIO CREAR VARIABLES
Y ASIGNARLE UN RESULTADO, PUEDO MANDAR DIRECTAMENTE EL RESULTADO"""

"""
A partir del siguiente código, utilizar range() para preguntar cuántos invitados
vendrán a la fiesta.
Luego, utilizar un bucle for para preguntar el nombre de cada uno
y guardarlo en una lista. Ordenarlos alfabéticamente (opcional)
Finalmente, convertir la lista en una tupla
y mostrar la lista de invitados iterando sobre ellos
"""
"""def saludar(nombre):
    print(f"¡Bienvenido {nombre}!")

cantidad_invitados= int(input("cuantos invitados vendran a la fiesta? "))

lista_de_invitados = []

for nombre in range(cantidad_invitados):
    lista_de_invitados.append(input("Nombre: "))

lista_de_invitados.sort()

tuple=tuple(lista_de_invitados)

for invitado in lista_de_invitados:
    saludar(invitado)
"""
"""
colores={"rojo","celeste","azul","blanco","amarillo"}

colores.add("verde")
colores.remove("celeste")
colores.discard("violeta")
colores.discard("blanco")
 
print(colores)"""

"""
=========
EJERCICIO
=========
Solicitar al usuario datos sobre un producto:
    - nombre
    - precio
    - cantidad
Guardar en un diccionario y mostrar en la consola:
"El producto < > cuesta $< > y su stock es < >."
"""

"""nombre=input("ingresa el nombre ")
precio=float(input("ingresa el precio "))
cantidad=int(input("ingresa la cantidad"))

producto={
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad
}

print(producto)


"""

"""nota_uno = 10
nota_dos = 6
nota_tres = 8

lista=[nota_dos, nota_tres, nota_uno]

print(sum(lista)/len(lista))
"""
"""entrada=False
while(entrada==False):
    edad=int(input("ingresha tu edad tio "))
    if(edad>0 and edad<=99):
        entrada=True
    else:
        print("tu edad no es valida tio, vete a tomar por culo!")

if(edad>=18):
    print("jo-der tio, eresh mayior de edad! me cago en la puta!")

else:
    print("vete a tomar por culo, wachin de mierda")
"""

uno=300*6
dos=500*4
tres=700*2

lista=[uno,dos,tres]
lista=sum(lista)

lista=lista/12

if lista > 900:
    print("ganas un sueldo mejor que lo normal")
elif lista < 300:
    print("fokin pobre panza de mierda")
elif lista >= 300 and lista <= 900:
    print(f"wena tio {lista}")