"""
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

"""
"""
#factory
from abc import ABC, abstractmethod 

class animal(ABC):
    @abstractmethod
    def Hablar(self):
        pass

class Perro(animal):    
    def Hablar(self):
        print("Guau!")
        
class Gato(animal):    
    def Hablar(self):
        print("Miau!")

class Factory():
    def crear_animal(animal):
        if animal == "Perro":
            return Perro()
        if animal == "Gato":
            return Gato()
                
animal1 = Factory.crear_animal("Perro")
animal1.Hablar()

animal2 = Factory.crear_animal("Gato")
animal2.Hablar()
"""
"""
#factory

from abc import ABC, abstractmethod

class NPC(ABC):
    @abstractmethod
    def Hablar(self):
        pass

class Caster(NPC):
    def Hablar(self):
        print("Te voy a arrancar a los tiros zapallo")

class Melee(NPC):
    def Hablar(self):
        print("Mira que te pincho salamin..")

class Factory():
    def crear_npc(mensaje:str):
        if mensaje == "Caster":
            return Caster()
        if mensaje == "Melee":
            return Melee()

npc = Factory.crear_npc("Caster")
npc.Hablar()

npc = Factory.crear_npc("Melee")
npc.Hablar()

enepese = NPC()
enepese.Hablar()
"""

"""#singleton

class logger():
    singleton = None
    logs = []
    def __new__(cls):
        if cls.singleton == None:
            cls.singleton = super().__new__(cls) 
        return cls.singleton
    
    def ingresar(cls,mensaje:str):
        cls.logs.append(mensaje)
    def Mostrar(cls):
        for log in cls.logs:
            print(log)

logger1 = logger()
logger1.ingresar("eze capo of the world mundial")
logger1.ingresar("wii are the chanpion")

logger2 = logger()

print("Son el mismo el singleton funciona" if logger1 == logger2 else "No funca")

logger2.Mostrar()"""

