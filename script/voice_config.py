import sys
import os
import speech_recognition as sr
from playsound import playsound
from colorama import Fore, init, Style
from time import localtime, sleep
from ascii import bomGia, boaNoite 

def ifs(texto):
    Hora = localtime()
    init()
    if texto in ["Hola","Hola tío"]:
        print(Fore.RED,Style.DIM,"Hola tío")
        playsound("C:/Users/ezeri/Documents/Python/script/Audios/Hola_tio.mp3")
        print(Fore.RED,Style.DIM,"En que puedo ayudarte?")
        playsound("C:/Users/ezeri/Documents/Python/script/Audios/En_que_puedo_ayudarte.mp3")

    elif texto in ["contate un chiste","Contame un chiste","Cuentame un chiste", "Dame un chiste"]:
        print(Fore.RED,Style.DIM,"¿Que hace una abeja en el gimnasio?")
        playsound("C:/Users/ezeri/Documents/Python/script/Audios/chiste.mp3")
        print(Fore.RED,Style.DIM,"¡Zzzum-ba!")

    elif texto in ["salir","exit","fin del programa","salir del programa"]:
        print(Fore.RED,Style.DIM,"Finalizando el programa..")
        playsound("C:/Users/ezeri/Documents/Python/script/Audios/Finalizando_programa.mp3")
        sys.exit(0)

    elif texto in ["abrir póker","Abre poker","abre poker","poker","timba","y el poker","abrir el poker","abrí el póker","abrí el póquer","abrí el poker"]:
        print(Fore.RED,Style.DIM,"Salio esa timba perro")
        playsound("C:/Users/ezeri/Documents/Python/script/Audios/timba.mp3")
        os.system(r'"C:/Users/ezeri/AppData/Roaming/GGPCOM/bin/launcher.exe"')
        
    elif texto in ["Qué pensás del estado de Israel"]:
        print(Fore.RED,Style.DIM,"Una manga de giles..")
        playsound("C:/Users/ezeri/Documents/Python/script/Audios/giles.mp3")

    elif texto in ["abre campus", "abrir campus", "abrí el campus","Campus","abrir el campus","abre el campus","abre campos"]:
        print(Fore.RED,Style.DIM,"En ello..")
        playsound("C:/Users/ezeri/Documents/Python/script/Audios/En_ello.mp3")
        os.system(r'start chrome "https://frgp.cvg.utn.edu.ar/"')

    elif texto in["Google Chrome","Abre Google Chrome","Abrir Google Chrome","Abri Google Chrome"]:
        print(Fore.RED,Style.DIM,"En ello..")
        playsound("C:/Users/ezeri/Documents/Python/script/Audios/En_ello.mp3")
        os.system(r'"C:/Program Files/Google/Chrome/Application/chrome.exe"')

    elif texto in ["te quiero mucho","Gracias quiero mucho","quiero mucho","quiero","gracias Te quiero mucho","Gracias te quiero mucho"]:
        print(Fore.RED,Style.DIM,"Yo tambien te quiero mucho UwU")
        playsound("C:/Users/ezeri/Documents/Python/script/Audios/me_quiere.mp3")
    
    elif texto in ["Puta"]:
        pass
    
    print(Style.RESET_ALL)



def escuchar_lo_dicho():
    
    r = sr.Recognizer()

    with sr.Microphone() as fuente:
        r.adjust_for_ambient_noise(fuente)
        audio = r.listen(fuente)

    try:
        texto = r.recognize_google(audio,language="es-AR")
        print(texto)
        ifs(texto)
    except sr.UnknownValueError:
        print("No entendi.")
        sleep(1)
    except sr.RequestError:
        print("Error de Conexion")
    




    """elif texto in ["bom dia", "boa noite", "boa tarde"]:
        init()
        if Hora[3] > 13 and Hora[3] < 18:
            print(Fore.MAGENTA +Style.BRIGHT+boaNoite )
            playsound("C:/Users/ezeri/Documents/Python/script/Audios/Boa_Tarde.mp3")
        elif Hora[3] > 18 or Hora[3]<6:
            print(Fore.MAGENTA +Style.BRIGHT+boaNoite )
            playsound("C:/Users/ezeri/Documents/Python/script/Audios/Boa_noite.mp3")
        elif Hora[3]>6 and Hora[3]<13:
            print(Fore.MAGENTA +Style.BRIGHT+bomGia)
            playsound("C:/Users/ezeri/Documents/Python/script/Audios/Bom_dia.mp3")"""