"""
Crear una cadena con un mensaje que hable de la programación con Python
y recorrer la variable con for, impriendo caracter por caracter.
"""

from time import sleep

frase = (
    "La creciente popularidad del aprendizaje "
    "automático probablemente hará que Python sea el lenguaje líder en el futuro."
)

contador = 1
caracteres_nuevos = ""

for caracter in frase:
    caracteres_nuevos += caracter
    if contador == 5:
        sleep(0.6)
        print(caracteres_nuevos, end="\r")
        contador = 0
        caracteres_nuevos = ""
    contador += 1
