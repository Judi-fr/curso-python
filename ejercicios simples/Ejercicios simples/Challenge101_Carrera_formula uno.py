import json

#fuente
aux =  "tiempo_Total en pista", "vuelta Mas Rapida", "total de vueltas"

pilotos = ["Yuki Tsunoda",
            "Sergio Pérez",
            "Carlos Sainz",
            "Max Verstappen",
            "Lando Norris",
            "George Russell",
            "Esteban Ocon",
            "Charles Leclerc",
            "Yuki Tsunoda",
            "Oscar Piastri",
            "Fernando Alonso",
            "Lewis Hamilton",
            "Pierre Gasly",
            "Lance Stroll",
            "Nyck de Vries",
            "Kevin Magnussen",
            "Valtteri Bottas",
            "Guanyu Zhou",
            "Alexander Albon",
            "Logan Sargeant",
            "Nico Hulkenberg"]



tiempos = [[3610, 115, 30],
            [6150, 115, 52],
            [6153, 116, 52],
            [6140, 116, 52],
            [6141, 116, 52],
            [6160, 115, 52],
            [6165, 114, 52],
            [6172, 112, 52],
            [6175, 115, 52],
            [6177, 114, 52],
            [4720, 111, 40],
            [6111, 114, 52],
            [700, 119, 5],
            [6201, 118, 52],
            [6133, 114, 52],
            [1205, 118, 10],
            [6272, 122, 52],
            [6375, 135, 52],
            [6475, 144, 52],
            [5720, 151, 30],
            [6130, 11, 52]      ]
pilotos_escuderias=["George Russell","MERCEDES",
                    "Lewis Hamilton","MERCEDES",
                    "Pierre Gasly","ALPINE",
                    "Esteban Ocon","ALPINE",
                    "Nico Hulkenberg","HAAS",
                    "Kevin Magnussen","HAAS",
                    "Oscar Piastri","MCLAREN",
                    "Lando Norris","MCLAREN",
                    "Sergio Pérez","RED BULL",
                    "Max Verstappen","RED BULL",
                    "Fernando Alonso","ASTON MARTIN",
                    "Lance Stroll","ASTON MARTIN",
                    "Nyck de Vries","ALPHATAURI",
                    "Yuki Tsunoda","ALPHATAURI",
                    "Carlos Sainz","FERRARI",
                    "Charles Leclerc","FERRARI",
                    "Valtteri Bottas","ALFA ROMEO",
                    "Guanyu Zhou","ALFA ROMEO",
                    "Alexander Albon","WILLIAMS",
                    "Logan Sargeant","WILLIAMS"]






#tiempos2 = dict()
tiempos2 = {}


print (f"el objeto contiene {tiempos2}  es del tipo {type (tiempos2}")

"""
Se acaba de correr una carrera de F1 de 52 vueltas. Sabemos que corrieron a lo sumo 20 pilotos.

Los datos estan cargados en un diccionario en donde el nombre del piloto es la clave a la que se le asocian tres valores
enteros que representan la duración de la carrera, la de la vuelta mas rapida y la cantidad de vueltas que realizó,
respectivamente.

Los dos primeros datos estan dados en segundos
Ejemplo:
    Hamilton,   6115,113,52
    Vettel,     4720,112,40

Significa que Hamilton completé la carrera en 6115 segundos, su vuelta mas rapida fue de 113 segundos y finaliz6 la
carrera ya que hizo las 52 vueltas. Vettel tuvo su vuelta mas rapida en 112 segundos pero no finalizé la carrera, ya que
completé solo 40 vueltas

Se pide, hacer un programa en Python que:

    'Se proporsionan los datos en un diccionario con listas como valores.'
    'tranformalo en un dicionario con otro diccionario anidado' en base a la aux
Ej
    origen <clave>:    <    lista   >  pasar a < clave > :<                              valor                                               >
                                                          {  <sub clave 1         :val 1>,<sub clave 2       :val 1>,<sub clave 3      :val 3>
          {"Hamilton":[6115, 113, 52], ====>  "Hamilton": {"tiempo_Total en pista":6115  ,"vuelta Mas Rapida":113   ,"total de vueltas":52    },
           "Bottas":  [3610, 115, 30], ====>  "Bottas":   {"tiempo_Total en pista":3610  ,"vuelta Mas Rapida":115   ,"total de vueltas":30    },

cada_clave='Hamilton'
                tiempo_Total en pista=6115
                vuelta Mas Rapida=113
                total de vueltas=52

0) Estructura de datos:
1) Manupulacion de datos:
    A)Genera dos listas de los pilotos que abandonaro y los que no.

    B) Quien gano, con que tiempos de vuelta y totales

    C) Genera el dicionario del podio
    podio= {
            "primero":{"Apellido":"","tiempo_Total en pista":0, "vuelta Mas Rapida":0},
            "segundo":{"Apellido":"","tiempo_Total en pista":0, "vuelta Mas Rapida":0},
            "tercero":{"Apellido":"","tiempo_Total en pista":0, "vuelta Mas Rapida":0}
            }

    D) Genera el dicionario de os 3 pilotos mas rápidos
    piloto_mas_rapido= {
                        "Apellido1":puntos1,
                        "Apellido2":puntos2,
                        "Apellido3":puntos3,
                        }

    E) Genera el diccionario de puntage obtenido por cada piloto: puntaje.
    Para simplificar, solo reciben puntos los pilotos que hayan finalizado la carrera,
    salvo que sea el piloto que hizo la vuelta mas rapida quien recibirá un punto extra haya o no finalizado la carrera.
    datos:
            puntos = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

    En base a la lista de puntos por posición (el primero 25, el segundo 18, etc.)
2) Escuderías
    F) Puntos por escuderia
    G) Podio escuderia
3)  Menu con opciones y colores
4)  Guardan en Excel y BBDD
"""




