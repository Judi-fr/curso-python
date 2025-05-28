'''
Genere un script donde el medico ingrese los argumentos del pasiente (peso y altura)
imprime las categorias y  subcategorias:

Ej:
    categorias
         subcategorias
            subsubcategorias
________________________________
    Peso bajo                       
        Delgadez moderada
________________________________
    Sobrepeso             
        Obesidad
            Obesidad media
________________________________
    Normal
________________________________

datos:

https://es.wikipedia.org/wiki/%C3%8Dndice_de_masa_corporal

Clasificación   IMC (kg/m²)

________________________________
Valores principales Valores adicionales
Peso bajo                          <18,50      
     Delgadez severa               <16,00      
     Delgadez moderada        16,00-16,99     16,00 -  <17  
     Delgadez leve            17,00-18,49     17,00 - < 18,5 
Normal                        18,50-24,99     18,50 - < 25 
                                        
Sobrepeso                         >=25,00      
     Preobesidad              25,00-29,99     25,00 - < 30  
     Obesidad                     >=30,00      
          Obesidad leve       30,00-34,99     30,00 - < 35
          Obesidad media      35,00-39,99     35,00 - < 40
          Obesidad mórbida        >=40,00     

Algunas organizaciones consideran sobrepeso un índice superior a 27.0.
En adultos (mayores de 18 años) estos valores son independientes de la edad, sea hombre o mujer.


Categoría de nivel de peso  Intervalo del percentil
Bajo peso                   Menos del percentil 5
Eutrófico                   > percentil 5 y < percentil 85
Sobrepeso                   > 85 hasta y < percentil 95
Obeso                       > percentil 95



Algunas organizaciones consideran sobrepeso un índice superior a 27.0.
En adultos (mayores de 18 años) estos valores son independientes de la edad, sea hombre o mujer.


Categoría de nivel de peso  Intervalo del percentil
Bajo peso                   Menos del percentil 5
Eutrófico                   > percentil 5 y < percentil 85
Sobrepeso                   > 85 hasta y < percentil 95
Obeso                       > percentil 95


Limitaciones

Correlación entre el IMC y el porcentaje de grasa corporal (%BF) de 8550 hombres en una estadística realizada por el National Health and Nutrition Examination Survey. Los datos en el cuadrante superior izquierdo y en el inferior derecho muestran algunas limitaciones del IMC.9​
El matemático Keith Devlin y el Center for Consumer Freedom (asociación de la industria de la restauración) defiende que el error en el IMC es significante y tan habitual que lo hace inútil para la evaluación de la salud.10​11​ El profesor Eric Oliver de la Universidad de Chicago dijo sin embargo que el IMC era conveniente pero también era una medida del peso inexacto, que fuerza a ciertos grupos de la población y debería ser revisado.12​

Escala
El exponente en el denominador de la fórmula para el IMC es arbitrario. El IMC depende del peso y del «cuadrado» de la altura. Mientras que la masa se incrementa del orden de la tercera potencia, al ser una medida que depende del volumen tridimensional, implica que los individuos más altos con la misma forma de cuerpo y composición relativa tienen un índice mayor de BMI.13​

Ignora variaciones en las características físicas
El IMC añade aproximadamente un 10 % para los individuos más altos y recorta aproximadamente otros 10 % para los más pequeños. En otras palabras, una persona con una talla pequeña podría tener más grasa que el óptimo, pero su BMI reflejar que es «normal». Por el contrario, una persona de talla grande (o alto) podría ser un individuo saludable con un índice de grasa bajo, pero ser clasificado con sobrepeso14​

No diferencia entre masa muscular y masa grasa
El IMC asume una distribución entre la masa muscular y la masa grasa que no son ciertas. El IMC generalmente sobreestima el tejido adiposo en aquellos con mayor masa corporal (por ejemplo atletas) y subestima el exceso de grasa en aquellos con menor masa corporal. Un estudio en junio de 2008 por Romero-Corral examinó a 13 601 sujetos de Estados Unidos y encontró que la obesidad (IMC>30) se encontraba presente en el 21 % de los hombres y el 31 % de las mujeres. Sin embargo, usando el porcentaje de grasa corporal se encontró que la obesidad se encontraba en el 50 % de los hombres y el 62 % de las mujeres. A pesar del subcontaje que estimó el IMC, los valores del IMC sí se encontraban en un rango asociado con porcentajes de grasa corporal grandes.

Variación en la relación con la salud
Un estudio publicado por el Journal of the American Medical Association en 2005 demostró que las personas con sobrepeso tienen una probabilidad de morir similar a las personas con peso normal tal y como lo define el IMC, mientras aquellas «obesas» o «por debajo de lo normal» tienen una probabilidad mayor de morir.15​

Un estudio de 2010 que siguieron a 11 000 sujetos durante 8 años concluyó que el IMC no es una buena medida para considerar el riesgo de ataque al corazón, infarto de miocardio o muerte. Una medida mejor podría ser el índice cintura-altura.16​

Un estudio GWAS publicado en 2015 (realizado en población europea), consiguió identificar loci (Locus) relacionados con el IMC y que ejercían diferentes efectos dependiendo de la edad del grupo de población. Gracias a esto, se pudieron establecer co-relaciones con rasgos cardiometabólicos u obesidad. Sin embargo, aún es necesario investigar más en profundidad estas relaciones con muestras poblacionales más amplias, con el fin de obtener una mejor significación y objetivización de los parámetros.17​

IMC y diabetes
Saber si el índice de masa corporal puede correlacionarse con enfermedades como la diabetes tipo 2, ha despertado gran interés en la comunidad científica. Sin embargo, las investigaciones a la fecha no han confirmado una relación directa entre estos dos parámetros.18​19​

El interés despertó a partir de datos extraídos de dos servicios de medicina en Estados Unidos. La mayoría de los pacientes con índice de masa corporal alto tenían tendencia a trastornos en el metabolismo crónicos como la diabetes. Sin embargo, los resultados obtenidos en las investigaciones no lo confirmaron. Dichos estudios dejan en claro que el IMC no es el mejor método para estimar si una persona puede tener diabetes o no.20​

'''
limpiar()
print(F'''{Fore.WHITE+Back.BLUE}

Peso bajo                       <18,50      
     Delgadez severa            <16,00      
     Delgadez moderada          16,00-16,99 
     Delgadez leve              17,00-18,49 
Normal                          18,50-24,99 
Sobrepeso                       >=25,00     
     Preobesidad                25,00-29,99 
     Obesidad                   >=30,00     
          Obesidad leve         30,00-34,99 
          Obesidad media        35,00-39,99 
          Obesidad mórbida      40,00      ''',Style.RESET_ALL)
