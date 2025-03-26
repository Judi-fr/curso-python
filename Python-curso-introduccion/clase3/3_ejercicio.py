"""
Crear un contador que vaya disminuyendo su valor
de uno en uno desde 10 a 0
mientras se imprime por pantalla
"""

from time import sleep

contador = 10

while contador >= 0:
    sleep(0.3)
    print(contador)
    # contador = contador - 1
    contador -= 1
