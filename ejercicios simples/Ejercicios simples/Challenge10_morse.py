#######################################################################################################
import os
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')
def pausa():
    input("\tEnter para continuar")
from colorama import *
#######################################################################################################
limpiar()
from datetime import datetime, date, time
# ~ pausa();limpiar();#(0,estado='inicio',modulo=4)
import math
import datetime
import pandas 

####################################################################################################
#                                                                                                  #
#                                        Bases de datos                                            #
#                                                                                                  #
####################################################################################################

print(F'''{Fore.WHITE+ Style.BRIGHT + Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║              ╦     ╔═════╗     ╔═══╦═══╗   ╔═══════╗     ╔═════╗            ║
║              ║    ╔╝     ╚╗        ║       ║            ╔╝     ╚╗           ║
║              ║    ║                ║       ║            ║       ║           ║
║              ║    ╚╗               ║       ║            ║       ║           ║
║              ║     ╚═════╗         ║       ╠══════╣     ╠═══════╣           ║
║              ║           ╚╗        ║       ║            ║       ║           ║
║              ║    ╚╗     ╔╝        ║       ║            ║       ║           ║
║              ╩     ╚═════╝         ╩       ╚═══════╝    ╩       ╩           ║
║                                                                             ║
║    ╔═══════╗            ╦                                   ╦   ╔═══╦═══╗   ║
║    ║                    ║                                   ║       ║       ║
║    ║                    ║                                   ║       ║       ║
║    ║                    ║                                   ║       ║       ║
║    ╠══════╣     ╔═══════╣    ╦       ╦    ╔═══════╗         ║       ║       ║
║    ║            ║       ║    ║       ║    ║                 ║       ║       ║
║    ║            ║       ║    ║       ║    ║          ╔╗     ║       ║       ║
║    ╚═══════╝    ╚═══════╝    ╚═══════╝    ╚═══════╝  ╚╝     ╩       ╩       ║
║                                                                             ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣{Style.RESET_ALL}
║                                                                             ║
║    ╔══════╗    ╦       ╦   ╔═══╦═══╗   ╦       ╦    ╔═════╗    ╔╗      ╦    ║
║    ║      ╚╗   ╚╗     ╔╝       ║       ║       ║   ╔╝     ╚╗   ║╚╗     ║    ║
║    ║       ║    ╚╗   ╔╝        ║       ║       ║   ║       ║   ║ ╚╗    ║    ║
║    ║      ╔╝     ╚╗ ╔╝         ║       ║       ║   ║       ║   ║  ╚╗   ║    ║
║    ╠══════╝       ╚╦╝          ║       ╠═══════╣   ║       ║   ║   ╚╗  ║    ║
║    ║               ║           ║       ║       ║   ║       ║   ║    ╚╗ ║    ║
║    ║               ║           ║       ║       ║   ╚╗     ╔╝   ║     ╚╗║    ║
║    ╩               ╩           ╩       ╩       ╩    ╚═════╝    ╩      ╚╝    ║
║                                                                             ║
║                                                                             ║
║                                                                             ║
║  ╔═════╗   ╔╗       ╔╗   ╔═════╗    ╔╗      ╦                               ║
║ ╔╝     ╚╗   ║       ║   ╔╝     ╚╗   ║╚╗     ║                               ║
║ ║       ║   ╚╗     ╔╝   ║       ║   ║ ╚╗    ║                               ║
║ ║       ║    ║     ║    ║       ║   ║  ╚╗   ║                               ║
║ ╠═══════╣    ╚╗   ╔╝    ╠═══════╣   ║   ╚╗  ║  ╠═════╣                      ║
║ ║       ║     ║   ║     ║       ║   ║    ╚╗ ║                               ║
║ ║       ║     ╚╗ ╔╝     ║       ║   ║     ╚╗║                               ║
║ ╩       ╩      ╚═╝      ╩       ╩   ╩      ╚╝                               ║
║                                                                             ║
║                                                                             ║
║                             ╔═══════╗   ╔═════╗  ╔══════╗    ╔═════╗        ║
║                                    ╔╝  ╔╝     ╚╗ ║      ╚╗  ╔╝     ╚╗       ║
║                                   ╔╝   ║       ║ ║       ║  ║       ║       ║
║                                  ╔╝    ║       ║ ║       ║  ║       ║       ║
║                               ╔══╝     ╠═══════╣ ║       ║  ║       ║       ║
║                              ╔╝        ║       ║ ║       ║  ║       ║       ║
║                             ╔╝         ║       ║ ║      ╔╝  ╚╗     ╔╝       ║
║                             ╚═══════╝  ╩       ╩ ╚══════╝    ╚═════╝        ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝''')
pausa()
limpiar()

