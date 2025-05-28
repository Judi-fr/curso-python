
'''
DESAFIO N~'33
 * CICLO SEXAGENARIO CHINO
 * Dificultad: MEDIA
 *
Enunciado: Crea un función, que dado un año, indique el elementoo y animal correspondiente
en el ciclo sexagenario del zodíaco chino.
 - Información: https://www.travelchinaguide.com/intro/astrology/60año-cycle.htm
 - El ciclo sexagenario se corresponde con la combinación de 
 elementoos:      madera, fuego, tierra, metal, agua y 
 animales:       rata, buey, tigre, conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo (en este orden).
 - Cada elementoo se repite dos años seguidos.
 - El último ciclo sexagenario comenzó en 1984 (Madera Rata).\\
 
 
 
 pasar a GUI
 
 
 
 
'''



def funcion_Zodiaco_chino(año) :
    elementos = ("madera", "fuego", "tierra", "metal", "agua")
    animales = ("rata", "buey", "tigre", "conejo", "dragón", "serpiente", "caballo", "oveja", "mono", "gallo", "perro", "cerdo")

    if (año < 604) :
        return "El ciclo sexagenario comenzó en el año 604."
    año_sexagenario = (año - 4) % 60
    elemento = elementos[int((año_sexagenario % 10) / 2)]
    animal = animales[año_sexagenario % 12]
    return f"{año}: {elemento} {animal}"

print(funcion_Zodiaco_chino(1924))
print(funcion_Zodiaco_chino(1946))
print(funcion_Zodiaco_chino(1984))
print(funcion_Zodiaco_chino(604))
print(funcion_Zodiaco_chino(603))
print(funcion_Zodiaco_chino(1987))
print(funcion_Zodiaco_chino(2020))
print(funcion_Zodiaco_chino(2022))
