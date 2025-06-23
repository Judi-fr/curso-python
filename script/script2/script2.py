from time import sleep, localtime
import speech_recognition as sr
from playsound import playsound
from IFS import *
from volumen import *
from saludo import *
import keyboard

def jew():
    print("jew")
    setear_volumen(40)
    playsound("C:/Users/ezeri/Documents/Python/script2/audio/jew.mp3")

def escuchar_lo_dicho():
    
    r = sr.Recognizer()

    with sr.Microphone() as fuente:
        r.adjust_for_ambient_noise(fuente)
        playsound("C:/Users/ezeri/Documents/Python/script2/audio/TIMBRE.mp3")
        audio = r.listen(fuente)

    try:
        texto = r.recognize_google(audio,language="es-AR")
        print(texto)
        analizar(texto)
    except sr.UnknownValueError:
        print("No entendi.")
    
    except sr.RequestError:
        print("Error de Conexion")

setear_volumen(40)
saludo()
setear_volumen(60)
while True:
    keyboard.add_hotkey('ctrl + F12',jew)
    keyboard.add_hotkey('ctrl + F1',escuchar_lo_dicho)
    keyboard.wait()
