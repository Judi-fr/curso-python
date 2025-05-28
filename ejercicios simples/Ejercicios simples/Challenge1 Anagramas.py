
'''
DESAFIO N~01
 * ¿ES UN ANAGRAMA?
 * Dificultad: MEDIA

Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
NO hace falta comprobar que ambas palabras existan.
Dos palabras exactamente iguales no son anagrama.
    1) Imprime cada dato en una misma linea
    2) crea una lista con tres sub listas string_1 , string_2 y salida, e imprimela al final
nota:
    verifica las mayusculas/minusculas
    verifica las acentos
'''
##Solucion

def comparar_anagrama(string_1, string_2):
    """ 
    string_1= string_1.lower()
    string_2= string_2.lower()
    print (f"antes {string_1=}")
    print (f"antes {string_2=}")
    dic={"á":"a",
        "é":"e",
        "í":"i",
        "ó":"o",
        "ú":"u",
        "ü":"u"}
    """ 

        
    """
    for caracter_1 in string_1:
        if caracter_1=="á":
            string_1=string_1.replace("á","a")
        elif caracter_1=="é":
            string_1=string_1.replace("é","e")
        elif caracter_1=="í":
            string_1=string_1.replace("í","i")
        elif caracter_1=="ó":
            string_1=string_1.replace("ó","o")
        elif caracter_1=="ú":
            string_1=string_1.replace("ú","u")
        elif caracter_1=="ü":
            string_1=string_1.replace("ü","u")
        print(caracter_1)
    for caracter_1 in string_2:
        if caracter_1=="á":
            string_2=string_2.replace("á","a")
        elif caracter_1=="é":
            string_2=string_2.replace("é","e")
        elif caracter_1=="í":
            string_2=string_2.replace("í","i")
        elif caracter_1=="ó":
            string_2=string_2.replace("ó","o")
        elif caracter_1=="ú":
            string_2=string_2.replace("ú","u")
        elif caracter_1=="ü":
            string_2=string_2.replace("ü","u")
        print(caracter_1)
    """
    #··-----------------------------------------------------------
    """
    for vocal in dic.keys():
        if vocal in string_1:
            string_1=string_1.replace(vocal,dic[vocal])
        if vocal in string_2:
            string_2=string_2.replace(vocal,dic[vocal])
    """
    #··-----------------------------------------------------------
    string_1=string_1.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ü","u")
    string_2=string_2.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ü","u")
 
    print (f"despues {string_1=}")
    print (f"despues {string_2=}")
    #                       genero una lista de cada string
    lista_1=list(string_1)
    lista_2=list(string_2)
    print (f"lista {lista_1=}")
    print (f"lista {lista_2=}")
    #                       ordeno las listas
    lista_1.sort()
    lista_2.sort()
    print (f"sort {lista_1=}")
    print (f"sort {lista_2=}")
    #                       comparo si ambas listas ordenadas son identicas
    if lista_1 == lista_2:
        return True
    else:
        return False

    #··-----------------------------------------------------------

    # ~ print (sorted(string_1))
    # ~ print (sorted(string_2))
    if sorted(string_1) == sorted(string_2):
        return True
    else:
        return False
    #··-----------------------------------------------------------
def comparar_anagrama_python(string_1, string_2):
    """
    string_1=string_1.lower().\
            replace("á","a").\
            replace("é","e").\
            replace("í","i").\
            replace("ó","o").\
            replace("ú","u").\
            replace("ü","u")
    string_2=string_2.lower().\
            replace("á","a").\
            replace("é","e").\
            replace("í","i").\
            replace("ó","o").\
            replace("ú","u").\
            replace("ü","u")
    return sorted(string_1) == sorted(string_2)
    """
    return sorted(string_1.lower().\
                            replace("á","a").\
                            replace("é","e").\
                            replace("í","i").\
                            replace("ó","o").\
                            replace("ú","u").\
                            replace("ü","u")) == sorted(string_2.lower().\
                                                                replace("á","a").\
                                                                replace("é","e").\
                                                                replace("í","i").\
                                                                replace("ó","o").\
                                                                replace("ú","u").\
                                                                replace("ü","u"))

    
        
palabra_1=""
palabra_2=""
while len (palabra_1)!=len(palabra_2):
    palabra_1= input ("Ingrese la primer palabra:")
    palabra_2= input ("Ingrese la segunda palabra:")


# ~ print (f'Son anagramas :{comparar_anagrama("VáLéntin", "valenTÍn") }')

respuesta =comparar_anagrama_python("VáLéntin", "valenTÍn")
if respuesta is True:
    print (f" {palabra_1} es anagrama de {palabra_2}")
