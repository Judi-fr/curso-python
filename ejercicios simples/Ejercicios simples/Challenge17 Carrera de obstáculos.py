
'''
DESAFIO N~'17
 * LA CARRERA DE OBSTÁCULOS
 * Dificultad: MEDIA
 *
 * Enunciado: Crea una función que evalúe si un/a atleta ha superado correctamente una
 * carrera de obstáculos.
 * - La función recibirá dos parámetros:
 *      - Un array que sólo puede contener String con las palabras "CORRER" o "SALTAR"
 *      - Un String que represente la pista y sólo puede contener "_" suelo) o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 *      - Si el/a atleta hace "CORRER" en "_" (suelo) y "SALTAR" en "|" (valla) será correcto y no
 *        variará el símbolo de esa parte de la pista.
 *      - Si hace "SALTAR" en "_" (suelo), se variará la pista por "x".
 *      - Si hace "CORRER" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera.
 * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
'''
## Solucion
def arbitro_de_pista(movimientos, pista):
    pista=  list(pista)# 
    dic={"CORRER":"_","SALTAR":"|"}
    flag = False
    if len(pista)!=len(movimientos) :
        return ("error en cantidad de movimientos")
    elif  not all([True if cada in ['CORRER','SALTAR']  else False for cada in movimientos ]) :
        return ("movimientos  invalido")
    elif not all([True if cada in ['_', '|'] else False for cada in pista ]):
        return ("pista invalida")
    else:#len(pista)==len(movimientos)
        for index in range(0,len(pista)):
            if pista[index]==dic[movimientos[index]]:
                continue
            elif pista[index]=="|":
                pista[index]="/"
                flag=True
            elif pista[index]=="_":
                pista[index]="X"
                flag=True
    pista=str().join(pista)
    if flag==True:
        return pista, f"La proxima :(, el atleta recorrio la pista con errores"
    else:
        return pista, f"Felicitacione!!, el atleta recorrio la pista sin errores"




pistas = ["_|_|_","|||||","__|___|___|___|___|___|___|___","__||___|___||___|___||___|___||___","__|_|__|___|__|_|______","__||_|___||_|___||_|___||___"]


 

import random

pista = random.choice(pistas)
print (pista)
exit()
athleta = ['CORRER','SALTAR','CORRER','SALTAR','CORRER']
pista = "_|_|_"
print(arbitro_de_pista(athleta,pista))
print("*"*50)
athleta = ['CORRER','SALTAR','SALTAR','SALTAR','CORRER']
pista = "_|_|_"
print(arbitro_de_pista(athleta,pista))
print("*"*50)
athleta = ['CORRER','CORRER','CORRER','SALTAR','CORRER']
pista = "_|_|_"
print(arbitro_de_pista(athleta,pista))
print("*"*50)
athleta = ['CORRER','CORRER','SALTAR','SALTAR','CORRER']
pista = "_|_|_|_"
print(arbitro_de_pista(athleta,pista))
print("*"*50)
athleta = ['CORRER','SALTAR','CORRER','SALTAR']
pista = "_|_|_"
print(arbitro_de_pista(athleta,pista))
print("*"*50)
athleta = ['CORRER','SALTAR','CORRER','SALTAR','CORRER','SALTAR','CORRER']
pista = "_|_|_"
print(arbitro_de_pista(athleta,pista))
print("*"*50)
athleta = ['SALTAR','SALTAR','SALTAR','SALTAR','SALTAR']
pista = "|||||"
print(arbitro_de_pista(athleta,pista))
print("*"*50)
athleta = ['SALTAR','SALTAR','SALTAR','SALTAR','SALTAR']
pista = "||?||"
print(arbitro_de_pista(athleta,pista))
print("*"*50)
athleta = ['SALTAR','NADAR','SALTAR','SALTAR','SALTAR']
pista = "|||||"
print(arbitro_de_pista(athleta,pista))
print("*"*50)








