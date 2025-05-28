'''
DESAFIO N~#51
 * Reloj
 * Dificultad: FÁCIL
 *
 * Enunciado:
1)                usando for genera un reloj que cuente los minutos (0 a 59)
        luego
2)                usando for genera un reloj que cuente los segundos (0 a 59)
        luego
3)                usando for genera un reloj que cuente los horas (0 a 23)
        luego
4)                usando for genera un reloj que cuente los dias (1 a 31)
        luego
5)                usando for genera un reloj que cuente los meses (1 a 12)
        modifica
6)                los dias desde una tupla con index
        luego
7)                Agrega los nombres de los meses con index
        modifica
8)                los dias y los nombres de los meses con zip

 *
 * bucles anidados
'''

#·············································································································
"""
1)  usando for genera un reloj que cuente los minutos (0 a 59)
"""
recursos = 0
rango_segundos = range(0,60,1)
for segundo in rango_segundos:
    print (f" {segundo=}")
    recursos+=1

print(f"La cantidad de bucles dados  es igual a {recursos} segundos",);

#·············································································································
"""
2)  usando for genera un reloj que cuente los segundos (0 a 59)
"""
recursos = 0
rango_minutos = range(0,60,1)
rango_segundos = range(0,60,1)
for minuto in rango_minutos:
    for segundo in rango_segundos:
        print (f"{minuto=} {segundo=}")
        recursos+=1
    print("-"*50)
print(f"La cantidad de bucles dados  es igual a {recursos} segundos",);
#·············································································································
"""
3)  usando for genera un reloj que cuente los horas (0 a 23)
"""
recursos = 0
rango_horas = range(0,24,1)
rango_minutos = range(0,60,10)#          modificar a step 10 para que sea mas rapido
rango_segundos = range(0,60,10)#         modificar a step 10 para que sea mas rapido
for hora in rango_horas:
    for minuto in rango_minutos:
        for segundo in rango_segundos:
            print (f"{hora=} {minuto=} {segundo=}")
            recursos+=1
        print("-"*50)
    print("="*50)
print(f"La cantidad de bucles dados  es igual a {recursos} segundos",);
#·············································································································
"""
4)  usando for genera un reloj que cuente los dias (1 a 31)
"""
recursos = 0
rango_dias = range(0,32,1)
rango_horas = range(0,24,6)#             modificar a step 6 para que sea mas rapido
rango_minutos = range(0,60,10)#          modificar a step 10 para que sea mas rapido
rango_segundos = range(0,60,10)#         modificar a step 10 para que sea mas rapido
for dia in rango_dias:
    for hora in rango_horas:
        for minuto in rango_minutos:
            for segundo in rango_segundos:
                print (f"{dia=} {hora=} {minuto=} {segundo=}")
                recursos+=1
            print("-"*50)
        print("="*50)
print(f"La cantidad de bucles dados es igual a {recursos} segundos",);
#·············································································································
"""
5)  usando for genera un reloj que cuente los meses (1 a 12)
"""
recursos = 0
rango_horas = range(0,24,6)#             modificar a step 6 para que sea mas rapido
rango_minutos = range(0,60,10)#          modificar a step 10 para que sea mas rapido
rango_segundos = range(0,60,10)#         modificar a step 10 para que sea mas rapido
rango_dias = range(1,32,1)#              suponemos que todos los meses tienen 31 dias
rango_meses = range(0,31,1)
for mes in rango_meses:
    for dia in rango_dias:
        for hora in rango_horas:
            for minuto in rango_minutos:
                for segundo in rango_segundos:
                    print (f"{mes=} {dia=} {hora=} {minuto=} {segundo=}")
                    recursos+=1
                print("-"*50)
            print("="*50)
