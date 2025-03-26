contador = 0

while contador <= 10:
    if contador == 3:
        contador += 1
        continue
    if contador == 7:
        break

    print(contador)
    contador += 1
