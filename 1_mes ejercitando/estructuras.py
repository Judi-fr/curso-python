import csv
import json


#PARTE 1
"""animales = ["mono","perro","burro","gato","mono"]

animales=set(animales)
dict_animales=dict()

for animal in animales:
    patas=int(input(f"Cuantas patas tiene un {animal}? "))

    dict_animales[animal]=patas

print(dict_animales)

"""
#PARTE 2
"""
unoAlveinte= [x for x in range(1,21)]
print(unoAlveinte)
multiplos3=[x for x in unoAlveinte if x % 3 == 0 ]
print(multiplos3)

dic_cuadrados = {x: (x+5)**2 for x in unoAlveinte}
print(dic_cuadrados)"""

#PARTE 3
"""
with open("Archivo.csv",mode="w",newline="") as archivo:
    escribir = csv.writer(archivo)
    escribir.writerow(["nombre","edad"])
    escribir.writerow(["Ezequiel",24])

with open("Archivo.csv",mode="r") as archivo:
    lector = csv.reader(archivo)
    for registro in lector:
        pass
        #print(registro)

try:
    with open("Archivo.json",mode="r") as archivo:
        datos = json.load(archivo)
except:
    datos = []

#registro = {"Nombre":"Andres","Apellido":"Rieznik"}

#datos.append(registro)

with open("Archivo.json", mode="w") as archivo:
    read = json.dump(datos,archivo,indent=2)

with open("Archivo.json",mode="r") as archivo:
        datos = json.load(archivo)
        print(datos)
    
"""

#PARTE 4
"""
datos = [["nombre","apellido","edad"]]

for datitos in range(2):
    nombre=input("nombre: ")
    apellido=input("apellido: ")
    edad=int(input("edad: "))
    lista=[nombre,apellido,edad]
    datos.append(lista)

with open("ArchivoCSV.csv", mode="w",newline="") as archivo:
    for datitos in datos:
        write = csv.writer(archivo)
        write.writerow(datitos)

diccionario = {}
num=0
with open("ArchivoCSV.csv",mode="r") as archivo:
    read = csv.reader(archivo)
    for i, datos in enumerate(read):
        if i == 0:
            continue
        diccionario[f"ID {i}"] = {"nombre":datos[0],"apellido":datos[1],"edad":datos[2]} 
    print(diccionario)

with open("Archivo.json",mode="w") as archivo:
    write = json.dump(diccionario,archivo,indent=2)
    
with open("Archivo.json", mode="r") as archivo:
    leido = json.load(archivo)
    print(leido)"""

import requests
"""
API_KEY = "72d981895f243ef9d3811084afaa3a52"
ciudad = "Buenos Aires"
url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"

res = requests.get(url)
datos = res.json()


print(f"Clima en {ciudad} : {datos['weather'][0]['description'].capitalize()}")
print(f"Temperatura: {datos['main']['temp']}°C")"""

token="""BEARER eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3ODUzNjE2MzMsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJqdWFuaXRvYWxjYWNob2ZhNTVAaG90bWFpbC5jb20ifQ.7UlljmzrEnvL5lt4G_3gT_D-Q013yjYuYNY3xX3OARiVmjzY2gmyjOCBvil1Gp4Aiz_1RYQX2Nqtf_x7DC4Wig"""
url = "https://api.estadisticasbcra.com/usd"

headers = {"Authorization":token}
res = requests.get(url,headers=headers)

USD = []

if res.status_code == 200:
    for valor in res.json():
        nuevo = {
            "dia" if k == "d" else "valor" if k == "v" else k: v
            for k, v in valor.items()
        }
        USD.append(nuevo)
    with open("Dolar_blue.json", mode="w",encoding="utf-8")as archivo:
        escribir = json.dump(USD,archivo,indent=2,ensure_ascii=False)
        
else:
    print(f"❌ Error: {res.status_code}")
    print(res.text)