print(f"La cantidad de bucles dados es igual a {recursos} segundos",);
#·············································································································
"""
6)  los dias desde una tupla
"""
recursos = 0
rango_meses = range(1,12)
rango_horas = range(0,24,6)#             modificar a step 6 para que sea mas rapido
rango_minutos = range(0,60,10)#          modificar a step 10 para que sea mas rapido
rango_segundos = range(0,60,10)#         modificar a step 10 para que sea mas rapido
lista_cantidad_dias=[31,28,31,30,31,30,31,31,30,31,30,31]
for mes in rango_meses:
    fin = lista_cantidad_dias[mes]
    rango_dias = range(0,fin+1,1)
    for dia in rango_dias:
        for hora in rango_horas:
            for minuto in rango_minutos:
                for segundo in rango_segundos:
                    print (f"{dia=} {hora=} {minuto=} {segundo=}")
                    recursos+=1
                print("-"*50)
            print("="*50)
print(f"La cantidad de bucles dados es igual a {recursos} segundos",);
#·············································································································
"""
7)  Agrega los nombres de los meses
"""
recursos = 0
rango_meses = range(0,12)
rango_horas = range(0,24,6)#             modificar a step 6 para que sea mas rapido
rango_minutos = range(0,60,10)#          modificar a step 10 para que sea mas rapido
rango_segundos = range(0,60,10)#         modificar a step 10 para que sea mas rapido
lista_nombre_meses=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
lista_cantidad_dias=[31,28,31,30,31,30,31,31,30,31,30,31]
for mes in rango_meses:
    rango_dias = range(0,lista_cantidad_dias[mes]+1,1)
    for dia in rango_dias:
        for hora in rango_horas:
            for minuto in rango_minutos:
                for segundo in rango_segundos:
                    print (f" {lista_nombre_meses[mes]}   {mes+1=}   {dia=} {dia=} {hora=} {minuto=} {segundo=}")
                    recursos+=1
                print("-"*50)
            print("="*50)
print(f"La cantidad de bucles dados es igual a {recursos} segundos",);
#·············································································································
"""
8)  los dias y los nombres de los meses con zip
"""
lista_nombre_meses=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
lista_cantidad_dias=[31,28,31,30,31,30,31,31,30,31,30,31]
recursos = 0
rrango_horas = range(0,24,6)#            modificar a step 6 para que sea mas rapido
rango_minutos = range(0,60,10)#          modificar a step 10 para que sea mas rapido
rango_segundos = range(0,60,10)#         modificar a step 10 para que sea mas rapido

for nombre_mes,cant_dias_en_mes in zip(lista_cantidad_dias,lista_nombre_meses):
    rango_dias = range(0,cant_dias_en_mes+1,1)
    for dia in rango_dias:
        for hora in rango_horas:
            for minuto in rango_minutos:
                for segundo in rango_segundos:
                    print (f" {nombre_mes}   {dia=} {hora=} {minuto=} {segundo=}")
                    recursos+=1
                print("-"*50)
            print("="*50)
print(f"La cantidad de bucles dados es igual a {recursos} segundos",);

#·············································································································
"""
9)  calculo de años  
"""
year=""
while not year.isnumeric() or len(year)!=4:
    year= input ("ingrese el año actual (yyyy):")
year= int(year)
currentYear = year + 1
if not (currentYear % 4 == 0 and (currentYear % 100 != 0 or currentYear % 400 == 0)) :
    lista_cantidad_dias[1]= 29
    print ("Año B")
recursos = 0
rrango_horas = range(0,24,6)#            modificar a step 6 para que sea mas rapido
rango_minutos = range(0,60,10)#          modificar a step 10 para que sea mas rapido
rango_segundos = range(0,60,10)#         modificar a step 10 para que sea mas rapido
lista_nombre_meses=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
lista_cantidad_dias=[31,28,31,30,31,30,31,31,30,31,30,31]
for nombre_mes,cant_dias_en_mes in zip(lista_cantidad_dias,lista_nombre_meses):
    rango_dias = range(0,cant_dias_en_mes+1,1)
    for dia in rango_dias:
        for hora in rango_horas:
            for minuto in rango_minutos:
                for segundo in rango_segundos:
                    print (f" {nombre_mes}   {dia=} {hora=} {minuto=} {segundo=}")
                    recursos+=1
                print("-"*50)
            print("="*50)
print(f"La cantidad de bucles dados es igual a {recursos} segundos",);





