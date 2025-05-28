'''
Como los valores hexagonales pueden incluir letras de A a F, se pueden deletrear ciertas palabras en inglés, como CAFE, BEEF, o FACADE. 
Este vocabulario se puede extender usando números para representar otras letras, como 5EAF00D, o DEC0DE5.

Dada una cadena, su tarea es devolver la suma decimal de todas las palabras en la cadena que pueden interpretarse como tales valores hexagonales.

Ejemplo
Trabajando con la cuerda "BAG OF BEES":

"BAG"  =  0, as it is not a valid hex value  
"OF"   =  0F   =  15
"BEES" =  BEE5 =  48869
Entonces, el resultado es la suma de estos: 48884 ( 0 + 15 + 48869 )

Notas
Las entradas son todas mayúsculas y no contienen puntuación
0puede ser sustituido por O
5puede ser sustituido por S


'''


# ~ text="Hello, World!"
# ~ text="Forty4Three"

text="Yo"
def str2int_1(text):
    y=list()
    for c in text:
        x=list()
        for z in str(hex(ord(c))):
            if z.isdecimal():
                x.append(int(z))
        y.append(sum(x))
    return (sum(y))
print (f" {text}  ---> {str2int_1(text)}")



def str2int_2(text):
    x=[ sum([int(z) for z in hex(ord(c)) if z.isdecimal()]) for c in text ]
    return sum(x)
print (f" {text}  ---> {str2int_2(text)}")


