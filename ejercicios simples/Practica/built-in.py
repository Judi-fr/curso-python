

numerillos = [1,2,3,4,6]

Manuel = True 
Ezequiel = True
Ivan = True
Isaac = False


drogadictos = [Manuel, Ezequiel, Ivan, Isaac]

cuadrad0 = list(map(lambda x: x **3,numerillos))
print(cuadrad0)

nombres= ["esteban","quito"]

nombresEnumerados = dict(zip(nombres,cuadrad0))

print(nombresEnumerados)

siono = all(x % 2 == 0 for x in numerillos)

print(siono)

droga = list(filter(None,drogadictos))

print(droga)

siono = all(True for x in droga)

print(siono)