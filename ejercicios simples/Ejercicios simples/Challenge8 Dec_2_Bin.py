
'''
DESAFIO N~8
 * DECIMAL A BINARIO
 * Dificultad: FÁCIL
Enunciado: Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
'''



def int_2_binary(decimal): 

    valor_dec = decimal
    str_binario = ""
    while (valor_dec != 0) :
        resto = valor_dec % 2
        valor_dec = valor_dec //2
        str_binario = f"{resto}"+str_binario

    return str_binario

print(f"{int_2_binary(387)=}")
print(f"{int_2_binary(0)=}")
print(f"{int_2_binary(1)=}")
print(f"{int_2_binary(2)=}")
print(f"{int_2_binary(3)=}")
print(f"{int_2_binary(4)=}")
print(f"{int_2_binary(5)=}")
print(f"{int_2_binary(6)=}")
print(f"{int_2_binary(7)=}")
print(f"{int_2_binary(8)=}")
print(f"{int_2_binary(9)=}")
print(f"{int_2_binary(10)=}")
print(f"{int_2_binary(32)=}")
print(f"{int_2_binary(256)=}")
print(f"{int_2_binary(1024)=}")
