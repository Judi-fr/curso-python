'''
Utilizar el Block de notas o el editor del Visual Studio para crear un archivo
de texto cuyas líneas pueden tener indistintamente 
cualquiera de los siguientes formatos:


f1=[DD MM AAAA DDDDDDDDDDDDDDDDDDDD NNN PPP.PP]
f2=[DD MM AAAA NNN DDDDDDDDDDDDDDDDDDDD PPP.PP]


Donde:
DD = Número de día, en dos posiciones. (01 a 31, comienza en columna 0)
MM = Número de mes, en dos posiciones. (01 a 12, comienza en columna 3)
AAAA = Número de año, en cuatro posiciones. (comienza en columna 6)
DDD... = Nombre del producto (20 posiciones, rellenado con espacios si 
la longitud es menor que 20. Comienza en columna 11 o 16 según el tipo de registro)
NNN = Cantidad de unidades compradas o vendidas. (001 a 999, comienza
en columna 32 u 11) 
PPP.PP = Precio por unidad. Número real (tres dígitos y dos 
decimales, comienza en columna 36)

EJEMPLO:
12 08 2009 035 RESMA PAPEL OBRA 70G 101.15 <– Venta de mercaderías 
08 10 2009 TIJERA ESCOLAR PLAST 150 064.21 <– Compra de mercaderías
 

El mismo archivo contiene registros de ambos formatos intercalados sin ningún 
criterio particular. Se solicita imprimir un listado con la cantidad en stock 
para cada producto, la que se obtiene sumando las compras y restando las ventas
de cada uno de ellos. El listado debe mostrarse ordenado en forma descendente 
según la cantidad en stock. Imprimir también el resultado del ejercicio para 
el año 2009, el que se obtiene restando el total obtenido por ventas menos el
total invertido en compras, considerando solamente aquellas operaciones del año 2009.
No se conoce la cantidad de productos. Tampoco es posible estimar una cantidad 
para este valor.
'''

# ~ def carga(f1):
	# ~ formato = False
	# ~ i=0
	# ~ while(formato == True):
		# ~ i++
		# ~ f1[] = input("Ingresar los datos del formato: ")
		# ~ while()
        
        
# ~ f1=[DD MM AAAA DDDDDDDDDDDDDDDDDDDD NNN PPP.PP]
# ~ f2=[DD MM AAAA NNN DDDDDDDDDDDDDDDDDDDD PPP.PP]

lista_productos = ['pilas Eveready AA','pilas Duracell AAA']
def berna(string):
    print("^"*50)
    if len(string)!=42:
        return "Error"
    else:
        try:
            print(int(string[0:2]))
            print(1<=int(string[0:2])<=31)
            print(1<=int(string[3:5])<=12)
            print(1900<=int(string[6:10])<=2022) 
            print(string[11:31].strip() )
            print(0<=int(string[32:35])<=999) 
            print(0<=float(string[36:43])<=999.99) 
            if (int(string[0:2]))\
                and (1<=int(string[0:2])<=31)\
                and (1<=int(string[3:5])<=12)\
                and (1900<=int(string[6:10])<=2022) \
                and (string[11:31].strip() )\
                and (0<=int(string[32:35])<=999) \
                and (0<=float(string[36:43])<=999.99) :
                print("ok formato 1")
                return
        except:
            pass
        try:
            print(string)
            print(int(string[0:2]))
            print(1<=int(string[0:2])<=31)
            print(1<=int(string[3:5])<=12)
            print(1900<=int(string[6:10])<=2022) 
            print(0<=int(string[11:14])<=999) 
            print(string[15:35].strip() )
            print(0<=float(string[36:43])<=999.99) 
            if (int(string[0:2]))\
                and (1<=int(string[0:2])<=31)\
                and (1<=int(string[3:5])<=12)\
                and (1900<=int(string[6:10])<=2022) \
                and (0<=int(string[11:14])<=999) \
                and (string[15:35].strip() )\
                and (0<=float(string[36:43])<=999.99) :
                print("ok formato 2")
                return
        except:
            print("no corresponde a ningun tipo")
            # ~ print("ok paso 1")
# ~ 31 11 2022 pilas eveready_AAA_ 150 789.12
    # ~ DD MM AAAA DDDDDDDDDDDDDDDDDDDD NNN PPP.PP
f1="31 11 2022 pilas eveready_AAA_  150 789.12"
# ~ carga(f1)
# ~ berna(f1)
f2='31 11 2022 321 pilas eveready_AAA__ 789.12'
berna(f2)
