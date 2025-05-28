print('''
● Reto : 
        Ha sido contratado por un importante fabricante de reproductores de MP3 para implementar un nuevo estándar de compresión de música. 
        En este kata implementará el CODIFICADOR, y su kata complementario se ocupa del DECODIFICADOR. 
        Puede considerarse una versión más difícil de Range Extraction. 
        Especificación La señal de entrada se representa como una matriz de números enteros. 
        Se pueden acortar varios casos de regularidades. 
        Una secuencia de 2 o más números idénticos se acorta como número*cuenta 
        Una secuencia de 3 o más números consecutivos se acorta como el primero al último. 
            Esto es cierto tanto para el orden ascendente como para el descendente. 
        Una secuencia de 3 o más números con el mismo intervalo se acorta como primero-último/intervalo. 
        Tenga en cuenta que el intervalo NO necesita un signo La compresión ocurre de izquierda a derecha.
        
        
         Ejemplos    [1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20] 
                            se comprime a "1,3-5,7-11,14,15,17 -20" 
                     [0, 2, 4, 5, 7, 8, 9] 
                            se comprime a "0-4/2,5,7-9" 
                     [0, 2, 4, 5, 7, 6, 5] 
                            se comprime a "0-4/2,5,7-5" 
                     [0, 2, 4, 5, 7, 6, 5, 5, 5, 5, 5] 
                            se comprime a "0-4/2,5,7-5,5*4" 
Aporte Una matriz no vacía de enteros Producción Una cadena de enteros separados por comas y descriptores de secuencia
​
''')
from __init__ import *
limpiar()
print(f'''
● 
''')

def compress(raw):
    # Your code here!
    salida=[]
    for index in range(0,len(raw-1)):
        if raw[index]==raw[index+1]:
            raw[index] = raw[index]+"*2"
            del raw[index+1]
        
        if  '*' in raw[index]:
            if raw[index+1]==raw[index][1]:
                raw[index][2]+=1
    for index in range(0,len(raw-1)):
        dif=raw[index]-raw[index+1]
        if raw[index+1]-raw[index+2]==dif:
            raw[index]=raw[index]+"/3"
        
        
        
TESTS = (("2 identical numbers", [1,2,2,3],"1,2*2,3"),
         ("3 consecutive numbers, ascending", [1,3,4,5,7],"1,3-5,7"),
         ("3 consecutive numbers, descending", [1,5,4,3,7],"1,5-3,7"),
         ("3 numbers with same interval, descending", [1,10,8,6,7],"1,10-6/2,7"))

for txt,descodif,codif in TESTS:
    salida=compress (descodif)
    if salida == codif:
        print (f"{txt}:\n\t\tok")
    else:#if salida == codif:
        print (f"{txt}:\n\t\tError")


