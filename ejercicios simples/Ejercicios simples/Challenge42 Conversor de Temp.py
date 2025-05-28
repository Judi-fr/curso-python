

'''
DESAFIO N~'42
 * CONVERSOR DE TEMPERATURA
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que transforme grados Celsius en Fahrenheit y viceversa.
 * - Para que un dato de entrada sea correcto debe poseer un símbolo "° o  º" y su unidad ("C" o "F").
 * - En caso contrario retornará un error.

de Celsius a Fahrenheit round((Celsius * 9/5) + 32,2)°F"
de Fahrenheit a Celsius round((degrees - 32) * 5/9,2)°C"

'''
"""
while True:
    numero = input ("ingrese un valor:")
    if numero.replace("-","",1).isdigit() :
        numero = int(numero)
        print (f"casting de string a entero {numero} {type(numero)}")
    elif numero.replace("-","",1).replace(".","",1).isdigit() :
        numero = float(numero)
        print (f"casting de string a float {numero} {type(numero)}")
    elif numero.replace("-","",1).upper().replace(".","",1).replace("J","",1).isdigit() :
        numero = complex(numero)
        print (f"casting de string a complex {numero} {type(numero)}")
    else:
        print (f"su dato {numero} no fue acepto")
"""
entrada=""
# entrada y validar datos
while not entrada.replace("-","",1).replace("+","",1).replace("C","",1).replace("F","",1).isnumeric() or \
        ("C" not in entrada and\
        "F" not in entrada ):
    entrada=input("ingrese la temperatura + F o C:").upper()
    entrada=entrada.replace("º","").replace("°","").replace(" ","").replace(",",".",1)
    

if "F" in entrada and "C" not in entrada:
    valor = (float(entrada.replace("F","")))
    salida = round((valor - 32) * 5/9,2)
    salida = str(salida)+"ºC"
    print (f"la conversión es de {entrada} a {salida}")
elif "C" in entrada and "F" not in entrada:
    valor = (float(entrada.replace("C","")))
    salida = round((valor * 9/5) + 32,2)
    salida = str(salida)+"ºF"
    print (f"la conversión es de {entrada} a {salida}")
else:
    print ("ingreso de datos invalidos")
    








exit()

def temperatureConverter(degrees):
    try :
        if "°C" in degrees.upper():
            degrees=degrees.upper().replace(" ","").replace("°C","")
            degrees=eval(degrees)
            salida= f"{round((degrees * 9/5) + 32,2)}°F"

        elif "°F" in degrees.upper():
            degrees=degrees.upper().replace(" ","").replace("°F","")
            degrees=eval(degrees)
            salida= f"{round((degrees - 32) * 5/9,2)}°C"
        else:
            raise
    except:
        salida="Error en los datos"       
    return salida


print(f'{temperatureConverter("100°C")}')
print(f'{temperatureConverter("100°F")}')
print(f'{temperatureConverter("100C")}')
print(f'{temperatureConverter("100F")}')
print(f'{temperatureConverter("100")}')
print(f'{temperatureConverter("100")}')
print(f'{temperatureConverter("- 100 °C ")}')
print(f'{temperatureConverter("- 100 °F ")}')
print(f'{temperatureConverter("100A°C")}')
print(f'{temperatureConverter("100A°F")}')
print(f'{temperatureConverter("°C")}')
print(f'{temperatureConverter("°F")}')