else:
    print (f" {palabra_1}  y {palabra_2} no son anagramas")
# ~ comparar_anagrama(palabra_1, palabra_2)


ejemplos=[('Alegan','Ángela'), ('Nepal','Panel'), ('Nacionalista','Altisonancia'), ('Valora','Álvaro'), ('Raza','Zara'), ('Frase','Fresa'), ('Colinas','Nicolás'), ('Pagar','Praga'), ('Integrarla','Inglaterra'), ('Quieren','Enrique'), ('Cornisa','Narciso'), ('Acuerdo','Ecuador'), ('Japonés','Esponja'), ('Amparo','Páramo'), ('Deudora','Eduardo'), ('Ramón','Norma'), ('Camino','Mónica'), ('Fotolitografía','Litofotografía'), ('Animal','Lámina'), ('Matar','Marta'), ('Saco','Cosa'), ('Mora','Roma'), ('Brasil','Silbar'), ('Sentido','Destino'), ('Saunas','Susana'), ('Croacia','Arcaico'), ('Tinieblas','Sibilante'), ('Aretes','Teresa'), ('Andalucía','Alucinada'), ('Cronista','Cortinas'), ('Ventilan','Valentín'), ('Aparcamiento','Metacarpiano'), ('Calienta','Alicante'), ('Trama','Marta'), ('Ballena','Llenaba'), ('Reposaré','Reposera'), ('Cardiografía','Radiográfica'), ('Conejo','Encojo'), ('Demostración','Domesticaron'), ('Desamparador','Desparramado'), ('Polonia','Opalino'), ('Sopera','Sopear'), ('Conservadora','Conversadora'), ('Ardientemente','Retenidamente'), ('Áspero','Espora'), ('Irónicamente','Renacimiento'), ('Riesgo','Sergio'), ('Aires','Aries'), ('Escandalizar','Zascandilear'), ('Agonista','Santiago'), ('Presa','Pesar'), ('Enfriamiento','Refinamiento'), ('Calor','Colar'), ('Esta','Ates'), ('Romina','Marino'), ('Prisa','París'), ('Astringencia','Transigencia'), ('Materialismo','Memorialista'), ('Poder','Pedro'), ('Resto','Retos'), ('Enérgicamente','genéricamente'), ('Necrófila','Florencia'), ('Reías','Ríase'), ('Presuposición','Superposición'), ('Armonía','Mariano'), ('Terso','Teros'), ('Enamoramientos','Armoniosamente'), ('Salario','Rosalía'), ('Caracas','Cáscara'), ('Rectificable','Certificable'), ('Ovoide','Oviedo'), ('España','Apañes'), ('Reconquistados','Conquistadores'), ('Camelia','Micaela'), ('Alondra','Ladrona'), ('Escabullimiento','Bulliciosamente'), ('Enlodar','Leandro'), ('Conservación','Conversación'), ('Electromagnético','Magnetoeléctrico'), ('Delira','Lidera'), ('Derrocamiento','Recordamiento'), ('Imponderable','imperdonable'), ('Agranda','Granada'), ('Manila','Animal'), ('Armonización','Romanización'), ('Licúa','Lucía'), ('Ruanda','Anudar'), ('Pronosticación','Contraposición'), ('Amor','Roma'), ('Protesta','Portaste'), ('imperdonablemente','imponderablemente'), ('cristianodemócrata','democratacristiano'), ('fotolitográficamente','litofotográficamente')]
#··-----------------------------------------------------------
"""
for lista in ejemplos:
    palabra_1 =lista[0]
    palabra_2 =lista[1]
    respuesta =comparar_anagrama_python(palabra_1, palabra_2)
    if respuesta is True:
        print (f" {palabra_1} es anagrama de {palabra_2}")
    else:
        print (f" {palabra_1}  y {palabra_2} no son anagramas")
"""
#··-----------------------------------------------------------
"""
for palabra_1 , palabra_2 in ejemplos:
    if comparar_anagrama_python(palabra_1, palabra_2):
        print (f" {palabra_1} es anagrama de {palabra_2}")
    else:
        print (f" {palabra_1}  y {palabra_2} no son anagramas")

"""
#··-----------------------------------------------------------
for palabra_1 , palabra_2 in ejemplos:
    if sorted(palabra_1.lower().\
                            replace("á","a").\
                            replace("é","e").\
                            replace("í","i").\
                            replace("ó","o").\
                            replace("ú","u").\
                            replace("ü","u")) == sorted(palabra_2.lower().\
                                                                replace("á","a").\
                                                                replace("é","e").\
                                                                replace("í","i").\
                                                                replace("ó","o").\
                                                                replace("ú","u").\
                                                                replace("ü","u")):

        print (f" {palabra_1} es anagrama de {palabra_2}")
    else:
        print (f" {palabra_1}  y {palabra_2} no son anagramas")






