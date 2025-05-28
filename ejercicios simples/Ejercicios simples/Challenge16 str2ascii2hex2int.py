'''
Complete the function that accepts a valid string and returns an integer.

Wait, that would be too easy!
Every character of the string should be converted to the hex value of its ascii code, 
then the result should be the sum of the numbers in the hex strings (ignore letters).

Complete una función que ingrese un string y retorne un entero.

Alto, no es tan facil!!!
Cambia cada caracter a numeros ascii
Cada numero ascii a hexadecimal.
Elimina todas las letras y suma todos los numeros de los hexadecimales
retorna la suma todos los numeros  



Examples
"Yo" ==> "59 6f" ==> 5 + 9 + 6 = 20
"Hello, World!"  ==> 91
"Forty4Three"    ==> 113
'''

y=[]
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


