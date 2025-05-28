print("*"*100)
print(f'''
1) Genera un script en Python que encuentre en una lista de enteros con exactamente dos ocurrencias de diecinueve y al menos tres ocurrencias de cinco. ''')
Entrada=[19, 19, 15, 5, 3, 5, 5, 2]
Salida=True
Entrada=[19, 15, 15, 5, 3, 3, 5, 2]
Salida=False
Entrada=[19, 19, 5, 5, 5, 5, 5]
Salida=True
Solucion="""
print(Entrada.count(19) == 2 and Entrada.count(5) >= 3)
"""
print("*"*100)
print(f'''
2) Genera un script en Python que encuentre en unalista de enteros y verifique la longitud y el quinto elemento. 
Devuelve True si la longitud de la lista es 8 y el quinto elemento aparece tres veces en dicha lista. ''')
Entrada=[19, 19, 15, 5, 5, 5, 1, 2]
Salida=True
Entrada=[19, 15, 5, 7, 5, 5, 2]
Salida=False
Entrada=[11 , 12, 14, 13, 14, 13, 15, 14]
Salida=True
Entrada=[19, 15, 11, 7, 5, 6, 2]
Salida=False
Solucion="""
print (len(Entrada)==8 and Entrada.count(Entrada[4])==3)
"""
print("*"*100)
print(f'''
3) Genera un script en Python de Python que encuentre en unaprueba de enteros si es un entero mayor que 4^4 y que este %(modulo) 34 == 4. ''')
Entrada=922
Salida=True
Entrada=914
Salida=False
Entrada=854
Salida=True
Entrada=854
Salida=True
Solucion="""
print(Entrada>4**4 and Entrada % 34 ==4)
"""
print("*"*100)
print(f'''
4. ¡Estamos haciendo montones de piedras! La primera pila tiene n piedras. 
Si n es par, entonces todas las pilas tienen  n cantidad de objetos y todos estos seran desde n(par) de 2 en 2 (para ser par) n veces de piedras. 
Si n es impar, lo mismo, entonces todas las pilas tienen  n cantidad de objetos y todos estos seran desde n(impar) de 2 en 2 (para ser impar) n veces de piedras. 
mm...Cada pila debe tener más piedras que la pila anterior pero la menor cantidad posible??
Escribe un programa Python para encontrar el número de piedras en cada pila. ''')
Entrada= 2
Salida=[2, 4]# desde 2 , 2 objetos
Entrada= 10
Salida=[10, 12, 14, 16, 18, 20, 22, 24, 26, 28]#desde 10, 10 objetos
Entrada= 3
Salida=[3, 5, 7]
Entrada= 17
Salida=[17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
Solucion="""
print(f"{[v for v in range(Entrada,(Entrada*2+Entrada),2)]=}")
print("opción")
print(f"{[Entrada + 2 * v for v in range(Entrada)]=}")
"""
print("*"*100)
print(f'''
5) Genera un script en Python para verificar que en la coleccion de entrada de n elementos, 
el ante ultimo elemento sea substring del último elemento.''')
Entrada=['a', 'abb', 'sfs', 'oo', 'de', 'sfde']#len = 5>>Entrada[3] debe estar en Entrada[4]
Salida=True
Entrada=['a', 'abb', 'sfs', ' oo', 'ee', 'sfde']
Salida=False
Entrada=['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']
Salida=False
Entrada=['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'qwsfsdfrew']
Salida=True
Solucion="""
print(f"{ (True if Entrada[-2] in Entrada[-1] else False) =}")
exit()
"""
print("*"*100)
print(f'''
6) Genera un script en Python para verificar que en la coleccion que cumpla con las siguientes condiciones
    1) Contiene 100 elementos. 
    2) Valores entre 0 y 999.
    3) Entre cada elemento debe haber una diferencia de 10. ''')
Entrada=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210 , 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460 , 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710 , 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960 , 970, 980, 990]
Salida=True
Entrada=[0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480 , 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720, 740, 760, 780, 800, 820, 840, 860, 880, 900, 920, 940, 960, 980 ]
Salida=False
Solucion="""
print ( True if len(Entrada)==100 and Entrada[0]==0 and Entrada[-1]<1000 and all([True if (Entrada[index]==  Entrada[index+1]-10) else False for index in range(0,len(Entrada)-1)]) else False)
print("opción")
print ( all(i in range(1000) and abs(i - j) >= 10 for i in Entrada for j in Entrada if i != j) and len(set(Entrada)) == 100)
"""
print("*"*100)
print(f'''
7) Genera un script en Python para verificar una lista de enteros donde la suma de cada elementos entre 
    l index 0 y n es igual al valor de la lista en [n]. ''')
Entrada=[0, 1, 2, 3, 4, 5]
Salida=False
Entrada=[1, 1, 1, 1, 1, 1]
Salida=True
Entrada=[2, 2, 2, 2 , 2]
Salida=False
Solucion="""
print(all([sum(Entrada[0:index])==index for index in range(len(Entrada)) ]))
# ~ """
print("*"*100)
print(f'''
8) Genera un script en Python para dividir un string de palabras separadas por espacios solos o comas (omitir los espacios post comas) en dos listas, palabras y separadores. ''')
Entrada= 'Python 2022, Ejercicios.'
Salida=[['Python', '2022', 'Ejercicios.'], [' ', ',']]
Entrada= "El baile, realizado en el gimnasio de la escuela, terminó a medianoche."
Salida=  [['El', 'baile', 'realizado', 'en', 'el', 'gimnasio', 'de', 'la', 'escuela', 'terminó', 'a', 'medianoche.'], [' ', ',', ' ', ' ', ' ', ' ', ' ', ' ', ',', ' ', ' ']]
Entrada= "Los colores en mi sala de estudio son azul, verde y rojo."
Salida=[['Los', 'colores', 'en', 'mi', 'sala', 'de', 'estudio', 'son', 'azul', 'verde', 'y', 'rojo.'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']]
Solucion="""
print(f"{Entrada=}\n", [Entrada.replace(",","").replace("  "," ").split(),[ caracter for index,caracter in enumerate(Entrada) if ((caracter==" " and Entrada[index-1]!=",") or (caracter=="," ) )]])
"""
print("*"*100)
print(f'''
9) Genera un script en Python para encontrar enteros de lista que contengan exactamente cuatro valores distintos, 
    de modo que ningún entero se repita dos veces consecutivas entre las primeras veinte entradas. ''')
Entrada=[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
Salida=True
Entrada=[1, 2, 3 , 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
Salida=False
Entrada=[1, 2, 3, 1, 2, 3, 1, 2, 3 , 1, 2, 3, 1, 2, 3]
Salida=False
Solucion="""
print(all([Entrada[index] != Entrada[index + 1] for index in range(len(Entrada)-1 if (len(Entrada)<20) else 20) ])and len(set(Entrada))==4)
exit()
"""
print("*"*100)
print(f'''
10. Dada un string que consta de espacios en blanco y grupos de paréntesis coincidentes, 
    escriba un programa de Python para dividirla en grupos de paréntesis perfectamente coincidentes 
    sin ningún espacio en blanco. ''')
Entrada='( ()) ((()()())) (()) ()'
Salida=['(())', '((()()()))', ' (())', '()']
Entrada='() (( ( )() ( )) ) ( ())'
Salida=['()', '((()()()))', '(())']
Solucion="""
print()
"""
print("*"*100)
print(f'''
11) Genera un script en Python para encontrar los índices de números de una lista dada por debajo de un umbral dado. ''')
Lista_original=[0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]
Umbral= 100
Salida=[0, 1, 2, 3, 7, 8, 9, 10]
Lista_original=[0, 12, 4, 3, 49, 9, 1, 5, 3]
Umbral= 10
Salida=[0, 2, 3, 5, 6, 7, 8]
Solucion="""
print()
"""
print("*"*100)
print(f'''
12) Genera un script en Python para verificar si las strings dadas son palíndromos o no. Devuelve True, False. ''')
Entrada=['palindrome', 'madamimadam', '', 'foo', 'eyes']
Salida=[False, True, True, False, False]
Solucion="""
print()
"""
print("*"*100)
print(f'''
13) Genera un script en Python para encontrar las strings en una lista dada, comenzando con alguna de los caracteres prefijo dado al inicio. ''')
Entrada=[( 'ca',('gato', 'coche', 'miedo', 'centro'))]
Salida=['gato', 'coche']
Entrada=[('do',('gato' , 'dog', 'shatter', 'donut', 'at', 'todo'))]
Salida=['dog', 'donut']
Solucion="""
print()
"""
print("*"*100)
print(f'''
14) Genera un script en Python para encontrar las longitudes de una lista dada de strings no vacías. ''')
Entrada=['gato', 'coche', 'miedo', 'centro']
Salida=[3, 3, 4, 6]
Entrada=['gato', 'perro', 'destrozar', ' donut', 'at', 'todo', '']
Salida=[3, 3, 7, 5, 2, 4, 0]
Solucion="""
print()
"""
print("*"*100)
print(f'''
15)  Escriba un programa Python que encuentre es string las largo de la lista. ''')
Entrada=['cat', 'car', 'fear', 'center']
Salida='center'
Entrada=['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Salida='shatter'
Solucion="""
print()
"""
input("Enter para continua.............")
print("*"*100)
print(f'''
16) Genera un script en Python para encontrar las strings en una lista dada que contenga una substring dada. ''')
Entrada=[('ca',('gato', 'coche', 'miedo', 'centro'))]
Salida= ['gato', 'coche']
Entrada= [('o',('gato' , 'perro', 'destrozar', 'dona', 'en', 'todo', ''))]
Salida= ['perro', 'dona', 'todo']
Entrada= [('oe',('gato ', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
Salida= []
Solucion="""
print()
"""
print("*"*100)
print(f'''
17) Genera un script en Python para crear un string que consista en enteros no negativos hasta n inclusive. ''')
Entrada= 4
Salida=0 ,1 ,2, 3 ,4
Entrada=15
Salida= 0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ,15
Solucion="""
print()
"""
print("*"*100)
print(f'''
18. Una matriz irregular/desigual, o matriz irregular, es una matriz que tiene un número diferente de elementos en cada fila. Las matrices irregulares no se usan en álgebra lineal, ya que no se pueden realizar transformaciones de matrices estándar en ellas, pero son útiles como matrices en computación.
Escriba un programa en Python para encontrar los índices de todas las ocurrencias de objetivo en la matriz desigual. ''')
Entrada=[([1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19]),19]
Salida=[[0, 4], [1, 0], [1, 3], [4, 1]]
Entrada=[([1, 2, 3, 2], [], [7, 9, 2 , 1, 4]), 2]
Salida=[[0, 1], [0, 3], [2, 2]]
Solucion="""
print()
"""
print("*"*100)
print(f'''
19) Genera un script en Python de Python para dividir un string dada en strings si hay un espacio en el string; de lo contrario,
divida en comas si hay una coma; de lo contrario, devuelva la lista de letras minúsculas en orden impar (orden de a = 0, b = 1, etc.)''')
Entrada='abcd'
Salida=['a', 'b ', 'c', 'd']
Entrada='a,b,c,d'
Salida:['a' , 'b', 'c', 'd']
Entrada='abcd'
salida=['b', 'd']
Solucion="""
print()
"""
print("*"*100)
print(f'''
20) Genera un script en Python para determinar la dirección ("creciente" o "decreciente") de los números de secuencia monótona. ''')
Entrada=[1, 2, 3, 4, 5, 6]
Salida="creciente"
Entrada=[6, 5, 4, 3, 2, 1]
Salida="decreciente"
Entrada=[19, 19, 5, 5, 5, 5, 5]
Salida='¡No es una secuencia monótona!'
Solucion="""
print()
"""
print("*"*100)
print(f'''
21) Genera un script en Python para verificar, para cada string en una lista dada, si el último carácter es una letra aislada o no. Devuelve True o False. ''')
Entrada=['gato', 'coche', 'miedo', 'centro']
Salida=[False, False, False, False]
Entrada=['ca t', 'coche', 'miedo' , 'cent r']
Salida=[True, False, True, True]
Solucion="""
print()
"""
print("*"*100)
print(f'''
22) Genera un script en Python para calcular la suma de los valores ASCII de los caracteres en mayúsculas en un string determinada. ''')
Entrada='PytHon ExerciSEs'
Salida=373
Entrada='the blue JavaScript developmmen'
Salida=157
Solucion="""
print()
"""
print("*"*100)
print(f'''
23) Genera un script en Python para encontrar los índices para los cuales caen los números en la lista. 
NOTA: puede detectar varias caídas simplemente comprobando si nums[i] < nums[i-1]''')
Entrada=[0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
Salida=[1, 4, 6, 8, 10, 11, 15, 16, 18]
Entrada=[6, 5, 4, 3, 2, 1]
Salida=[1, 2, 3, 4, 5]
Entrada=[1, 19, 5, 15, 5, 25, 5]
Salida=[0, 2, 4, 6 ]
Solucion="""
print()
"""
print("*"*100)
print(f'''
24) Genera un script en Python para crear una lista cuyo i -ésimo elemento sea el máximo de los primeros i elementos de una lista de entrada. ''')
Entrada=[0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
Salida=[0, 0, 3, 8, 8, 9, 9, 14, 14, 14, 14, 14, 14, 17, 41, 41, 41, 41, 41, 41]
Entrada=[6, 5, 4, 3, 2, 1]
Salida=[6, 6, 6, 6, 6, 6]
Entrada=[1, 19, 5, 15, 5, 25, 5]
Salida=[1, 19, 19 , 19, 19, 25, 25]
Solucion="""
print()
"""
print("*"*100)
print(f'''
25) Genera un script en Python para encontrar el XOR de dos strings dadas interpretadas como números binarios. ''')
Entrada=['0001', '1011']
Salida=0b1010
Entrada=['100011101100001', '100101100101110']
Salida=0b110001001111
Solucion="""
print()
"""
print("*"*100)
print(f'''
26) Genera un script en Python para encontrar el número más grande donde las comas o los puntos son puntos decimales. ''')
Entrada=['100', '102,1', '101.1']
Salida=102.1
Solucion="""
print()
"""
print("*"*100)
print(f'''
27) Genera un script en Python para encontrar x que minimice la desviación cuadrática media de una lista dada de números. ''')
Entrada=[4, -5, 17, -9, 14, 108, -9]
Salida=17.142857142857142
Entrada=[12, -2, 14, 3, -15, 10, -45, 3, 30 ]
Salida=1.1111111111111112
Solucion="""
print()
"""
print("*"*100)
print(f'''
28) Genera un script en Python para seleccionar un string de una lista dada de strings con los caracteres más exclusivos. ''')
Entrada=['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
Salida='abcdefhijklmnop'
Entrada=['Green', 'Red', 'Orange ', 'Amarillo', '', 'Blanco']
Salida='Naranja'
Solucion="""
print()
"""
print("*"*100)
print(f'''
29) Genera un script en Python para encontrar los índices de dos números que suman 0 en una lista dada de números. ''')
Entrada=[1, -4, 6, 7, 4]
Salida=[4, 1]
Entrada=[1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]
Salida=[1, 7]
Solucion="""
print()
"""
print("*"*100)
print(f'''
30) Genera un script en Python para encontrar la lista de strings que tiene menos caracteres en total (incluidas las repeticiones). ''')
Entrada=[['esto', 'lista', 'es', 'estrecho'], ['yo', 'soy', 'más corto pero más ancho']]
Salida=['esto', 'lista ', 'es', 'estrecho']
Entrada=[['Rojo', 'Negro', 'Rosa'], ['Verde', 'Rojo', 'Blanco']]
Salida=['Rojo', 'Negro ', 'Rosa']
Solucion="""
print()
"""
print("*"*100)
print(f'''
31. Escribe un programa en Python para encontrar las coordenadas de un triángulo con las longitudes de lado dadas. ''')
Entrada=[3, 4, 5]
Salida=[[0.0, 0.0], [3, 0.0], [3.0, 4.0]]
Entrada=[5, 6, 7]
Salida=[[0.0, 0.0 ], [5, 0.0], [3.8, 5.878775382679628]]
Solucion="""
print()
"""
print("*"*100)
print(f'''
32) Genera un script en Python para cambiar la escala y cambiar los números de una lista dada, de modo que cubran el rango [0, 1]. ''')
Entrada=[18.5, 17.0, 18.0, 19.0, 18.0]
Salida=[0.75, 0.0, 0.5, 1.0, 0.5]
Entrada=[13.0, 17.0, 17.0, 15.5, 2.94]
Salida=[0.7155049786628734, 1.0, 1.0, 0.8933143669985776, 0.0]
Solucion="""
print()
"""
print("*"*100)
print(f'''
33) Genera un script en Python para encontrar las posiciones de todas las vocales mayúsculas (sin contar la Y) en índices pares de un string dada. ''')
Entrada= 'w3rEsOURcE'
Salida=[6]
Entrada='AEIOUYW'
Salida=[0, 2, 4]
Solucion="""
print()
"""
print("*"*100)
print(f'''
34. Escribe un programa en Python para encontrar la suma de los números de una lista dada entre los primeros k con más de 2 dígitos. ''')
Entrada= [4, 5, 17, 9, 14, 108, -9, 12, 76]
Valor_de_K= 4
Salida=0
Entrada= [4, 5, 17, 9, 14, 108, - 9, 12, 76]
Valor_de_K= 6
Salida=108
Entrada= [114, 215, -117, 119, 14, 108, -9, 12, 76]
Valor_de_K= 5
Salida=331
Entrada= [114, 215, -117, 119, 14, 108, -9, 12, 76]
Valor_de_K= 1
Salida=114
Solucion="""
print()
"""
print("*"*100)
print(f'''
35) Genera un script en Python para calcular el producto de los dígitos impares en un número dado, o 0 si no hay ninguno. ''')
Entrada= 123456789
Salida=945
Entrada= 2468
Salida=0
Entrada= 13579
Salida=945
Solucion="""
print()
"""
print("*"*100)
print(f'''
36) Genera un script en Python para encontrar los k números más grandes de una lista dada de números. ''')
Entrada= [1, 2, 3, 4, 5, 5, 3, 6, 2]
Salida=[6]
Entrada= [1, 2, 3, 4, 5, 5, 3, 6, 2 ]
Salida=[6, 5]
Entrada= [1, 2, 3, 4, 5, 5, 3, 6, 2]
Salida=[6, 5, 5]
Entrada= [1, 2, 3, 4, 5 , 5, 3, 6, 2]
Salida=[6, 5, 5, 4]
Entrada= [1, 2, 3, 4, 5, 5, 3, 6, 2]
Salida=[6, 5, 5, 4, 3]
Solucion="""
print()
"""
print("*"*100)
print(f'''
37) Genera un script en Python para encontrar el divisor entero más grande de un número n que sea menor que n. ''')
Entrada= 18
Salida=9
Entrada= 100
Salida=50
Entrada= 102
Salida=51
Entrada= 500
Salida=250
Entrada= 1000
Salida=500
Entrada= 6500
Salida=3250
Solucion="""
print()
"""
print("*"*100)
print(f'''
38) Genera un script en Python para ordenar los números de una lista dada por la suma de sus dígitos. ''')
Entrada= [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Salida=[10, 11, 20, 12, 13, 14, 15, 16, 17, 18, 19]
Entrada= [23, 2, 9, 34, 8, 9, 10, 74]
Salida=[10, 2, 23, 34, 8, 9, 9, 74]
Solucion="""
print()
"""
print("*"*100)
print(f'''
39) Genera un script en Python para determinar qué triples suman cero de una lista dada de listas. ''')
Entrada= [[1343532, -2920635, 332], [-27, 18, 9], [4, 0, -4], [2, 2, 2], [-20, 16, 4] ]
Salida=[False, True, True, False, True]
Entrada= [[1, 2, -3], [-4, 0, 4], [0, 1, -5], [1, 1, 1 ], [-2, 4, -1]]
Salida=[True, True, False, False, False]
Solucion="""
print()
"""
print("*"*100)
print(f'''
40) Genera un script en Python para encontrar strings que, cuando se invierten las mayúsculas en minúsculas y viceversa, 
proporcionen un destino donde las vocales se reemplazan por caracteres dos ascii mas grandes. ''')
Entrada= 'Python'
Salida='pYTHQN'
Entrada= 'aeiou'
Salida='CGKQW'
Entrada= '¡Hola, mundo!'
Salida='hGLLQ, WQRLD!'
Entrada='AEIOU'
Salida='cgkqw'
Solucion="""
print()
"""
print("*"*100)
print(f'''
41) Genera un script en Python para ordenar números según strings. ''')
Entrada=['seis','uno','cuatro','uno','dos','tres']
Salida=['uno','dos','tres','cuatro','seis']
Entrada=['seis','uno','cuatro','tres','dos','nueve','ocho']
Salida=['uno','dos','tres','cuatro','seis','ocho','nueve']
Entrada=['nueve','ocho','siete','seis','cinco','cuatro','tres','dos','uno']
Salida=['uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve']
Solucion="""
print()
"""
print("*"*100)
print(f'''
42) Genera un script en Python para encontrar el conjunto de caracteres distintos en un string dado, 
ignorando mayúsculas y minúsculas. ''')
Entrada= 'HELLO'
Salida=['h', 'o', 'l', 'e']
Entrada= 'HelloLo'
Salida=['h', 'o', 'l', 'e']
Entrada= 'Ignoring case'
Salida=['s','n','c', 'o','e','i','r','g','a', ' ']
Solucion="""
print()
"""
print("*"*100)
print(f'''
43) Genera un script en Python para encontrar todas las palabras en un string dada con n consonantes. ''')
string= 'this is our time'
Entrada= 3
Salida=['this']
Entrada=2
Salida=['time']
Entrada=1
Salida=['is', 'our']
Solucion="""
print()
"""
print("*"*100)
print(f'''
44) Genera un script en Python para encontrar qué caracteres de un número hexadecimal corresponden a números primos. ''')
Entrada= '123ABCD'
Salida=[False, True, True, False, True, False, True]
Entrada= '123456'
Salida=[False, True, True, False, True, False]
Entrada= 'FACE'
Salida=[False, False, False, False]
Solucion="""
print()
"""
print("*"*100)
print(f'''
45) Genera un script en Python para encontrar todos los palíndromos pares hasta n. ''')
# ~ Salida=
# ~ Palíndromos pares hasta 50 -
# ~ [0, 2, 4, 6, 8, 22, 44]
# ~ Palíndromos pares hasta 100 -
# ~ [0, 2, 4, 6, 8, 22, 44, 66, 88]
# ~ Incluso palíndromos hasta 500 -
# ~ [0, 2, 4, 6, 8, 22, 44, 66, 88, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 404, 414 , 424, 434, 444, 454, 464, 474, 484, 494]
# ~ Incluso palíndromos hasta 2000 -
# ~ [0, 2, 4, 6, 8, 22, 44, 66, 88, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 404, 414, 424, 434, 444, 454, 464, 474, 484, 494, 606, 616, 626, 636, 646, 656, 666, 676, 686, 696, 808, 818, 828, 838, 848, 858, 868, 878, 888, 898]
Solucion="""
print()
"""
print("*"*100)
print(f'''
46. ​​Dada una matriz de números que representan una rama en un árbol binario, escriba un programa en Python para 
encontrar el valor par mínimo y su índice. En caso de empate, devuelve el índice más pequeño. 
Si no hay números pares, la respuesta es []. ''')
Entrada=[1, 9, 4, 6, 10, 11, 14, 8]
#Valor par mínimo y su índice de dicha matriz de números:
Salida=[4, 2]
Entrada=[1, 7, 4, 4, 9, 2]
Salida=[2, 5]
Entrada=[1, 7, 7, 5, 9]
Salida=[]
Solucion="""
print()
"""
print("*"*100)
print(f'''
47) Genera un script en Python para Filtrar los números en números en una lista dada cuya suma de dígitos es > 0, donde el primer dígito puede ser negativo. ''')
Entrada=[11, -6, -103, -200]
Salida=[11, -103]
Entrada=[1, 7, -4, 4, -9, 2]
Salida=[1, 7, 4, 2]
Entrada=[10, -11, -71, -13, 14, -32]
Salida=[10, -13, 14]
Solucion="""
print()
"""
print("*"*100)
print(f'''
48) Genera un script en Python para encontrar los índices de dos entradas que muestren que la lista no está en orden creciente. Si no hay infracciones (están aumentando), devuelve una lista vacía. ''')
Entrada=[1, 2, 3, 0, 4, 5, 6]
Salida=[2, 3]
Entrada=[1, 2, 3, 4, 5, 6]
Salida=[]
Entrada=[ 1, 2, 3, 4, 6, 5, 7]
Salida=[4, 5]
Entrada=[-3, -2, -3, 0, 2, 3, 4]
Salida=[1, 2]
Solucion="""
print()
"""
print("*"*100)
print(f'''
49) Genera un script en Python para encontrar el índice h, el mayor número positivo h tal que h aparece en la secuencia al menos h veces. Si no existe tal número positivo, devuelva h = -1. ''')
Entrada=[1, 2, 2, 3, 3, 4, 4, 4, 4]
Salida=4
Entrada=[1, 2, 2, 3, 4, 5, 6]
Salida=2
Entrada=[3, 1, 4, 17, 5, 17, 2, 1, 41, 32, 2, 5, 5, 5, 5]
Salida=5
Solucion="""
print()
"""
print("*"*100)
print(f'''
50) Genera un script en Python para encontrar las palabras de longitud uniforme de una lista dada de palabras y ordénelas por longitud. ''')
Entrada=['Rojo', 'Negro', 'Blanco', 'Verde', 'Rosa', 'Naranja']
Salida=['Pink', 'Orange']
Entrada=['The', 'worm', 'ate', 'a', 'bird', 'imagine', 'that', '!', ' Absurdo', '!!']
Salida=['!!', 'pájaro', 'eso', 'gusano', 'Absurdo']
print("*"*100)
print(f'''
51) Genera un script en Python para encontrar los primeros n números de Fibonacci. ''')
Entrada= 10
Salida=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
Entrada= 15
Salida=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
Entrada= 50
Salida=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025]
print("*"*100)
print(f'''
52) Genera un script en Python para revertir de minúsculas a mayúscus y cuseversa en el caso de que sea un string. 
En el caso que el string contenga solo decimales/digitos/numerico invierta el orden las strings. ''')
Entrada=['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
Salida=['CAT', 'CATATATATCTSA', 'ABCDEFHIJKLMNOP', '521581932952421', '', 'FOO', 'UNIQUE']
Entrada=['Green', 'Red', 'Orange', 'Yellow', '', 'White']
Salida=['gREEN', 'rED', 'oRANGE', 'yELLOW', '', 'wHITE']
Entrada=['Hello', '!@#', '!@#$', '123#@!']
Salida=['hELLO', '#@!', '$#@!', '!@#321']

Solucion="""
print()
"""
print("*"*100)
print(f'''
53) Genera un script en Python para encontrar el producto de los dígitos de las unidades en los números de una lista dada. ''')
Entrada=[12, 23]
Salida=6
Entrada=[12, 23, 43]
Salida=18
Entrada=[113, 234]
Salida=12
Entrada=[1002, 2005]
Salida=10
Solucion="""
print()
"""
print("*"*100)
print(f'''
54) Genera un script en Python para eliminar duplicados de una lista de enteros, conservando el orden. ''')
Entrada=[1, 3, 4, 10, 4, 1, 43]
Salida=[1, 3, 4, 10, 43]
Entrada=[10, 11, 13, 23, 11, 25, 23 , 76, 99]
Salida=[10, 11, 13, 23, 25, 76, 99]
Solucion="""
print()
"""
print("*"*100)
print(f'''
55) Genera un script en Python para encontrar los números que son mayores que 10 y tienen el primer y el último dígito impares. ''')
Entrada=[1, 3, 79, 10, 4, 1, 39, 62]
Salida=[79, 39]
Entrada=[11, 31, 77, 93, 48, 1, 57]
Salida=[ 11, 31, 77, 93, 57]
Solucion="""
print()
"""
print("*"*100)
print(f'''
56) Genera un script en Python para encontrar un exponente entero x tal que a^x = n. ''')
# ~ Entrada=
a = 2 
n = 1024
Salida=10
# ~ Entrada=
a = 3 
n = 81
Salida=4
# ~ Entrada=
a = 3 
n = 1290070078170102666248196035845070394933441741644993085810116441344597492642263849
Salida=170
Solucion="""
print()
"""
print("*"*100)
print(f'''
57) Genera un script en Python para encontrar la suma de las magnitudes de los elementos en el arreglo con un signo que sea igual al producto de los signos de las entradas. ''')
Entrada=[1, 3, -2]
Salida=-6
Entrada=[1, -3, 3]
Salida=-7
Entrada=[10, 32, 3]
Salida=45
Entrada=[-25, -12, -23]
Salida=-60
Solucion="""
print()
"""
print("*"*100)
print(f'''
58) Genera un script en Python para encontrar el mayor número par entre dos números inclusive. ''')
# ~ Entrada=
m = 12
n = 51
Salida=50
# ~ Entrada=
m = 1
n = 79
Salida=78
# ~ Entrada=
m = 47
n = 53
Salida=52
# ~ Entrada=
m = 100
n = 200
Salida=200
Solucion="""
print()
"""
print("*"*100)
print(f'''
59. Un nombre de archivo válido debe terminar en .txt, .exe, .jpg, .png o .dll, y debe tener como máximo tres dígitos, sin puntos adicionales) Genera un script en Python de Python para crear una lista de True/False que determine si el nombre de archivo candidato es válido o no. ''')
Entrada=['abc.txt', 'windows.dll', 'tiger.png', 'rose.jpg', 'test.py', 'win32.exe']
Salida=['Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí']
Entrada=['.txt', 'windows.exe', 'tiger.jpeg', 'rose.c', 'test.java ']
Salida=['No', 'Sí', 'No', 'No', 'No']
Solucion="""
print()
"""
print("*"*100)
print(f'''
60) Genera un script en Python para encontrar una lista de todos los números adyacentes a un número primo en la lista, ordenados sin duplicados. ''')
Entrada=[2, 17, 16, 0, 6, 4, 5]
Salida=[2, 4, 16, 17]
Entrada=[1, 2, 19, 16, 6, 4, 10]
Salida=[1, 2, 16, 19]
Entrada=[1, 2, 3, 5, 1, 16, 7, 11, 4]
Salida=[1, 2, 3, 4, 5, 7, 11, 16]
Solucion="""
print()
"""
print("*"*100)
print(f'''
61) Genera un script en Python para encontrar el número que, cuando se agrega a la lista, hace el total 0. ''')
Entrada=[1, 2, 3, 4, 5]
Salida=-15
Entrada=[-1, -2 , -3, -4, 5]
Salida=5
Entrada=[10, 42, 17, 9, 1315182, 184, 102, 29, 15, 39, 755]
Salida=-1316384
Solucion="""
print()
"""
print("*"*100)
print(f'''
62) Genera un script en Python para encontrar la clave del diccionario cuyo valor es diferente al de todas las demás claves. ''')
Entrada={'rojo': '', 'VERDE': '', 'azul': 'naranja'}
Salida='VERDE'
Entrada={'ROJO': '', 'VERDE': '', ' orange': '#125GD'}
Salida='orange'
Solucion="""
print()
"""
print("*"*100)
print(f'''
63) Genera un script en Python para encontrar la suma de los elementos pares que están en índices impares en una lista dada. ''')
Entrada=[1, 2, 3, 4, 5, 6, 7]
Salida=12
Entrada=[1, 2, 8, 3, 9, 4]
Salida=6
Solucion="""
print()
"""
print("*"*100)
print(f'''
64) Genera un script en Python para encontrar el string que consta de todas las palabras cuyas longitudes son números primos. ''')
Entrada='El veloz zorro marrón salta sobre el perro perezoso.'
Salida='El rápido zorro marrón salta'
Entrada='Efecto Omicron: Los vuelos extranjeros no se reanudarán el 15 de diciembre, decisión posterior.'
Salida='Efecto Omicron: los vuelos extranjeros no se realizarán el 15 de diciembre,'
Solucion="""
print()
"""
print("*"*100)
print(f'''
65) Genera un script en Python para desplazar los dígitos decimales n lugares a la izquierda, envolviendo los dígitos adicionales. Si shift > el número de dígitos de n, invierta el string. ''')
# ~ Entrada=
n = 12345 
turno = 1
# ~ Salida=
Resultado = 23451
# ~ Entrada=
n = 12345
turno = 2
# ~ Salida=
Resultado = 34512
# ~ Entrada=
n = 12345 
turno = 3
# ~ Salida=
Resultado = 45123
# ~ Entrada=
n = 12345 
turno = 5
# ~ Salida=
Resultado = 12345
# ~ Entrada=
n = 12345 
turno = 6
# ~ Salida=
Resultado = 54321
Solucion="""
print()
"""
print("*"*100)
print(f'''
66) Genera un script en Python para encontrar los índices del par más cercano de una lista de números. ''')
Entrada= [1, 7, 9, 2, 10]
Salida=[0, 3]
Entrada= [1.1, 4.25, 0.79, 1.0, 4.23]
Salida=[4, 1]
Entrada= [0.21, 11.3 , 2.01, 8.0, 10.0, 3.0, 15.2]
Salida=[2, 5]
Solucion="""
print()
"""
print("*"*100)
print(f'''
67) Genera un script en Python para encontrar un string que, cuando cada carácter se desplaza (ASCII incrementado)
 por desplazamiento, proporcione el resultado. ''')
# ~ Entrada=
# ~ tabla de caracteres ASCII
# ~ Shift = 1
# ~ Salida=
# ~ @rbhh bg`q`bsdq s`akd
# ~ Entrada='tabla de caracteres ASCII'
# ~ Shift = -1
# ~ Salida= 'Btdjj!dibsbdufs!ubcmf'
Solucion="""
print()
"""
print("*"*100)
print(f'''
68) Genera un script en Python para encontrar todos los 5 en números enteros menores que n que sean divisibles por 9 o 15. ''')
Entrada_Valor_de_n = 50
Salida=[[15, 1], [45, 1]]
Entrada_Valor_de_n  = 65
Salida= [[15, 1], [45, 1], [54, 0]]
Entrada_Valor_de_n  = 75
Salida= [[15, 1], [45, 1], [ 54, 0]]
Entrada_Valor_de_n = 85
Salida= [[15, 1], [45, 1], [54, 0], [75, 1]]
Entrada_Valor_de_n = 150
Salida= [[ 15, 1], [45, 1], [54, 0], [75, 1], [105, 2], [135, 2]]
Solucion="""
print()
"""
print("*"*100)
print(f'''
69) Genera un script en Python para crear una nueva string tomando un string y reorganizando palabra por palabra sus 
caracteres en orden ASCII. ''')
Entrada= 'tabla de caracteres Ascii'
Salida='Aciis aaccehrrt abelt'
Entrada= 'maltos won'
Salida='casi ahora'
Solucion="""
print()
"""
print("*"*100)
print(f'''
70) Genera un script en Python para encontrar el saldo registro negativo de una lista dada de números que representan 
depósitos y retiros bancarios. Imprime el saldo negativo en ese momento ''')
Entrada=[[12, -7, 3, -89, 14, 88, -78], [-1, 2, 7]]
Salida=[-81, -1]
Entrada=[[1200, 100, -900], [100, 100, -2400]]
Salida=[None, -2200]
Solucion="""
print()
"""
print("*"*100)
print(f'''
71. Dada una lista de números y un número para inyectar, escriba un programa Python para crear una lista que contenga ese
número entre cada par de números adyacentes. ''')
Entrada= [12, -7, 3, -89, 14, 88, -78, -1, 2, 7]
Separador: 6
Salida= [12, 6, -7, 6, 3, 6, -89, 6, 14, 6, 88, 6, -78, 6, -1, 6, 2, 6, 7]
Entrada=[1, 2, 3, 4, 5, 6]
Separador: 9
Salida=[ 1, 9, 2, 9, 3, 9, 4, 9, 5, 9, 6]
Solucion="""
print()
"""
print("*"*100)
print(f'''
72) Genera un script en Python para encontrar los índices de tres números que suman 0 en una lista dada de números. ''')
Entrada= [12, -7, 3, -89, 14, 4, -78, -1, 2, 7]
Salida=[1, 2, 5]
Entrada= [1, 2, 3, 4 , 5, 6, -7]
Salida=[2, 3, 6]
Solucion="""
print()
"""
print("*"*100)
print(f'''
73) Genera un script en Python para encontrar una substring en un string dada que contenga una vocal entre dos consonantes. ''')
Entrada='Hello'
Salida='Hel'
Entrada= 'Sandwich'
Salida='San'
Entrada= 'Python' 
Salida='hon'
Solucion="""
print()
"""
print("*"*100)
print(f'''
74) Genera un script en Python para encontrar un string que consista en caracteres separados por espacios con conteos dados. ''')
Entrada= {'f': 1, 'o': 2}
Salida='foo'
Entrada= {'a': 1, 'b': 1, 'c': 1}
Salida='abc'
Solucion="""
print()
"""
print("*"*100)
print(f'''
75) Genera un script en Python para reordenar los números de una matriz dada en orden creciente/decreciente 
en función de si el primer elemento más el último es par/impar. 
Reordenar los números de una matriz dada en orden creciente/decreciente en función de si el primer elemento 
más el último es par/impar.:''')
Entrada=[3, 7, 4]
Salida=[3, 4, 7]
Entrada=[ 2, 7, 4]
Salida=[7, 4, 2]
Entrada=[1, 5, 6, 7, 4, 2, 8]
Salida=[1, 2, 4, 5, 6, 7, 8]
Entrada=[1, 5, 6, 7, 4, 2, 9]
Salida=[9, 7, 6, 5, 4, 2, 1]
Solucion="""
print()
"""
print("*"*100)
print(f'''
76. Escribe un programa en Python para encontrar el índice del número primo más grande de la lista y la suma de sus dígitos. ''')
Entrada= [3, 7, 4]
Salida=[1, 7]
Entrada= [3, 11, 7, 17, 19, 4]
Salida=[4, 10]
Entrada= [23, 17, 201 , 14, 10473, 43225, 421, 423, 11, 10, 2022, 342157]
Salida=[6, 7]
Solucion="""
print()
"""
print("*"*100)
print(f'''
77) Genera un script en Python para convertir los GPA en calificaciones con letras de acuerdo con la siguiente tabla: ''')
'''
GPA	Los grados
4.0:	A+
3.7:	A
3.4:	A-
3.0:	B+
2.7:	B
2.4:	B-
2.0:	do+
1.7:	C
1.4:	C-
abajo:	F'''
Entrada=[4.0, 3.5, 3.8]
Salida=['A+', 'A-', 'A']
Entrada=[5.0, 4.7, 3.4, 3.0, 2.7, 2.4, 2.0, 1.7, 1.4, 0.0]
Salida=['A+', 'A+', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'F']
Solucion="""
print()
"""
print("*"*100)
print(f'''
78) Genera un script en Python para encontrar los dos números distintos más cercanos en una lista de números dada. ''')
Entrada=[1.3, 5.24, 0.89, 21.0, 5.27, 1.3]
Salida=[5.24, 5.27]
Entrada=[12.02, 20.3, 15.0, 19.0, 11.0, 14.99, 17.0, 17.0, 14.4, 16.8]
Salida :[14.99, 15.0]
Solucion="""
print()
"""
print("*"*100)
print(f'''
79) Genera un script en Python para encontrar los números negativos más grandes y los números positivos más pequeños (o 0 si ninguno). ''')
Entrada=[-12, -6, 300, -40, 2, 2, 3, 57, -50, -22, 12, 40, 9, 11, 18]
Salida=[-6, 2]
Entrada=[-1, -2, -3, -4]
Salida=[-1, 0]
Entrada=[1, 2, 3, 4]
Salida=[0, 1]
Entrada=[]
Salida=[0, 0]
Solucion="""
print()
"""
print("*"*100)
print(f'''
80) Genera un script en Python para redondear cada flotante en una lista dada de números hasta el siguiente entero y devuelva el total acumulado de los cuadrados enteros. ''')
Entrada= [2.6, 3.5, 6.7, 2.3, 5.6]
Salida=[9, 25, 74, 83, 119]
Entrada= [301.1, 401.4, -23.1, 13554122.0, 10201.0101, 10000000.0]
Salida=[91204 , 252808, 253337, 183714223444221, 183714327525025, 283714327525025]
Solucion="""
print()
"""
print("*"*100)
print(f'''
81) Genera un script en Python para calcular el promedio de los números a a b (b no incluido) redondeado al entero más cercano, en binario (o -1 si no hay tales números). ''')
Entrada=4 , 7
Salida=0b101
Entrada=11 , 19
Salida=0b1110
Solucion="""
print()
"""
print("*"*100)
print(f'''
82) Genera un script en Python para encontrar la sublista de números de una lista dada de números con solo dígitos impares en orden creciente. ''')
Entrada=[1, 3, 79, 10, 4, 2, 39]
Salida=[1, 3, 39, 79]
Entrada=[11, 31, 40, 68, 77, 93, 48, 1 , 57]
Salida=[1, 11, 31, 57, 77, 93]
Entrada=[9, -2, 3, 4, -2, 0, 2, -3, 8, -1]
Salida=[-3 , -1, 3, 9]
Solucion="""
print()
"""
print("*"*100)
print(f'''
83. un string es feliz si cada tres caracteres consecutivos son distintos. 
Escriba un programa de Python para encontrar dos índices que hagan infeliz a un string determinada. ''')
Entrada='Python'
Salida='Ninguna'
Entrada='Descontento'
Salida=[4, 5]
Entrada='Buscar'
Salida='Ninguna'
Entrada='Calle'
Salida=[3, 4]
Solucion="""
print()
"""
print("*"*100)
print(f'''
84) Genera un script en Python para encontrar el índice de los paréntesis coincidentes para cada carácter en un string dada. ''')
Entrada= '()(())'
Salida=[1, 0, 5, 4, 3, 2]
Entrada= '()()()'
Salida=[1, 0, 3, 2, 5, 4]
Entrada= '((()))'
Salida=[5, 4, 3, 2, 1, 0]
Solucion="""
print()
"""
print("*"*100)
print(f'''
85) Genera un script en Python para encontrar una secuencia creciente que consista en los elementos de la lista original. ''')
Entrada=[1, 3, 79, 10, 4, 2, 39]
Salida=[1, 2, 3, 4, 10, 39, 79]
Entrada=[11, 31, 40, 68, 77 , 93, 48, 1, 57]
Salida=[1, 11, 31, 40, 48, 57, 68, 77, 93]
Entrada=[9, -2, 3, 4, -2, 0, 2, - 3, 8, -1]
Salida=[-3, -2, -1, 0, 2, 3, 4, 8, 9]
Solucion="""
print()
"""
print("*"*100)
print(f'''
86) Genera un script en Python para encontrar las vocales de cada uno de los textos originales (y cuenta como una vocal al final de la palabra) de una lista dada de strings. ''')
Entrada= ['Python', 'es', 'Genial', 'play','ball']
Salida=['o', 'e', 'eia', 'ay','a']
Entrada= [ 'ably', 'abruptly ', 'abecedary', 'aparentemente', 'reconocidamente']
Salida=['ay', 'auy', 'aeeay', 'aaey', 'aoeey']
Solucion="""
print()
"""
print("*"*100)
print(f'''
87) Genera un script en Python para encontrar una substring válida de un string dada que contenga paréntesis coincidentes, al menos uno de los cuales esté anidado. ''')
Entrada=']][][[]]]'
Salida='[[]]'
Entrada=']]]]]]]]]]]]]]]]][][][][]]] ]]]]]]]][[[][[][[[[[][][][]][[[[[[[[[[[[[[[[[['
Salida='[[ ][][][]]'
Solucion="""
print()
"""
print("*"*100)
print(f'''
88) Genera un script en Python para encontrar un número entero (n >= 0) con el número dado de dígitos pares e impares. ''')
Entrada='Número de dígitos pares: 2, Número de dígitos impares: 3'
Salida=22333
Entrada='Número de dígitos pares: 4, Número de dígitos impares: 7'
Salida=22223333333
Solucion="""
print()
"""
print("*"*100)
print(f'''
89) Genera un script en Python para encontrar todos los números enteros <= 1000 que sean el producto de exactamente tres números primos. Cada número entero debe representarse como la lista de sus tres factores primos. ''')
Entrada= 10
Salida=[[2, 2, 2]]
Entrada= 50
Salida=[[2, 2, 2], [2, 2, 3], [2, 2, 5], [2 , 2, 7], [2, 2, 11], [2, 3, 2], [2, 3, 3], [2, 3, 5], [2, 3, 7], [2, 5 , 2], [2, 5, 3], [2, 5, 5], [2, 7, 2], [2, 7, 3], [2, 11, 2], [3, 2, 2 ], [3, 2, 3], [3, 2, 5], [3, 2, 7], [3, 3, 2], [3, 3, 3], [3, 3, 5], [3, 5, 2], [3, 5, 3], [3, 7, 2], [5, 2, 2], [5, 2, 3], [5, 2, 5], [5 , 3, 2], [5, 3, 3], [5, 5, 2], [7, 2, 2], [7, 2, 3], [7, 3, 2], [11, 2 , 2]]
Solucion="""
print()
"""
print("*"*100)
print(f'''
90. Por cada triple de comido, necesita, escriba un programa de Python para obtener un par de apetito total y restante. ''')
Entrada=[[2, 5, 6], [3, 9, 22]]
Salida=[[7, 1], [12, 13]]
Entrada=[[2, 3, 18], [ 4, 9, 2], [2, 5, 7], [3, 8, 12], [4, 9, 106]]
Salida=[[5, 15], [6, 0], [7, 2 ], [11, 4], [13, 97]]
Entrada=[[1, 2, 3], [4, 5, 6]]
Salida=[[3, 1], [9, 1]]
Solucion="""
print()
"""
print("*"*100)
print(f'''
91) Genera un script en Python para encontrar todos los números enteros de n dígitos que comiencen o terminen con 2. ''')
Entrada= 1
Salida=[2]
Entrada= 2
Salida=[12, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 32, 42, 52, 62, 72, 82, 92]
Entrada= 3
Salida=[102, 112, 122, 132, 142, 152, 162, 172, 182, 192, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 302, 312, 322, 332, 342, 352, 362, 372, 382, 392, 402, 412, 422, 432, 442, 452, 462, 472, 482, 492, 502, 512, 522, 532, 542, 552, 562, 572, 582, 592, 602, 612, 622, 632, 642, 652, 662, 672, 682, 692, 702, 712, 722, 732, 742, 752, 762, 772, 782, 792, 802, 812, 822, 832, 842, 852, 862, 872, 882, 892, 902, 912, 922, 932, 942, 952, 962, 972, 982, 992]
Solucion="""
print()
"""
print("*"*100)
print(f'''
92) Genera un script en Python para comenzar con una lista de números enteros, mantenga todos los demás elementos en su lugar y ordene la lista. ''')
Entrada=[2, 5, 6, 3, 1, 4, 34]
Salida=[1, 5, 2, 3, 6, 4, 34]
Entrada=[8, 0, 7, 2, 9 , 4, 1, 2, 8, 3]
Salida=[1, 0, 7, 2, 8, 4, 8, 2, 9, 3]
Solucion="""
print()
"""
print(f'''
93) Genera un script en Python para encontrar el palíndromo más cercano de un string dado. ''')
Entrada='cat'
Salida='cac'
Entrada='madan'
Salida='madam'
Entrada='radivider'
Salida='radividar'
Entrada='madan'
Salida='madam'
Entrada='abc'
Salida='aba'
Entrada='racecbr'
Salida='racecar'
Solucion="""
print()
"""
print("*"*100)
print(f'''
94. Dada un string que consta de espacios en blanco y grupos de paréntesis coincidentes, escriba un programa Python para dividirla en grupos de paréntesis perfectamente coincidentes sin ningún espacio en blanco. ''')
Entrada='( ()) ((()()())) (()) ()'
Salida=['(())', '((()()()))', ' (())', '()']
Entrada='() (( ( )() ( )) ) ( ())'
Salida=['()', '((()()()))', '(())']
Solucion="""
print()
"""
print("*"*100)
print(f'''
95) Genera un script en Python para encontrar un palíndromo de una longitud dada que contenga un string dada. ''')
Entrada= 'señora' , 7
Salida='señora'
Entrada= 'señora' , 6
Salida='señora'
Entrada= 'señora' , 5
Salida='señora'
Entrada= 'señora' , 3
Salida='señora'
Entrada= 'señora' , 2
Salida='mm'
Entrada= 'señora' , 1
Salida='aa'
Solucion="""
print()
"""
print("*"*100)
print(f'''
96) Genera un script en Python para obtener los dígitos individuales en números ordenados al revés y convertidos a palabras. ''')
Entrada=[1, 3, 4, 5, 11]
Salida=['cinco', 'cuatro', 'tres', 'uno']
Entrada=[27, 3, 8, 5, 1, 31 ]
Salida=['ocho', 'cinco', 'tres', 'uno']
Solucion="""
print()
"""
print("*"*100)
print(f'''
97) Genera un script en Python para encontrar el siguiente tipo extraño de lista de números: el primer elemento es el más pequeño, 
el segundo es el más grande de los restantes, el tercero es el más pequeño de los restantes, el cuarto es el más pequeño de los restantes , etc. ''')
Entrada=[1, 3, 4, 5, 11]
Salida=[1, 11, 3, 5, 4]
Entrada=[27, 3, 8, 5, 1, 31]
Salida=[1, 31, 3, 27, 5, 8]
Entrada=[1, 2, 7, 3, 4, 5, 6]
Salida=[1, 7, 2, 6, 3, 5, 4]
Solucion="""
print()
"""
print("*"*100)
print(f'''
98. Dada un string que consta de grupos de paréntesis anidados separados por paréntesis, 
escriba un programa en Python para calcular la profundidad de cada grupo. ''')
Entrada= '(()) (()) () ((()()()))'
Salida=[2, 2, 1, 3]
Entrada= '() (()) () () ( ) ()'
Salida=[1, 2, 1, 1, 1, 1]
Entrada= '(((((((()))))))) () (()) ((()()() ))'
Salida=[8, 1, 2, 3]
Solucion="""
print()
"""
print("*"*100)
print(f'''
99) Genera un script en Python para encontrar un string tal que, cuando tres o más espacios se compriman en un '-'
y uno o dos espacios se reemplacen por guiones bajos, conduzca al objetivo. ''')
Entrada='Python-Ejercicios'
Salida='Python Ejercicios'
Entrada='Python_Ejercicios'
Salida='Python Ejercicios'
Entrada='-¡Hola,_mundo!__¡Esto_es-tan-fácil!-'
Salida='¡Hola, mundo! ¡Esto es tan fácil!'
Solucion="""
print()
"""
print("*"*100)
print(f'''
100) Genera un script en Python para encontrar cuatro enteros pares positivos cuya suma sea un entero dado. ''')
# ~ Entrada
n = 100
Salida=[94, 2, 2, 2]
# ~ Entrada:
n = 1000
Salida=[994, 2, 2, 2]
# ~ Entrada:
n = 10000
Salida=[9994, 2, 2, 2]
# ~ Entrada:
n = 1234567890
Salida=[1234567884, 2, 2, 2]
