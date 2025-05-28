'''
DESAFIO N~'38
 * BINARIO A DECIMAL
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa se encargue de transformar un número binario a decimal sin utilizar
 * funciones propias del lenguaje que lo hagan directamente.
'''



def binary_2_int(binary):

    length = len(binary)-1
    decimal = 0
    for index ,digitChar in enumerate(binary[::-1]):
        if (digitChar == '0' or digitChar == '1') :
            decimal += int(digitChar) * 2.0**index
        else :
            return None
    return decimal

print(f'{binary_2_int("00110")=}')
print(f'{binary_2_int("01100")=}')
print(f'{binary_2_int("000000000")=}')
print(f'{binary_2_int("00210")=}')
print(f'{binary_2_int("001101001110")=}')
print(f'{binary_2_int("00b10")=}')
print(f'{binary_2_int("")=}')
print(f'{binary_2_int("-00110")=}')
print(f'{binary_2_int(" ")=}')
print(f'{binary_2_int(" 10011")=}')
print(f'{binary_2_int("1O1OO11")=}')
print(f'{binary_2_int("1010011")=}')