'''
DESAFIO N~9
 * CÓDIGO MORSE
 * Dificultad: MEDIA
Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
'''


















def decoder(string):
    print ("*"*104)
    print ("*","de string a morse".center(100),"*")
    print ("*"*104)
    salida_morse=""
    for caracter in string.upper():
        """
        if caracter in dict_string_a_morse.keys():
            salida_morse= salida_morse+dict_string_a_morse[caracter]+"  "
        else:
            print (f"caracter no valido {caracter}")
        """
        """
        salida_morse= salida_morse+dict_string_a_morse.get(caracter,f"caracter no valido {caracter}")+"  "
        """
        salida_morse= salida_morse+dict_string_a_morse.get(caracter,"")+"     "
        print (salida_morse)
    return (f"{salida_morse}")
    #----------------------------------------------------------------------
def invertir(dict_string_a_morse):
    dict_morse_a_string={}
    for caracteres,morse in dict_string_a_morse.items():
        dict_morse_a_string[morse]=caracteres
    #print (dict_morse_a_string,type (dict_morse_a_string))
    return dict_morse_a_string
    #---------------------------------------------------------------------
def encoder(morse):
    print ("*"*104)
    print ("*","de morse a string".center(100),"*")
    print ("*"*104)
    salida_string=""
    # ~ print (morse, type(morse))
    lista = morse.replace("     ","#").replace(" ","#").split("#")
    print (lista, type(lista))
    #---------------------------------------------------------------------
    #   opcion 1 dar vuelta el dict
    dict_morse_a_string = invertir(dict_string_a_morse)
    salida_string=""
    for caracter in lista:
        print (f"|{caracter}|",dict_morse_a_string.get(caracter.strip(" ")," "))

        salida_string= salida_string+dict_morse_a_string.get(caracter," ")+""
    return (f'{salida_string.replace("  "," ")}')
    #----------------------------------------------------------------------

dict_string_a_morse = {"A" : ".—", "N" : "—.",     "0" : "—————",
                "B" : "—...",   "Ñ" : "——.——",  "1" : ".————",
                "C" : "—.—.",   "O" : "———",    "2" : "..———",
                "CH": "————",   "P" : ".——.",   "3" : "...——",
                "D" : "—..",    "Q" : "——.—",   "4" : "....—",
                "E" : ".",      "R" : ".—.",    "5" : ".....",
                "F" : "..—.",   "S" : "...",    "6" : "—....",
                "G" : "——.",    "T" : "—",      "7" : "——...",
                "H" : "....",   "U" : "..—",    "8" : "———..",
                "I" : "..",     "V" : "...—",   "9" : "————.",
                "J" : ".———",   "W" : ".——",    "." : ".—.—.—",
                "K" : "—.—",    "X" : "—..—",   "," : "——..——",
                "L" : ".—..",   "Y" : "—.——",   "?" : "..——..",
                "M" : "——",     "Z" : "——..",   "\"": ".—..—.",
                "/" : "—..—.",  " " :" ",       "     ":""}

#salida = input("ingrese un texto :").upper()
string_de_entrada ="Hola Mundo It esto es Python 2025"
en_morse = decoder(string_de_entrada)
print (f"string de entrada original {string_de_entrada}")
print (f"string de entrada {en_morse=}")
string_de_salida = encoder(en_morse)
print (f"string de salida{string_de_salida=}")
print(f"""
comparamos:
{string_de_entrada}\n
{string_de_salida}""")