'''
Alegan – Ángela                         Nepal – Panel                           Nacionalista – Altisonancia
Valora – Álvaro                         Raza – Zara                             Frase – Fresa
Colinas – Nicolás                       Pagar – Praga                           Integrarla – Inglaterra
Quieren – Enrique                       Cornisa – Narciso                       Acuerdo – Ecuador
Japonés – Esponja                       Amparo – Páramo                         Deudora – Eduardo
Ramón – Norma                           Camino – Mónica                         Fotolitografía – Litofotografía
Animal – Lámina                         Matar – Marta                           Saco – Cosa
Mora – Roma                             Brasil – Silbar                         Sentido – Destino
Saunas – Susana                         Croacia – Arcaico                       Tinieblas – Sibilante
Aretes – Teresa                         Andalucía – Alucinada                   Cronista – Cortinas
Ventilan – Valentín                     Aparcamiento – Metacarpiano             Calienta – Alicante
Trama – Marta                           Ballena – Llenaba                       Reposaré – Reposera
Cardiografía – Radiográfica             Conejo – Encojo                         Demostración –  Domesticaron
Desamparador – Desparramado             Polonia – Opalino                       Sopera – Sopear
Conservadora – Conversadora             Ardientemente – Retenidamente           Áspero – Espora
Irónicamente – Renacimiento             Riesgo – Sergio                         Aires – Aries
Escandalizar – Zascandilear             Agonista – Santiago                     Presa – Pesar
Enfriamiento – Refinamiento             Calor – Colar                           Esta – Ates
Romina – Marino                         Prisa – París                           Astringencia – Transigencia
Materialismo – Memorialista             Poder – Pedro                           Resto – Retos
Enérgicamente – genéricamente           Necrófila – Florencia                   Reías – Ríase
Presuposición – Superposición           Armonía – Mariano                       Terso – Teros
Enamoramientos – Armoniosamente         Salario – Rosalía                       Caracas – Cáscara
Rectificable – Certificable             Ovoide – Oviedo                         España – Apañes
Reconquistados – Conquistadores         Camelia – Micaela                       Alondra – Ladrona
Escabullimiento – Bulliciosamente       Enlodar – Leandro                       Conservación – Conversación
Electromagnético – Magnetoeléctrico     Delira – Lidera                         Derrocamiento – Recordamiento
Imponderable – imperdonable             Agranda – Granada                       Manila – Animal
Armonización – Romanización             Licúa – Lucía                           Ruanda – Anudar
Pronosticación – Contraposición         Amor – Roma                             Protesta – Portaste

'''
"""
def funcion(palabra_1,palabra_2):
    dic={"á":"a","é":"e","í":"i","ó":"o","ú":"u","ü":"u"}
    for clave,valor in dic.items():    
        palabra_1=palabra_1.replace(clave,valor) 
        palabra_2=palabra_2.replace(clave,valor) 
    if palabra_1!=palabra_2 and len(palabra_1)==len(palabra_2) and sorted ([char for char in palabra_1 ]) == sorted([char for char in palabra_2 ]) :
        salida =True
    else:
        salida =False
    print(sorted([char for char in palabra_1 ]),sorted([char for char in palabra_2 ]))
    print(sorted([char for char in palabra_1 ])==sorted([char for char in palabra_2 ]))

    print (f"{palabra_1},{palabra_2}, {salida}")
    matriz = [[palabra_1],[palabra_2],[salida]]
    return matriz
palabra_1 = input("Ingrese el primer string:").lower()

palabra_2 = input("Ingrese el segundo string:").lower()

matriz = funcion(palabra_1,palabra_2)
print (f"{matriz=}")

exit()


    
matriz =[]
def isAnagram(wordOne, wordTwo):
    wordOne=wordOne.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    wordTwo=wordTwo.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    if (wordOne.lower() == wordTwo.lower()):
        salida = False
    elif (sorted(wordOne.lower()) == sorted(wordTwo.lower())):
        salida = True
    else:
        salida = False

    matriz.append([salida,wordOne, wordTwo])
    return salida
print(isAnagram("amor", "roma"))
print(isAnagram("pepe", "sopa"))
print(isAnagram("España","apañes"))
print(isAnagram("Enrique","quieren"))
print(isAnagram("Ballena","llenaba"))
print(isAnagram("Reposaré","Reposera"))
print (matriz)
for par_de_datos in enemplos:
    print(isAnagram(par_de_datos))

"""
