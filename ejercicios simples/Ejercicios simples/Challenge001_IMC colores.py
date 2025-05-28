# ~ from __init__ import *

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AGT1973
# Copyright 2023 Ariel H Garcia Traba <cursos.agt@gmail.com> +54 9 11 4475 4637
import os
import time
try:
    from colorama import *
except Exception as error_:
    import pip
    pip.main(['install', 'colorama'])
    from colorama import *
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')

def pausa():
    input("\tPresione una tecla para continuar")
    print("\n")
'''
fuente : https://es.wikipedia.org/wiki/%C3%8Dndice_de_masa_corporal

Clasificación   IMC (kg/m²)

Valores principales Valores adicionales
Peso bajo                   <18.50     
     Delgadez severa            <16.00      
     Delgadez moderada          16.00-16.99     
     Delgadez leve              17.00-18.49     
Normal                      18.50-24.99     
Sobrepeso                   ≥25.00
     Preobesidad                25.00-29.99     
     Obesidad                   ≥30.00
          leve                      30.00-34.99     
          media                     35.00-39.99    
          mórbida                   40.00      


Algunas organizaciones consideran sobrepeso un índice superior a 27.0.
En adultos (mayores de 18 años) estos valores son independientes de la edad. sea hombre o mujer.


Categoría de nivel de peso  Intervalo del percentil
Bajo peso                   Menos del percentil 5
Eutrófico                   > percentil 5 y < percentil 85
Sobrepeso                   > 85 hasta y < percentil 95
Obeso                       > percentil 95


Limitaciones

Correlación entre el IMC y el porcentaje de grasa corporal (%BF) de 8550 hombres en una estadística realizada por el National Health and Nutrition Examination Survey. Los datos en el cuadrante superior izquierdo y en el inferior derecho muestran algunas limitaciones del IMC.9​
El matemático Keith Devlin y el Center for Consumer Freedom (asociación de la industria de la restauración) defiende que el error en el IMC es significante y tan habitual que lo hace inútil para la evaluación de la salud.10​11​ El profesor Eric Oliver de la Universidad de Chicago dijo sin embargo que el IMC era conveniente pero también era una medida del peso inexacto. que fuerza a ciertos grupos de la población y debería ser revisado.12​

Escala
El exponente en el denominador de la fórmula para el IMC es arbitrario. El IMC depende del peso y del «cuadrado» de la altura. Mientras que la masa se incrementa del orden de la tercera potencia. al ser una medida que depende del volumen tridimensional. implica que los individuos más altos con la misma forma de cuerpo y composición relativa tienen un índice mayor de BMI.13​

Ignora variaciones en las características físicas
El IMC añade aproximadamente un 10 % para los individuos más altos y recorta aproximadamente otros 10 % para los más pequeños. En otras palabras. una persona con una talla pequeña podría tener más grasa que el óptimo. pero su BMI reflejar que es «normal». Por el contrario. una persona de talla grande (o alto) podría ser un individuo saludable con un índice de grasa bajo. pero ser clasificado con sobrepeso14​

No diferencia entre masa muscular y masa grasa
El IMC asume una distribución entre la masa muscular y la masa grasa que no son ciertas. El IMC generalmente sobreestima el tejido adiposo en aquellos con mayor masa corporal (por ejemplo atletas) y subestima el exceso de grasa en aquellos con menor masa corporal. Un estudio en junio de 2008 por Romero-Corral examinó a 13 601 sujetos de Estados Unidos y encontró que la obesidad (IMC>30) se encontraba presente en el 21 % de los hombres y el 31 % de las mujeres. Sin embargo. usando el porcentaje de grasa corporal se encontró que la obesidad se encontraba en el 50 % de los hombres y el 62 % de las mujeres. A pesar del subcontaje que estimó el IMC. los valores del IMC sí se encontraban en un rango asociado con porcentajes de grasa corporal grandes.

Variación en la relación con la salud
Un estudio publicado por el Journal of the American Medical Association en 2005 demostró que las personas con sobrepeso tienen una probabilidad de morir similar a las personas con peso normal tal y como lo define el IMC. mientras aquellas «obesas» o «por debajo de lo normal» tienen una probabilidad mayor de morir.15​

Un estudio de 2010 que siguieron a 11 000 sujetos durante 8 años concluyó que el IMC no es una buena medida para considerar el riesgo de ataque al corazón. infarto de miocardio o muerte. Una medida mejor podría ser el índice cintura-altura.16​

Un estudio GWAS publicado en 2015 (realizado en población europea). consiguió identificar loci (Locus) relacionados con el IMC y que ejercían diferentes efectos dependiendo de la edad del grupo de población. Gracias a esto. se pudieron establecer co-relaciones con rasgos cardiometabólicos u obesidad. Sin embargo. aún es necesario investigar más en profundidad estas relaciones con muestras poblacionales más amplias. con el fin de obtener una mejor significación y objetivización de los parámetros.17​

IMC y diabetes
Saber si el índice de masa corporal puede correlacionarse con enfermedades como la diabetes tipo 2. ha despertado gran interés en la comunidad científica. Sin embargo. las investigaciones a la fecha no han confirmado una relación directa entre estos dos parámetros.18​19​

El interés despertó a partir de datos extraídos de dos servicios de medicina en Estados Unidos. La mayoría de los pacientes con índice de masa corporal alto tenían tendencia a trastornos en el metabolismo crónicos como la diabetes. Sin embargo. los resultados obtenidos en las investigaciones no lo confirmaron. Dichos estudios dejan en claro que el IMC no es el mejor método para estimar si una persona puede tener diabetes o no.20​

'''
limpiar()
print(F'''{Fore.BLACK+Back.GREEN}
          imc = peso /altura**2                       
Peso bajo                   <18.50                    
     Delgadez severa            <16.00                
     Delgadez moderada          16.00-16.99           
     Delgadez leve              17.00-18.49           
Normal                      18.50-24.99               
Sobrepeso                   ≥25.00                    
     Preobesidad                25.00-29.99           
     Obesidad                   ≥30.00                
          leve                      30.00-34.99       
          media                     35.00-39.99       
          mórbida                   40.00             '''+Style.RESET_ALL)
