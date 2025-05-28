'''
Ejercicio
Las matemáticas financieras, resumidas en una frase, las podríamos definir como la rama de las matemáticas que estudia los flujos de dinero a través del tiempo. Básicamente se presupone que el dinero tiene menos valor en el futuro que en el presente, ya sea por un tema inflacionario o por la preferencia natural de las personas a priorizar el consumo presente.

El valor futuro es el valor alcanzado por un determinado capital al final del período determinado (para el ejemplo usaremos la fórmula del interés compuesto). Para calcularlo se utiliza la siguiente fórmula

El valor presente de una inversión es cuando calculamos el valor actual que tendrá una determinada cantidad que recibiremos o pagaremos en un futuro. Para calcularlo se utiliza la siguiente fórmula

 
Donde  es el valor futuro,  es el valor actual o inicial de la inversión,  es el tipo de interés y  es número de años de la inversión.

Crear una función que reciba como entrada un capital, un tipo de interés y un número de años, y muestre por pantalla el valor futuro de la inversión cada año del periodo indicado.
Crear una función que reciba como entrada un capital, un tipo de interés y un número de años, y muestre por pantalla el valor actual del capital cada año del periodo indicado.
Ejemplo de ejecución

# ~ Introduce un capital: 1000
# ~ Introduce un tipo de interés: 10
# ~ Introduce un número de años: 3
# ~ VALOR FUTURO
# ~ Año 0 : 1100.0
# ~ Año 1 : 1210.0000000000002
# ~ Año 2 : 1331.0000000000005
# ~ VALOR ACTUAL
# ~ Año 0 : 909.090909090909
# ~ Año -1 : 826.4462809917354
# ~ Año -2 : 751.3148009015775
# ~ Solución
'''
def vf(capital, tipo, periodo):
    '''
    Función que muestra por pantalla el valor futuro de una inversión cada año de un periodo dado.
    Parámetros: 
        - capital: Es un real con el capital inicial de la inversión.
        - tipo: Es un real con el tipo de interés anual.
        - periodo: Es un entero con el número de años de la inversión.
    '''
    print(f"VALOR FUTURO=")
print(f"VALOR ACTUAL= {va(cantidad, tipo, años)}")
    # Bucle iterativo para recorrer la secuencia de años.
    for i in range(periodo):
        # Aplicamos la fórmula para el cálculo del valor futuro para cada año i. 
        print(f"Año {i}: {capital / (1 + tipo / 100) ** (i + 1)}")
    return
 
def va(capital, tipo, periodo):
    '''
    Función que muestra por pantalla el valor actual de una inversión cada año de un periodo dado.
    Parámetros: 
        - capital: Es un real con el capital final de la inversión.
        - tipo: Es un real con el tipo de interés anual.
        - periodo: Es un entero con el número de años de la inversión.
    ''' 
    print(f"VALOR ACTUAL= ")
    # Bucle iterativo para recorrer la secuencia de años.
    for i in range(periodo): 
         # Aplicamos la fórmula para el cálculo del valor actual para cada año i. 
        print(f"Año {-i}: {capital / (1 + tipo / 100) ** (i + 1)}")
    return

# Ejemplo
cantidad=""
while cantidad.replace(".","").isdecimal() is False:
    cantidad = input("Introduce un capital: ")
cantidad = float (cantidad)  
tipo=""
while tipo.replace(".","").isdecimal() is False:
    tipo = input("Introduce un tipo de interés: ")
tipo = float (tipo)  
años=""
while años.isdecimal() is False:
    años = input("Introduce un número de años: ")
años = int (años)  
vf(cantidad, tipo, años)
va(cantidad, tipo, años)

