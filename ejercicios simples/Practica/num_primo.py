#como saber si un numero es primo

numero = int(input("Ingrese el numero: "))

es_primo = True

for x in range(2,numero):
    if numero % x == 0:
        es_primo = False

print(f"primo == {es_primo}")

    