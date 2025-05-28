
'''
DESAFIO N~0
 * "FIZZ BUZZ"
 * Dificultad: BAJA     FUENTE Brais Moure
Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 ( incluidos)

sustituyendo los siguientes:
  - Múltiplos de 3 por la palabra "fizz".
  - Múltiplos de 5 por la palabra "buzz".
  - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
    1) Imprime cada dato en una misma linea
    2) crea una lista e imprimela al final
    3) crea un diccionario con clave str de números y valor en fizz / buzz o números  e imprimela al final
'''
##Solucion


4





rango= range(1,101,1)
print(f"{rango=}\n{type(rango)}\n{list(rango)}")
lista=[]#item 2
dic={}#item 3
for cada_dato in rango:
    if cada_dato%3==0 and cada_dato%5!=0:
        salida="fizz"
    elif cada_dato%3!=0 and cada_dato%5==0:
        salida="buzz"
    elif cada_dato%3==0 and cada_dato%5==0:
        salida="fizzbuzz"
    else:
        salida=cada_dato
    print (f" {salida}, ",end="")# item 1
    lista.append(salida)#item 2
    dic[str(cada_dato)]=salida #item 3
    # ~ dic[str(cada_dato-1)]=salida-1 if isinstance(salida,int) else salida #item 3
    
    
print(f"\n\n\n{lista=}" )#item 2
print(f"\n\n\n{dic=}" )#item 3
exit()







for index in range(1,101):
    divisibleByThree = index % 3 == 0
    divisibleByFive = index % 5 == 0
    lista=[]
    dic={}
    if (divisibleByThree is True and  divisibleByFive is True):
        salida="fizzbuzz"
    elif (divisibleByThree is True):
        salida="fizz"
    elif (divisibleByFive is True):
        salida="buzz"
    else :
        salida=index
    print(f"dato en index {index} es {salida}")
    lista.append(salida)
    dic[str(index)]=salida
print (f"{lista=}")
print (f"{dic=}")
####################################################################################3


def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)

fizzbuzz()
