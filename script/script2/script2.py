import time
import win32gui
import win32con
import speech_recognition as sr
from playsound import playsound
from IFS import *
import volumen
import cv2
import keyboard

volumen.setear_volumen(18)
playsound("C:/Users/ezeri/Documents/Python/script/script2/audio/AOE.mp3")    


os.system("cls")
def jew():
    playsound("C:/Users/ezeri/Documents/Python/script/script2/audio/jew.mp3")

def bobesponja():
    playsound("C:/Users/ezeri/Documents/Python/script/script2/audio/bobesponja.mp3")    

def Bananero():
    #volumen.setear_volumen(12)
    playsound("C:/Users/ezeri/Documents/Python/script/script2/audio/bananero.mp3")    

def CsGO():
    #volumen.setear_volumen(12)
    playsound("C:/Users/ezeri/Documents/Python/script/script2/audio/CsGO.mp3")    

def picara():
    #volumen.setear_volumen(16)
    playsound("C:/Users/ezeri/Documents/Python/script/script2/audio/mira-que-picara-que-sos.mp3")    

def maryjane():
    #volumen.setear_volumen(9)
    playsound("C:/Users/ezeri/Documents/Python/script/script2/audio/maryjane.mp3")    

def macri():
    #volumen.setear_volumen(12)
    playsound("C:/Users/ezeri/Documents/Python/script/script2/audio/macri.mp3")    


def topturo():

   #volumen.setear_volumen(16)
    img = cv2.imread("C:/Users/ezeri/Documents/Python/script/script2/img/Topuria4.jpg")
    cv2.imshow("el bastardo",img)
    cv2.waitKey(100)

    hwnd = win32gui.FindWindow(None, "el bastardo")
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                      win32con.SWP_NOSIZE | win32con.SWP_NOMOVE | win32con.SWP_SHOWWINDOW)


    playsound("C:/Users/ezeri/Documents/Python/script/script2/audio/Topuria2.mp3")
    cv2.destroyAllWindows()


def escuchar_lo_dicho():
    
    r = sr.Recognizer()

    with sr.Microphone() as fuente:
        r.adjust_for_ambient_noise(fuente)
        playsound("C:/Users/ezeri/Documents/Python/script/script2/audio/TIMBRE.mp3")
        audio = r.listen(fuente)

    try:
        texto = r.recognize_google(audio,language="es-AR")
        analizar(texto)
    except sr.UnknownValueError:
        playsound("C:/Users/ezeri/Documents/Python/script/script2/audio/hueso.mp3")
    except sr.RequestError:
        print("Error de Conexion")
        main()

def main():
    while True:
        keyboard.add_hotkey('ctrl + F2',maryjane)
        keyboard.add_hotkey('ctrl + F3',picara)
        keyboard.add_hotkey('ctrl + F7',macri)
        keyboard.add_hotkey('ctrl + F8',CsGO)
        keyboard.add_hotkey('ctrl + F9',Bananero)
        keyboard.add_hotkey('ctrl + F10',topturo)
        keyboard.add_hotkey('ctrl + F11',bobesponja)
        keyboard.add_hotkey('ctrl + F12',jew)
        keyboard.add_hotkey('ctrl + F1',escuchar_lo_dicho)
        keyboard.wait()

main()