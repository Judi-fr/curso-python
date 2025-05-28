
'''
DESAFIO N~6
 * INVIRTIENDO CADENAS
 * Dificultad: FÁCIL
Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
'''
###############################################################################################
def reverse(text):
    a=list(text)
    a.reverse()
    return "".join(a)
print(reverse("Hola mundo"))
exit()
###############################################################################################
def reverse(text):
    return text[::-1]
print(reverse("Hola mundo"))

exit()
###############################################################################################

def reverse(text):
    reversedText = ""
    for caracter in text[::-1]: 
        reversedText += caracter
    return reversedText
print(reverse("Hola mundo"))


###############################################################################################
def reverse(text):
    reversedText = ""
    for index in text[::-1]: 
        reversedText += text[index]
    return reversedText
print(reverse("Hola mundo"))
###############################################################################################
def reverse(text):
    reversedText = ""
    for index in range(len(text)-1, -1,-1): 
        reversedText += text[index]
    return reversedText
print(reverse("Hola mundo"))

###############################################################################################
def reverse(text):
    reversedText = ""
    textCount=len(text)
    for index in range(0,textCount): 
        reversedText += text[(textCount -1) - index]
    return reversedText
print(reverse("Hola mundo"))
###############################################################################################
# Sin un bucle, mediante una función recursiva
def recursiveReverse(text, index = 0, reversedText= ""):
    textCount = len(text) - 1
    reversedText += text[textCount - index]
    if (index < textCount) :
        reversedText = recursiveReverse(text, index + 1, reversedText)
    return reversedText


print(recursiveReverse("Hola mundo"))