pausa()













salir=False
while  salir  is False:
    nombre = input("ingrese su nombre :").title()
    peso =""
    while peso.replace(".","").isdecimal() is False:
        peso = input (f"por favor {nombre} engrese su peso en kg :")
    peso = float(peso)
    altura=""
    while altura.replace(".","").isdecimal() is False:
        altura = input (f"por favor {nombre} engrese su aptura en metros :")
    altura = float(altura)
    imc = peso/(altura**2)
    print (f"{nombre} su IMC es de {imc}")
    '''
    Peso bajo                          <18,50      
         Delgadez severa               <16,00      
         Delgadez moderada        16,00-16,99     16,00 -  <17  
         Delgadez leve            17,00-18,49     17,00 - < 18,5 
    Normal                        18,50-24,99     18,50 - < 25 
                                            
    Sobrepeso                         >=25,00      
         Preobesidad              25,00-29,99     25,00 - < 30  
         Obesidad                     >=30,00      
              Obesidad leve       30,00-34,99     30,00 - < 35
              Obesidad media      35,00-39,99     35,00 - < 40
              Obesidad mórbida        >=40,00     
    '''
    if imc<18.5:
        print ("peso bajo")
        if imc < 16:
            print ("\tDelgadez severa")
        elif imc < 17:
            print ("\tDelgadez moderada")    
        else: #elif imc < 18,5:
            print ("\tDelgadez leve")
            
    elif imc<25:
        if imc <20:#entre >= 18.5 y <20
            print ("peso normal")
            print ("\tbajo")
        elif imc<22:#entre >= 20 y <22         
            print ("peso normal")
        else: #elif imc<25::#entre >=20 y < 25    
            print ("peso normal")
            print ("\talto")
    
    else:
        print ("Sobrepeso")
        if  imc<30:
            print ("\tPreobesidad")
        else: # elif imc>=30
            print ("\tObesidad")
            if imc <35:
                print ("\t\tleve")
            elif imc <40:
                print ("\t\tmedia")
            else: #elif imc>=40:
                print ("\t\tmórbida")
    salir = input ("s pasa Salir\n enter para continuar :")
    #if salir =='S' or salir =="s":
    
    if salir.upper() =='S':
        salir = True
    else:
        salir = False




exit()
##Solucion

salida = ""
nombre_paciente = ""
peso_paciente = ""
altura_paciente = ""

while len (nombre_paciente)<3 or nombre_paciente.replace(" ","").isalpha() is False:
    nombre_paciente = input ("por favor ingrese su nombre : ")

while peso_paciente.replace(".","").isdigit() is False:
    peso_paciente = input ("por favor ingrese su peso : ").replace(",",".")
    
while altura_paciente.replace(".","").isdigit() is False:
    altura_paciente = input ("por favor ingrese su altura : ").replace(",",".")
    
nombre_paciente = nombre_paciente.title()
peso_paciente = float(peso_paciente)
altura_paciente = float(altura_paciente)
altura_paciente2 = altura_paciente**2

imc = peso_paciente / altura_paciente2

# ~ imc = 42
if imc < 18.5:
    salida+=("Peso bajo ")
    if imc <= 16:
        salida+=("Delgadez severa ")
    elif imc < 17:
        salida+=("Delgadez moderada ")
    else:
        salida+=("Delgadez leve ")
elif imc < 25:
    salida+= ("Peso normal ")
else:
    salida+=("Sobrepeso ")
    if imc < 30:
        salida+= ("Preobesidad ")
    else:
        salida+= ("Obesidad ")
        if imc < 35:
            salida+=("Obesidad leve ")
        elif imc < 40:
            salida+=("Obesidad media ")
        else:
            salida+=("Obesidad mórbida ")
print(f"{imc} - {salida}")







