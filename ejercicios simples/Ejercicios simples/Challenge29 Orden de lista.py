
'''
DESAFIO N~'29
 * ORDENA LA LISTA
 * Dificultad: FÁCIL
 *
Enunciado: Crea una función que ordene y retorne una matriz de números.
  - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro adicional
     o "Desc" para indicar si debe ordenarse de menor a mayor o de mayor a menor.
  - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
'''


lista = [1,7,0,4,9,6,4,2,44,67,3,8,5,32,2,31,34,54,6,7,8,9,40,30,20,3,50,98,5,65]
lista2=lista.copy()
original=lista.copy()
limite = max(lista)
#           opcion 1
"""
for index in range(0,len(lista)-1,1):
    numero_actual = lista[index]
    numero_siguiente = lista[index+1]
    print (f" compato {numero_actual} con {numero_siguiente}")
    if numero_actual<numero_siguiente:
 
        temp = numero_actual
        numero_actual= numero_siguiente
        numero_siguiente=temp
        print (f"\t\t cambio {numero_actual} con {numero_siguiente}") 
"""
#           opcion 2
"""
for index in range(0,len(lista)-1,1):
    for index in range(0,len(lista)-1,1):
        print (f" compato {lista[index]} con {lista[index+1]}")
        if lista[index]<lista[index+1]:
            # ~ lista[index]=lista[index+1]
            # ~ lista[index+1]=lista[index]
            '''
            temp = lista[index]
            lista[index]= lista[index+1]
            lista[index+1]=temp
            del temp
            '''
            lista[index],lista[index+1]= lista[index+1],lista[index]
            print (f"\t\t cambio {lista[index]} con {lista[index+1]}")

print (f"\t\t original {original} ")
print (f"\t\t cambio   {lista} ")
"""

#           opcion 3
# ~ """
cambio = True
contador=0
# ~ lista = [9,8,7,6,5,4,3,2,1]
# ~ lista = [1,2,3,4,5,6,7,8,9]
#while flag is False :
lista = [1,7,0,4,9,6,4,2,44,67,3,8,5,32,2,31,34,54,6,7,8,9,40,30,20,3,50,98,5,65]

inicio = 0
limite_final=len(lista)
step=1
rango = range(inicio, limite_final, step)

print (f"{rango=} {list(rango)=}")


inicio = len(lista)-1
limite_final=0-1
step=-1
rango = range(inicio, limite_final, step)

print (f"{rango=} {list(rango)=}")






while  cambio is True :
    cambio = False
    for index in range(0,len(lista)-1,1):
        print (f" compato {lista[index]} con {lista[index+1]}")
        if lista[index]<lista[index+1]:
            cambio = True
            lista[index],lista[index+1]= lista[index+1],lista[index]
            print (f"\t\t cambio {lista[index]} con {lista[index+1]}")
            contador+=1

    print ("*"*50)
print (f"\t\t original {original} ")
print (f"\t\t cambio   {lista} ")

print (f"\t\t cambio de mayor a menor    {lista} ")
# ~ """

cambio = True
contador=0
# ~ lista2 = [9,8,7,6,5,4,3,2,1]
# ~ lista2 = [1,2,3,4,5,6,7,8,9]
#while flag is False :
while  cambio is True :
    cambio = False
    for index in range(0,len(lista2)-1,1):
        print (f" compato {lista2[index]} con {lista2[index+1]}")
        if lista2[index]>lista2[index+1]:
            cambio = True
            lista2[index],lista2[index+1]= lista2[index+1],lista2[index]
            print (f"\t\t cambio {lista2[index]} con {lista2[index+1]}")
            contador+=1

    print ("*"*50)
print (f"\t\t original {original} ")

print (f"\t\t cambio   {lista2} ")

print (f"\t\t cambios   {contador} ")






#           opcion 4

print (f"\t\t original {original} ")
lista.sort()
print (f"\t\t cambio de menor a mayor   {lista} ")

lista2=lista.copy()
lista2.sort(reverse=True)
print (f"\t\t cambio de mayor a menor    {lista} ")



def sort(numbers, ascn):

    sortedNumbers = []
    
    for index,number in enumerate(numbers):
        if ascn==True:
            if index==0:
                sortedNumbers.append(number)
            elif number <sortedNumbers[0]:
                sortedNumbers.insert(0,number)
            elif number >sortedNumbers[-1]:
                sortedNumbers.append(number)
        else:
            if index==0:
                sortedNumbers.append(number)
            elif number >sortedNumbers[0]:
                sortedNumbers.insert(0,number)
            elif number <sortedNumbers[-1]:
                sortedNumbers.append(number)
    return sortedNumbers


print(sort((4, 6, 1,9,0, 8, 2), True)) # 1, 2, 4, 6, 8
print(sort((4, 6, 1,9,0, 8, 2), False)) # 8, 6, 4, 2, 1

