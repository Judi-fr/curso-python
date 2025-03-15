def hola():
    print("Hola mundo")


def adios():
    print("Adiós mundo")


saludos = [hola, hola, adios]

for saludo in saludos:
    print("🔥 Invocando función 🔥", saludo.__name__)
    saludo()
