from __init__ import *
limpiar()
print(f'''
● Esta Matriz es magica

Todas las matrices con las que trabajamos en este problema serán matrices con elementos reales. 
Una tal matriz se dice que es mágica sí y sólo si son iguales la ocho sumas:
                [4,3,8],
                [9,5,1],
                [2,7,6] 
                la suma de los registro de cada   filas  da 15 (4+3+8=15) (9+5+1=15) (2+7+6=15)
                la suma de los registro de cada columnas da 15 (4+9+2=15) (3+5+7=15) (8+1+6=15)
                la suma de los registro de cada diagonal da 15 (4+5+6=15) (8+5+2=15) 
has un script para :
        1) crear una matriz de n por n
        2) cargar la matriz
        3) chequear si es o no es magica
        
constructor:
    [
        [ m+3, m-4, m+1],
        [ m-2,   m, m+2],               siendo m un número natural mayor que 4
        [ m-1, m+4, m-3]
    ] 
        
        
        
''')
##sulucion

#-------EJERCICIO 1 -------

def creador(): # crea la matriz NxN que necesitamos
    while True:
        try:
            n=int(input("Ingrese un numero para realizar una matriz cuadrada: "))
            while not (0<n and 10>n):
                n=int(input("Ingrese un numero para realizar una matriz cuadrada: "))
            matriz=[[0]*n for i in range(n)]
            break
        except: 
            print ("solo numeros")
    return matriz
	
def cargador(matriz): # carga la matriz NxN 
	for i in range(len(matriz)):
		for j in range(len(matriz)):
			matriz[i][j]= int(input(f"Ingrese el numero para la posicion {i};{j} : "))
	return matriz

def comprobador(cargada_NxN): # carga la matriz NxN 
    sumador_filas=[]
    sumador_col=[]
    sumador_diag_alfa=[]  
    sumador_diag_beta=[]
    n=len(cargada_NxN)
    for index in range(n):
        suma_F=sum(cargada_NxN[index])#lista
        sumador_filas.append(suma_F)
        suma_C =0
        for index_sub in range(n):
            suma_C +=cargada_NxN[index_sub][index]#es un entero
            # ~ print (f"{cargada_NxN[index_sub][index]=}  {index_sub=}    {index=}")
        sumador_col.append(suma_C)
        sumador_diag_alfa.append(cargada_NxN[index][index])
        sumador_diag_beta.append(cargada_NxN[index][n-index-1])
    
    print(f'''
    sumador_filas = {sumador_filas}
    sumador_col   = {sumador_col}
    diagonal Alfa = {sum(sumador_diag_alfa)}  => {(sumador_diag_alfa)}
    diagonal Beta = {sum(sumador_diag_beta)}  => {(sumador_diag_beta)}
    ''')    
        
    for index in range(1,n):
        if not (sumador_filas[index-1]==sumador_filas[index] and sumador_col[index-1]==sumador_col[index] ):
            return False
    if  not(sum(sumador_diag_alfa)==sum(sumador_diag_beta) and sumador_diag_alfa!=sumador_filas[0] and sumador_diag_beta!=sumador_filas[0]):
        return False
    else:
        return True
        
        
cargada_NxN = [ 
                [4,3,8],
                [9,5,1],
                [2,7,6] 
            ]
# ~ cargada_NxN = [
                # ~ [8,1,6],
                # ~ [3,5,7],
                # ~ [4,9,2]
            # ~ ]

            
# ~ cargada_NxN = [
                # ~ [16, 3, 2,13],
                # ~ [ 5,10,11, 8],
                # ~ [ 9, 6, 7,12],
                # ~ [ 4,15,14, 1]
            # ~ ]
# ~ cargada_NxN = [
                # ~ [16, 2, 3,13],
                # ~ [ 5,11,10, 8],
                # ~ [ 9, 7, 6,12],
                # ~ [ 4,14,15, 1]
            # ~ ]
# ~ cargada_NxN = [
                # ~ [ 4,14,15, 1],
                # ~ [ 9, 7, 6,12],
                # ~ [ 5,11,10, 8],
                # ~ [16, 2, 3,13]
            # ~ ]

# ~ cargada_NxN = [
                # ~ [17,24, 1, 8,15],
                # ~ [23, 5, 7,14,16],
                # ~ [ 4, 6,13,20,22],
                # ~ [10,12,19,21, 3],
                # ~ [11,18,25, 2, 9]
            # ~ ]
# ~ cargada_NxN = [
                # ~ [64, 2, 3,61,60, 6, 7,57],
                # ~ [ 9,55,54,12,13,51,50,16],
                # ~ [17,47,46,20,21,43,42,24],
                # ~ [40,26,27,37,36,30,31,33],
                # ~ [32,34,35,29,28,38,39,25],
                # ~ [41,23,22,44,45,19,18,48],
                # ~ [49,15,14,52,53,11,10,56],
                # ~ [ 8,58,59, 5, 4,62,63, 1]
            # ~ ]

salida=comprobador(cargada_NxN)
if salida is True:
    print ("es matriz magica")
else:
    print ("no es matriz magica")



matriz_NxN=creador()
print("La matriz es: /n", matriz_NxN)
cargada_NxN=cargador(matriz_NxN)
print("La matriz cargada es: /n", cargada_NxN)
salida=comprobador(cargada_NxN)
if salida is True:
    print ("es matriz magica")
else:
    print ("no es matriz magica")
