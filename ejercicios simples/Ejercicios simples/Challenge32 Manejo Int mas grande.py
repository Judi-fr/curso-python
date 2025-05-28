
'''
DESAFIO N~'32
 * EL SEGUNDO
 * Dificultad: FÁCIL
 *
Enunciado: Dado un listado de números, encuentra el SEGUNDO más grande.
'''

def funcion_buscar_segundo(*numeros): 
    numeros=list(numeros) 
    if len(numeros)>=2:
        found = False
        while found == False:
            found = True
            for index in range(0,len(numeros)-1) :
                if numeros[index]>numeros[index+1] :
                    found = False
                    numeros[index],numeros[index+1]=numeros[index+1],numeros[index]
                elif numeros[index]==numeros[index+1] :
                    numeros.pop(index)
                    break
    return "Error, no hay 2 elementos" if len(numeros)<2 else f'el segundo elemento mayor es {numeros[-2]}'
    

print(funcion_buscar_segundo(9, 8, 7, 6, 5, 4, 3, 2, 1, 0))
print(funcion_buscar_segundo(4, 6, 1, 8, 2))
print(funcion_buscar_segundo(4, 6, 8, 8, 6))
print(funcion_buscar_segundo(4, 4))
print(funcion_buscar_segundo(2, 4))
print(funcion_buscar_segundo())
print("*"*100)
def funcion_buscar_segundo_2(*numeros): 
    numeros=sorted(list(set(numeros))) 
    return "Error, no hay 2 elementos" if len(numeros)<2 else f'el segundo elemento mayor es {numeros[-2]}'


print(funcion_buscar_segundo_2(9, 8, 7, 6, 5, 4, 3, 2, 1, 0))
print(funcion_buscar_segundo_2(4, 6, 1, 8, 2))
print(funcion_buscar_segundo_2(4, 6, 8, 8, 6))
print(funcion_buscar_segundo_2(4, 4))
print(funcion_buscar_segundo_2(2, 4))
print(funcion_buscar_segundo_2())
print("*"*100)
