
'''
DESAFIO N~'25
 * PIEDRA, PAPEL, TIJERA
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "Piedra", "Papel" o "Tijera".
 * - Ejemplo. Entrada: [("Piedra","Tijera")=}'), ("Tijera","Piedra")=}'), ("Papel","Tijera")=}')]. Resultado: "Player 2".
 * - Cada juego es una lista/tupla de n pares de jugadas-primer jugador // segundo jugador
'''





def juego(*partidas):#ingresa como coleccion tipo Tupla
    '''
    si viene un vector = 1 sola jugada transformo en una matriz de un solo vector de 2 elementos 
                                                [(jugador_1 , jugador_2)]
                                                
    si vienen varios vectores es una matriz de  [(jugador_1 , jugador_2),
                                                 (jugador_1 , jugador_2),
                                                 (jugador_1 , jugador_2)]
    '''
    
    puntos_J1=0
    puntos_J2=0
    
    if len(partidas)==2 and isinstance(partidas[0],str):# una partida sola
        partidas= [[partidas[0],partidas[1]]]#transformo vector a matrix 1x1 (1 es un par)


    for partida_numero,cada_partida in enumerate(partidas):      
        # ~ print (f"{cada_partida}")
        jugador_1,jugador_2= cada_partida
        print (f"Tirada numero {partida_numero+1}    jugador 1={jugador_1}  vs   jugador 2={jugador_2}")
        if  jugador_1.upper() not in ["PIEDRA" , "TIJERA" ,"PAPEL"] or \
            jugador_2.upper() not in ["PIEDRA" , "TIJERA" ,"PAPEL"] :
            print (f"Tirada numero {partida_numero+1} no válida")
            puntos_J1+=0
            puntos_J2+=0
            continue
        else:
            
            if jugador_1.upper()== jugador_2.upper():
                puntos_J1+=0
                puntos_J2+=0
                print (f"Tirada numero {partida_numero+1}  empatada")
            elif    (jugador_1.upper()=="PIEDRA"  and jugador_2.upper()=="TIJERA") or \
                    (jugador_1.upper()=="TIJERA"  and jugador_2.upper()=="PAPEL") or \
                    (jugador_1.upper()=="PAPEL"   and jugador_2.upper()=="PIEDRA")  :
                puntos_J1+=1
                puntos_J2+=0
                print (f"Tirada numero {partida_numero+1} ganada por jugador 1")
            else:
                puntos_J1+=0
                puntos_J2+=1
                print (f"Tirada numero {partida_numero+1} ganada por jugador 2") 
        
    if puntos_J1 == puntos_J2:
        return f"partida empatada con {partida_numero+1} tiradas "
    elif puntos_J1 > puntos_J2:
        return f"partida ganada por el jugador 1 con {partida_numero+1} tiradas "
    else:
        return f"partida ganada por el jugador 2 con {partida_numero+1} tiradas "












retorno = juego("Piedra","Tijera")#vector
print (f"{retorno}")
print ("^"*100)
retorno = juego(("Piedra","Tijera"), ("Tijera","Piedra"), ("Papel","Tijera"))#matriz
print (f"{retorno}")
print ("^"*100)
retorno = juego(("Piedra","Tijera"), ("Tijera","Piedra"))#matriz
print (f"{retorno}")
print ("^"*100)
retorno = juego(("Piedra","Tijera"), ("Tijera","Piedra"), ("Papel","piedra"))#matriz
print (f"{retorno}")
print ("^"*100)
retorno = juego(("Piedra","Tijera"), ("Tijera","Piedra"), ("Papel","Spock"))#matriz
print (f"{retorno}")
print ("^"*100)


exit()
def ppt(*jugada):
        print ("*"*100)
        matriz=[]
        jugador_1=0
        jugador_2=0
        if not isinstance(jugada[0],tuple):
            matriz.append(jugada)
        else:
            matriz=list(jugada)
        for game in  matriz: 
            playerOneMove,playerTwoMove = game
            for Jugada_1,Jugada_2 in (("Piedra","Tijera"),("Papel","Piedra"),("Tijera","Papel")): 
                if (playerOneMove == Jugada_1 and playerTwoMove == Jugada_2):
                    jugador_1+=1
                    break
                elif (playerTwoMove == Jugada_1 and playerOneMove == Jugada_2):
                    jugador_2+=1
                    break
        if (jugador_1 > jugador_2):
            salida= "ganador Jugador 1"
        elif (jugador_1 < jugador_2):
            salida= "ganador Jugador 2"
        else:
            salida= "tablas / sin ganador tablas"
        return salida
print(f'{ppt("Piedra", "Piedra")=}')
print(f'{ppt("Piedra", "Papel")=}')
print(f'{ppt("Piedra", "Tijera")=}')
print(f'{ppt("Papel","Tijera")=}')
print(f'{ppt(("Piedra", "Piedra"),("Tijera", "Tijera"),("Papel", "Papel"))=}')
print(f'{ppt(("Piedra", "Tijera"),("Tijera", "Papel"),("Tijera", "Piedra"))=}')
print(f'{ppt(("Piedra", "Papel"), ("Tijera", "Piedra"),("Papel", "Tijera"))=}')
