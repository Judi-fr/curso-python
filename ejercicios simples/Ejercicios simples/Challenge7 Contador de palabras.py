
'''
DESAFIO N~7
 * CONTANDO PALABRAS
 * Dificultad: MEDIA
Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
'''



















exit()
def contador_de_palabras(texto) :

    lista_palabras = {}
    texto=texto.replace("\n","").replace('"','').replace('.',' ').replace(',',' ')
    lista = texto.lower().split(" ")
    for palabra in lista:
        if palabra not in lista_palabras.keys():# ver dic.get()
            lista_palabras[palabra]=1
        else :
            lista_palabras[palabra]+=1
    for palabra,cantidad in lista_palabras.items():    
        print(f"la {palabra=} se ha repetido {cantidad} {'vez' if(cantidad == 1)  else 'veces'}")

contador_de_palabras("Hola,Mundo este es un ejercicio en Python con strings")
contador_de_palabras('''poema numero XX - Pablo Neruda
PUEDO escribir los versos más tristes esta noche.

Escribir, por ejemplo: "La noche está estrellada,
y tiritan, azules, los astros, a lo lejos".

El viento de la noche gira en el cielo y canta.

Puedo escribir los versos más tristes esta noche.
Yo la quise, y a veces ella también me quiso.

En las noches como ésta la tuve entre mis brazos.
La besé tantas veces bajo el cielo infinito.

Ella me quiso, a veces yo también la quería.
Cómo no haber amado sus grandes ojos fijos.

Puedo escribir los versos más tristes esta noche.
Pensar que no la tengo. Sentir que la he perdido.

Oir la noche inmensa, más inmensa sin ella.
Y el verso cae al alma como al pasto el rocío.

Qué importa que mi amor no pudiera guardarla.
La noche está estrellada y ella no está conmigo.

Eso es todo. A lo lejos alguien canta. A lo lejos.
Mi alma no se contenta con haberla perdido.

Como para acercarla mi mirada la busca.
Mi corazón la busca, y ella no está conmigo.

La misma noche que hace blanquear los mismos árboles.
Nosotros, los de entonces, ya no somos los mismos.

Ya no la quiero, es cierto, pero cuánto la quise.
Mi voz buscaba el viento para tocar su oído.

De otro. Será de otro. Como antes de mis besos.
Su voz, su cuerpo claro. Sus ojos infinitos.

Ya no la quiero, es cierto, pero tal vez la quiero.
Es tan corto el amor, y es tan largo el olvido.

Porque en noches como ésta la tuve entre mis brazos,
mi alma no se contenta con haberla perdido.

Aunque éste sea el último dolor que ella me causa,
y éstos sean los últimos versos que yo le escribo.''')
