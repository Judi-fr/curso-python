from __init__ import *
print('''
Genera has un script donde el usuario ingrese un valor seguido de una de las siglas 
        (m para metro,
         y para yarda
         comilla doble para pulgada y 
         p para pie)
         
         
luego de un - la medida hay q convertirlo:
ej :
    10m-p           10 metros a pies       = 32.8084 pies
    10"-y           10 pugadas a yardas    = 0.277778 yardas
Unidades de Medida:
1 metro = 1.09361 yardas = 39.3701 pulgadas = 3.28084 pies
1 yarda = 0.9144 Metros= 3 pies= 36 pulgadas
1 pulgada = 0.0254 Metros= 0.0277778 yardas= 0.0833333 pies
1 pie = 0.3048 Metros= 0.333333 Yardas= 12 pulgadas
x=1
print (f"{x=}")
''')
# ~ pausa()
# ~ limpiar()
#######################################################################################################


matriz={
'm': {'y':1.09361 ,'"':39.370100 ,'p': 3.2808400 },
'y': {'m':0.91440 ,'p':3.0000000 ,'"': 36.000000 },
'"': {'m':0.02540 ,'y':0.0277778 ,'p': 0.0833333 }, 
'p': {'m':0.30480 ,'y':0.3333330 ,'"': 12.000000 }
}

x=''
while x != 'S' :
    parte_numerica=""
    tipo_medida_entrada=""
    while not parte_numerica.replace(".","").isdigit() or tipo_medida_entrada not in matriz.keys():
        entrada =input("ingrese el valor de entrada, y la designacion del tipo de medida:")
        entrada = entrada.strip(" ")
        #ej   20m
        print (f"'{entrada=}'")
        parte_numerica = entrada[0:-1]
        tipo_medida_entrada=entrada[-1]
        tipo_medida_entrada=tipo_medida_entrada.lower()
        parte_numerica=parte_numerica.strip(" ")


    parte_numerica=float(parte_numerica)
    tipo_medida_salida=""
    while tipo_medida_salida not in matriz.keys() or tipo_medida_salida==tipo_medida_entrada:
        tipo_medida_salida =input("ingrese la designacion del tipo de medida de salida:").lower()
    print ("*"*100)
    print (f"{parte_numerica} {tipo_medida_entrada}")
    print (f"equivalen a :")
    print (f"{parte_numerica*matriz[tipo_medida_entrada][tipo_medida_salida]} {tipo_medida_salida}")
    print ("*"*100)
    x= input("desea salir (s)").upper()

matriz_mini= {"m":1,"y":1.09361, '"':39.3701,"p":3.28084}
x=''
while x != 'S' :
    parte_numerica=""
    tipo_medida_entrada=""
    while not parte_numerica.replace(".","").isdigit() or tipo_medida_entrada not in matriz_mini.keys():
        entrada =input("ingrese el valor de entrada, y la designacion del tipo de medida:")
        entrada = entrada.strip(" ")
        #ej   20m
        print (f"'{entrada=}'")
        parte_numerica = entrada[0:-1]
        tipo_medida_entrada=entrada[-1]
        tipo_medida_entrada=tipo_medida_entrada.lower()
        parte_numerica=parte_numerica.strip(" ")


    parte_numerica=float(parte_numerica)
    tipo_medida_salida=""
    while tipo_medida_salida not in matriz_mini.keys() or tipo_medida_salida==tipo_medida_entrada:
        tipo_medida_salida =input("ingrese la designacion del tipo de medida de salida:").lower()
    print ("*"*100)
    print (f"{parte_numerica} {tipo_medida_entrada}")
    print (f"equivalen a :")
    print (f"{matriz_mini[tipo_medida_salida]*(parte_numerica/matriz_mini[tipo_medida_entrada])} {tipo_medida_salida}")
    print ("*"*100)
    x= input("desea salir (s)").upper()
## Solucion





valor   = es_flotante()
entrada = es_medida("entrante")
salida  = es_medida("saliente")

print (f"{valor} {entrada} de entrada equivalen a {round(matriz[salida]*(valor/matriz[entrada]),3)} {salida}")








exit()

def es_flotante():
    valor = ""
    while valor.replace(".","").isdigit() is False:
        valor = input("Ingrese el valor:")
    return float(valor)
def es_medida(tipo):
    medida = ""
    while not medida in matriz.keys() :
        medida = input(f"Ingrese la medida {tipo} {list(matriz.keys())} :").lower()
        if len(medida)==1:
            for clave in matriz.keys():
                if medida==clave[0]:
                    medida = clave

        # ~ medida =[ clave for clave in matriz.keys() if ( len(medida)==1 and  medida == clave[0]) else list(medida) if (len(medida)>1 and  medida in matriz.keys())]
    return medida




matriz ={"metro":   { "yarda":1.09361,  "pulgada": 39.3701, "foot":3.28084},
        "yarda" :   { "metro": 0.9144,  "pulgada":36,       "foot": 0.9144},
        "pulgada":  { "metro":0.0254,   "yarda": 0.0277778, "foot":0.0833333},
        "foot" :    { "metro": 0.3048,  "yarda":0.333333,   "pulgada":12}}
valor   = es_flotante()
entrada = es_medida("entrante")
salida  = es_medida("saliente")

print (f"{valor} {entrada} de entrada equivalen a {round((valor*matriz[entrada][salida]),3)} {salida}")



matriz= {"metro":1,"yarda":1.09361, "pulgada":39.3701,"foot":3.28084}

valor   = es_flotante()
entrada = es_medida("entrante")
salida  = es_medida("saliente")

print (f"{valor} {entrada} de entrada equivalen a {round(matriz[salida]*(valor/matriz[entrada]),3)} {salida}")

































