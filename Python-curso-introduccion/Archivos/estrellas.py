while True:
    k=0

    filas = int(input("Cantidad de filas? "))

    for i in range(1, 1+filas):
        for espacios in range(1, (filas-i)+1):
            print(" ",end="")
        while k != (2 * i - 1):
            print("*", end="")
            k+=1
        k=0
        print()