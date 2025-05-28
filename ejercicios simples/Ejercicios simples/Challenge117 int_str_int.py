print(f'''
●  Se le pide que eleve al cuadrado cada dígito de un número y los concatene.

Por ejemplo, si ejecutamos 9119 a través de la función, saldrá 811181, porque 9 2 es 81 y 1 2 es 1.

Nota: La función acepta un número entero y devuelve un número entero
''')
def square_digits(num):
    s=""
    for n in str(num):
       s=s+str(int(n)**2)
    return int(s)
print(square_digits(9119))
#-----------------------------------------------------------------------------
def square_digits(num):
    return int("".join([str(int(n)**2) for n in str(num)]))

print(square_digits(9119))
'''
Un cuadrado de cuadrados
Te gustan los bloques de construcción. Te gustan especialmente los bloques de construcción que son cuadrados. ¡Y lo que más te gusta es organizarlos en un cuadrado de bloques de construcción cuadrados!

Sin embargo, a veces, no puedes organizarlos en un cuadrado. En cambio, ¡terminas con un rectángulo ordinario! ¡Esas malditas cosas! Si solo tuviera una manera de saber si actualmente está trabajando en vano ... ¡Espere! ¡Eso es! Solo tiene que verificar si su número de bloques de construcción es un cuadrado perfecto.

Tarea
Dado un número integral, determine si es un número cuadrado:

En matemáticas, un número cuadrado o cuadrado perfecto es un número entero que es el cuadrado de un número entero; en otras palabras, es el producto de algún número entero consigo mismo.

Las pruebas serán siempre use algún número integral, así que no se preocupe por eso en lenguajes dinámicos escritos.

Ejemplos
-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false
isSquare (-1) // => false
isSquare   3  // => false
isSquare   4  // => true
isSquare  25  // => true
isSquare  26  // => false
'''
def is_square(n):
    if int(abs(n)**(1/2)) == (n**(1/2))  :
        return True  
    return False 
    
for l in [-1,0,3,4,25,26]:
    print (l,is_square(l))
#-----------------------------------------------------------------------------
print("-"*20,":)")
def is_square(n):
    return n >= 0 and (n**0.5) % 1 == 0
for l in [-1,0,3,4,25,26]:
    print (l,is_square(l))
#-----------------------------------------------------------------------------
print("-"*20,":)")
def is_square(n):    
    return n>=0 and (n**0.5).is_integer()
for l in [-1,0,3,4,25,26]:
    print (l,is_square(l))
#-----------------------------------------------------------------------------
print("-"*20,":)")
'''
Implemente una función que agregue dos números y devuelva su suma en binario. La conversión se puede hacer antes o después de la adición.
El número binario devuelto debe ser una cadena.
Ejemplos: ( Input1, Input2 - > Salida ( explicación ) ) )

1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
'''
def add_binary(a,b):
    return format((a+b),'b')
for par in [[1, 1],[5, 9]]:
    print(add_binary(par[0],par[1]))
#-----------------------------------------------------------------------------
def add_binary(a,b):
    return bin(a+b)[2:]
for par in [[1, 1],[5, 9]]:
    print(add_binary(par[0],par[1]))
#-----------------------------------------------------------------------------
def add_binary(a,b):
    return f"{a + b:b}"
for par in [[1, 1],[5, 9]]:
    print(add_binary(par[0],par[1]))
#-----------------------------------------------------------------------------
print("-"*20,":)")
#-----------------------------------------------------------------------------
'''
Antecedentes
Se puede hacer un análisis estadístico simple de una serie de muestras con un Resumen de cinco figuras.

El resumen de cinco cifras proporciona el cuartil inferior extremo, superior extremo, inferior, mediano y superior, 
todo derivado de los datos de muestra suministrados.

Confusamente, el resumen de cinco cifras a menudo incluye un sexto valor, que es el número de muestras en la serie.

Kata
En este Kata se le dará un esquema de clase para completar. 
La clase se instanciará con una secuencia de valores, y debe implementar el método para devolver la versión de seis cifras de un resumen de cinco cifras.

¡Se espera que haga los cálculos usted mismo, usar pandas o numpy le dará un ceño entrecerrado de su sensei! : )

Entradas
En la instanciación de clase se le dará una secuencia de valores. Esta secuencia puede contener valores no numéricos: estos deben ignorarse.
En la creación de resumen, se le dará un número máximo de dígitos decimales precision para todos los resultados numéricos. Si None se suministra, suponiendo que se debe devolver la precisión total.
Cálculos
N: Número de valores numéricos válidos en la secuencia.
Lower Extreme: el valor más pequeño contenido dentro de la secuencia.
Upper Extreme: el valor más grande contenido dentro de la secuencia.
Mediana: el valor central de la secuencia ordenada de valores válidos.
Cuartil inferior: el valor límite entre el primer y el segundo trimestres de la secuencia ordenada de valores válidos.
Cuartil superior: el valor límite entre el tercer y cuarto trimestres de la secuencia ordenada de valores válidos.
La mediana y ambos cuartiles pueden necesitar una interpolación lineal entre dos valores.

Ejemplos de interpolación lineal
Dada una secuencia de valores [2, 3, 4, 5, 6, 7, 8, 9]

Posición 3.5 devolvería el punto medio entre los valores en el índice 3 e índice 4 regresando 5.5.
Posición 1.25 devolvería el cuarto de punto entre los valores en el índice 1 e índice 2 regresando 3.25.
Posición 6.75 devolvería el punto de tres cuartos entre los valores en el índice 6 e índice 7 regresando 7.75.
Salidas
Devolverá una tupla con los valores calculados en el siguiente orden:

(N, lower_extreme, upper_extreme, lower_quartile, median, upper_quartile)
Cuando no se define precisión y se dan los errores de redondeo / cuantización con el procesamiento de coma flotante, sus respuestas deben estar dentro 10 ** -10 de la respuesta correcta. Cuando se define la precisión, se espera que su respuesta sea exacta.

Ejemplo trabajado
data = range(0, 7)
StatisticalSummary(data).five_figure_summary(2)   =>   (7, 0, 6, 1.5, 3, 4.5)

# Serie
Este kata es parte de una serie de kata sobre estadísticas básicas, se recomienda abordarlos en secuencia.

Los kata son:

Introducción a las estadísticas - Parte 1: Un resumen de cinco cifras
Introducción a las estadísticas - Parte 2: Parcelas
'''  
