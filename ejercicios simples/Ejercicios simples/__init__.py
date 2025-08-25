#singleton

class logger():
    unico = None
    mensajes = []

    def __new__(cls):
        if cls.unico is None:
            cls.unico = super().__new__(cls)
        return cls.unico

    def log(cls,mensaje):
        cls.mensajes.append(mensaje)

    def leer(cls):
        for mensaje in cls.mensajes:
            print(mensaje)


logger1 = logger()
logger1.log("Eze")
logger1.log("capo")
logger2 = logger()

print("true" if logger1 == logger2 else "false")

logger2.leer()