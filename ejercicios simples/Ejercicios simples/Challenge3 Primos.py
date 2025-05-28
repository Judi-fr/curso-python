
'''
DESAFIO N~3
 * ¿ES UN NÚMERO PRIMO?
 * Dificultad: MEDIA
Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
'''


def isPrime(number):

    if (number < 2):
        return  False
    for i in range(2, number) :
        if (number % i == 0) :
            return False
    return True
for number in range(1,101):
    salida=isPrime(number)
    print (f"numero {number} en primo {salida}")



def is_prime2():

    for number in range(1, 101):

        if number >= 2:

            is_divisible = False

            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break

            if not is_divisible:
                print(number)

is_prime2()


import random
def isPrime3_ext(number):

    if (number < 2):
        return  False
    for i in range(2, number) :
        if (number % i == 0) :
            return False
    return True

# ~ isPrime3_lambda = lambda number: False if (number < 2) else (True if (number % i == 0) else  False for i in range(2, number) )
que_hace_lambda = lambda number: False if (number < 2) else all(number % i != 0 for i in range(2, number))
for _ in range(1,101):
    number= random.randint(99,9999)
    print (f"ext     numero {number} en primo {isPrime3_ext(number)}")
    print (f"lambda  numero {number} en primo {isPrime3_lambda(number)}")
