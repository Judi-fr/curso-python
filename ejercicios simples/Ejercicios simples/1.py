
'''
 * "FIZZ BUZZ"
Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 ( incluidos_

sustituyendo los siguientes:
  - Múltiplos de 3 por la palabra "fizz".
  - Múltiplos de 5 por la palabra "buzz".
  - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
    1) cada dato en una misma linea
    2) crea una lista
    3) crea un diccionario con clave str de index y valor en fizz / buzz o index
'''

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