exit()
#2020
aux =  "tiempo_Total en pista", "vuelta Mas Rapida", "total de vueltas"
tiempos_1 = {
            "Hamilton":[6115, 113, 52],
            "Bottas":[3610, 115, 30],
            "Verstappen":[6111, 114, 52],
            "Perez":[6150, 115, 52],
            "Leclerc":[6153, 116, 52],
            "Ricciardo":[6140, 116, 52],
            "Sainz":[6141, 116, 52],
            "Norris":[6160, 115, 52],
            "Albon":[6165, 114, 52],
            "Gasly":[6172, 112, 52],
            "Stroll":[6175, 115, 52],
            "Ocon":[6177, 114, 52],
            "Vettel":[4720, 111, 40],
            "Kvyat":[700, 119, 5],
            "Lucas":[600, 116, 5],
            "Hulkenberg":[6201, 118, 52],
            "Raikkonen":[6133, 114, 52],
            "Giovinazzi":[1205, 118, 10],
            "Grosjean":[6130, 115, 52],
            }

print (f"{tiempos_1=}")

print (f"{tiempos_1['Vettel']=}")

print (f"{aux[0]} - {tiempos_1['Vettel'][0]=}")
print (f"{aux[1]} - {tiempos_1['Vettel'][1]=}")
print (f"{aux[2]} - {tiempos_1['Vettel'][2]=}")

for cada_clave in tiempos_1.keys():
    print (f"{cada_clave=}")
print ("*"*100)
for cada_valor in tiempos_1.values():
    print (f"{cada_valor=}")
print ("*"*100)
for cada_clave,cada_valor in tiempos_1.items():
    print (f"{cada_clave=} - {cada_valor=}")

print ("*"*100)
aux =  "tiempo_Total en pista", "vuelta Mas Rapida", "total de vueltas"

for cada_clave,cada_valor in tiempos_1.items():
    print (f"{cada_clave=}")
    for index, cada_sub_valor in enumerate(cada_valor):
        print (f"\t\t{aux[index]}={cada_sub_valor}")


exit()
tiempos_2=dict()
for corredor, datos in tiempos_1.items():
    tiempos_2[corredor]= {"tiempo_Total en pista":datos[0], "vuelta Mas Rapida":datos[1], "total de vueltas":datos[2]}
print (tiempos_2)
"""
fuente https://github.com/fedecarboni7/FIUBA/blob/main/algoritmos%20y%20programacion%20I/examenes/consigna.txt

‘Se acaba de correr una carrera de F1 de 52 vueltas. Sabemos que corrieron a lo sumo 20 pilotos.

Los datos estan cargados en un diccionario en donde el nombre del piloto es la clave a la que se le asocian tres valores
enteros que representan la duración de la carrera, la de la vuelta mas rapida y la cantidad de vueltas que realizó,
respectivamente.

Los dos primeros datos estan dados en segundos
Ejemplo:
    Hamilton,   6115,113,52
    Vettel,     4720,112,40

Significa que Hamilton completé la carrera en 6115 segundos, su vuelta mas rapida fue de 113 segundos y finaliz6 la
carrera ya que hizo las 52 vueltas. Vettel tuvo su vuelta mas rapida en 112 segundos pero no finalizé la carrera, ya que
completé solo 40 vueltas

Se pide, hacer un programa en Python que:

    'Se proporsionan los datos en un diccionario con listas como valores.'
    'tranformalo en un dicionario con otro diccionario anidado' en base a la aux
Ej
    origen <clave>:    <    lista   >  pasar a < clave > :<                              valor                                               >
                                                          {  <sub clave 1         :val 1>,<sub clave 2       :val 1>,<sub clave 3      :val 3>
          {"Hamilton":[6115, 113, 52], ====>  "Hamilton": {"tiempo_Total en pista":6115  ,"vuelta Mas Rapida":113   ,"total de vueltas":52    },
           "Bottas":  [3610, 115, 30], ====>  "Bottas":   {"tiempo_Total en pista":3610  ,"vuelta Mas Rapida":115   ,"total de vueltas":30    },

A)Genera dos listas de los pilotos que abandonaro y los que no.
    II) lista los pilotos con mas puntaje
B) Quien gano, con que tiempos de vuelta y totales
C) Genera el dicionario del podio
podio= {
        "primero":{"Apellido":"","tiempo_Total en pista":0, "vuelta Mas Rapida"0},
        "segundo":{"Apellido":"","tiempo_Total en pista":0, "vuelta Mas Rapida"0},
        "tercero":{"Apellido":"","tiempo_Total en pista":0, "vuelta Mas Rapida"0}
        }
D) Genera el dicionario de os 3 pilotos mas rápidos
piloto_mas_rapido= {
                    "Apellido1":puntos1,
                    "Apellido2":puntos2,
                    "Apellido3":puntos3,
                    }

E)Genera el diccionario de puntage obtenido por cada piloto: puntaje.
Para simplificar, solo reciben puntos los pilotos que hayan finalizado la carrera,
salvo que sea el piloto que hizo la vuelta mas rapida quien recibirá un punto extra haya o no finalizado la carrera.
datos:
        puntos = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

En base a la lista de puntos por posición (el primero 25, el segundo 18, etc.)


"""




