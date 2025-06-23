from time import sleep, localtime
from playsound import playsound

def saludo():
        
    Hora = localtime()

    if Hora[3] > 13 and Hora[3] < 18:
                playsound("C:/Users/ezeri/Documents/Python/script2/audio/Boa-tarde.mp3")
    elif Hora[3] > 18 or Hora[3]<6:
                playsound("C:/Users/ezeri/Documents/Python/script2/audio/Boa-noite.mp3")
    elif Hora[3]>6 and Hora[3]<13:
                playsound("C:/Users/ezeri/Documents/Python/script2/audio/Bom-dia.mp3")