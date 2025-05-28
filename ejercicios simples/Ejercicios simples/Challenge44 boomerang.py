
'''
DESAFIO N~44
 * BUMERANES
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que retorne el número total de bumeranes de un array de números
 * enteros e imprima cada uno de ellos.
 * - Un bumerán (búmeran, boomerang) es una secuencia formada por 3 números seguidos, en el que el
 *   primero y el último son iguales, y el segundo es diferente. Por ejemplo [2, 1, 2].
 * - En el array [2, 1, 2, 3, 3, 4, 2, 4] hay 2 bumeranes ([2, 1, 2] y [4, 2, 4]).
'''
def numberOfBoomerangs(*numbers):
    if (len(numbers) < 3) :
        return 0
    Boomerangs = 0
    for index,dato in enumerate (range(0,len(numbers)-2)):
        prev , current , next_ = numbers[index:index+3]
        if (prev == next_ and prev != current) :
            print(f"es bumeran [{prev}<{current}>{next_}]")
            Boomerangs+=1
    return Boomerangs
print(numberOfBoomerangs(2, 1, 2, 3, 3, 4, 2, 4))
print(numberOfBoomerangs(2, 1, 2, 1, 2))
print(numberOfBoomerangs(1, 2, 3, 4, 5))
print(numberOfBoomerangs(2, 2, 2, 2, 2))
print(numberOfBoomerangs(2, -2, 2, -2, 2))
print(numberOfBoomerangs(2, -2))
print(numberOfBoomerangs(2))
print(numberOfBoomerangs())