#pausa()
peso = 75
altura = 1.8
imc = round(peso /(altura**2),2)
"""
Peso bajo                   <18.50                    
Normal                      18.50-24.99               
Sobrepeso                   ≥25.00
"""
"""
if imc < 18.5:#                         condicion inicial
    print ("peso bajo")
else:#                                  todo el universo que no entro en la(s) condicion(es)
    if imc >= 18.5 and imc < 25:
        print ("peso normal")#             condicion secundaria
    else:
        print ("Sobrepeso")#               Todo el universo que no entro en la(s) condicion(es)
        
"""
"""
if imc < 18.5:
    print ("peso bajo")
else:
    if imc < 25:
        print ("peso normal")
    
    else:# if imc >= 25:
        print ("Sobrepeso")
"""
peso = 75
altura = 1.8
imc = round(peso /(altura**2),2)
#imc = 24

print (f"su IMC es de {imc}")
if imc < 18.5:#                         condicion inicial
    if imc < 16:#                       condicion interna o anidada
        print (Fore.BLACK+Back.RED,"peso bajo".ljust(30),Style.RESET_ALL)
        print (Fore.BLACK+Back.RED,"Delgadez severa".center(30),Style.RESET_ALL)
    elif imc < 17:#                     condicion interna o anidada
        print (Fore.BLACK+Back.LIGHTRED_EX,"peso bajo".ljust(30),Style.RESET_ALL)
        print (Fore.BLACK+Back.LIGHTRED_EX,"Delgadez moderada".center(30),Style.RESET_ALL)
    else:#elif imc < 18.5:#             todo lo que no entro en las condicion internas
        print (Fore.BLACK+Back.YELLOW,"peso bajo".ljust(30),Style.RESET_ALL)
        print (Fore.BLACK+Back.YELLOW,"Delgadez leve".center(30),Style.RESET_ALL)

elif imc < 25:#                     condicion secundaria
    print (Fore.BLACK+Back.GREEN,"peso normal".ljust(30),Style.RESET_ALL)
else:# if imc >= 25:#               Todo el universo que no entro en la(s) condicion(es)
    if imc < 30:#                       condicion interna o anidada
        print (Fore.BLACK+Back.YELLOW,"Sobrepeso".ljust(30),Style.RESET_ALL)
        print (Fore.BLACK+Back.YELLOW,"Preobesidad".center(30),Style.RESET_ALL)

    else:#if imc >=30:#             todo lo que no entro en las condicion internas
        if imc < 35:
            print (Fore.BLACK+Back.LIGHTRED_EX,"Sobrepeso".ljust(30),Style.RESET_ALL)
            print (Fore.BLACK+Back.LIGHTRED_EX,"Obesidad".center(30),Style.RESET_ALL)
            print (Fore.BLACK+Back.LIGHTRED_EX,"leve".rjust(30),Style.RESET_ALL)
        elif imc < 40:
            print (Fore.BLACK+Back.LIGHTMAGENTA_EX,"Sobrepeso".ljust(30),Style.RESET_ALL)
            print (Fore.BLACK+Back.LIGHTMAGENTA_EX,"Obesidad".center(30),Style.RESET_ALL)
            print (Fore.BLACK+Back.LIGHTMAGENTA_EX,"media".rjust(30),Style.RESET_ALL)

        else:#elif imc >= 40:
            print (Fore.BLACK+Back.RED,"Sobrepeso".ljust(30),Style.RESET_ALL)
            print (Fore.BLACK+Back.RED,"Obesidad".center(30),Style.RESET_ALL)
            print (Fore.BLACK+Back.RED,"mórbida".rjust(30),Style.RESET_ALL) 
    """
         Preobesidad                25.00-29.99           
         Obesidad                   ≥30.00
              leve                      30.00-34.99       
              media                     35.00-39.99       
              mórbida                   40.00             
             
    """


























    
