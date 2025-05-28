""" 
Complete el siguiente código. Explique su funcionamiento
Genere un programa que evalúe si el jugador recorre la pista de vallas sin errores.
por cada '_' que ve en pantalla de la pista random debe ingresar una 'C' de correr  y por cada '|' de valla una 'S' de saltar
si hay caracteres que no son 'C'  que '_'  o 'S' que '|'  se reintenta el ingreso
se unifican ambos strings a '_' y '|' 
Luego si hay mas  '_' o '|' en una que en otra pista pierde el jugador humano
se compara cada carácter de las dos pista, si son diferentes  pierde el jugador humano
si no hay errores resultado = "éxito" del jugador humano

Ejemplo 1:
pista = _ _ _ | _ _ _ | | _ _ _
C C C S C C C S S C C C
solucion= CCCSCCCSSCCC
El jugador recorrió la pista con éxito
---------------------------------------------------
Ejemplo 2:
pista = _ _ _ | _ _ _ | | _ _ _
C C S S C C C S C C C C
^__errores__^
solucion= CCSSCCCSCCCC
El jugador recorrió la pista con errores
"""
import random
pistas_posibles = {
"uno": "_|_|_",
"dos": "__|||||",
"tres": "__|___|___|___|___|___|___|___",
"cuatro": "__||___|___||___|___||___|___||___",
"cinco": "__|_|__|___|__|_|______",
"seis": "__||_|___||_|___||_|___||___"
}
gana_compu = 0
gana_jugador = 0
total_juegos=0
while True:
    
    # Selecciona al azar una de las claves del diccionario
    pista_random_index = random.choice(list(pistas_posibles.keys()))
    pista_random = pistas_posibles[pista_random_index]
    print(f"Pista seleccionada al azar: {pista_random}")
    pista_jugador = "x"
    # Solicita entrada del usuario y verifica si contiene solo 'C' y 'S'
    while not all(caracter in ["C", "S"] for caracter in pista_jugador):
        pista_jugador = input("\tIngrese S) saltar por cada '|' y C) correr por cada '_'\n>").upper()
    print(f"{all(caracter in ['C', 'S'] for caracter in set(pista_jugador))=}")
    # Cambia las 'C' por '_' y las 'S' por '|'
    total_juegos+=1
    pista_jugador_cambio = pista_jugador.replace("C", "_").replace("S", "|")
    print(f"Tu jugada modificada: {pista_jugador_cambio} {len(pista_jugador_cambio)}")
    print(f"Pista recorrida: {pista_random} {len(pista_random)}")
    # si hay mas '_' o '|' en una que en otra pista--->  reintente
    #...........................
        print (f"error la pista y la jugada miden diferente, reintente")
        continue
    # si hay errores, la posición  '_' o '|' es distinta en ambas pistas en el mismo lugar ---> resultado = "errores"
    #...........................
        regreso="errores"
        gana_compu+=1
    # No hay errores, la posición  '_' o '|' es igual en ambas pistas en el mismo lugar ---> resultado = "errores"
    #...........................    
        regreso="exito"
        gana_jugador+=1
    print("*"*50)
    #imprime cuantas ganadas y cuantas perdidas y los porcentajes
    print (f"El jugador recorrió la pista con {regreso}")
    opcion=input(" enter para continuar o T para terminar:").upper()
    if opcion =="T":
        break
    #imprima las estadísticas del juego (jugadas totales, ganadas, perdidas y porcentajes)
total_juegos = gana_compu + gana_jugador
print(f"""
Estadísticas
Total de juegos válidos: {total_juegos}
Juegos ganados: {........................... }
Juegos perdidos: {........................... }
#Porcentaje de victorias: {round........................... }%
#Porcentaje de derrotas:  {round........................... }%
""")
print("*" * 50)
"""
Explicación del Funcionamiento del Código
    1. Importar el módulo random: Para seleccionar aleatoriamente una pista de las posibles.
    2. Definir el diccionario de pistas posibles: Cada clave representa una pista con obstáculos ('|') y espacios para correr ('_').
    3. Inicializar contadores de victorias y derrotas.
    4. Bucle principal del juego:
        ◦ Selecciona aleatoriamente una pista del diccionario.
        ◦ Solicita al jugador que ingrese su jugada (S para saltar y C para correr) hasta que la entrada sea válida.
        ◦ Convierte las jugadas ('C' a '_', 'S' a '|') para compararlas con la pista seleccionada.
    5. Validación de la jugada del jugador:
        ◦ Verifica si la longitud de la jugada es diferente a la de la pista.
        ◦ Usa any para verificar si hay alguna diferencia entre la jugada del jugador y la pista seleccionada.
    6. Actualización del resultado:
        ◦ Incrementa el contador de victorias o derrotas basado en la validez de la jugada.
    7. Imprimir estadísticas al finalizar el juego:
        ◦ Calcula el porcentaje de victorias y derrotas.
        ◦ Muestra el total de juegos ganados y perdidos.
#-----------------------------------------------------------------
# si hay mas '_' o '|' en una que en otra pista--->  reintente
if len(pista_jugador_cambio) != len(pista_random):
#-----------------------------------------------------------------
# si hay errores si la posición  '_' o '|' es distinta en ambas pistas ---> resultado = "errores"
if any(pista_jugador_cambio[i] != pista_random[i] for i in range(len(pista_random))) :
#-----------------------------------------------------------------
# No hay errores, la posición  '_' o '|' es igual en ambas pistas en el mismo lugar ---> resultado = "errores"
else:
#-----------------------------------------------------------------
# Imprime las estadísticas del juego (jugadas ganadas, ganadas, perdidas y porcentajes)
"""

