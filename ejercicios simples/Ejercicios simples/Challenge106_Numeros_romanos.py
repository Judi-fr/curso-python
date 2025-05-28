print(f'''
● Genera un script para pasar de numeros romanos a indo=arábigos
        el numero romano se da como verdadero, no see chequea, 
        su ingreso por el usuario debere ser correcto 
''')

def Solucion1(romano: str) -> int:
    rosetta={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
    # ~ print(f"{romano=} {type(romano)}")
    lista_romano = list(romano.replace(" ","").strip(". ").upper())
    #           1 saco los espacios en puntas   .strip(". ")
    #           2 saco los espacios en el medio .replace(" ","")
    #           3 todo a mayúsculas
    #           4 casting str a lista
    lista_indo_arabigo=[]#list()
    # ~ print(f"{lista_romano=} {type(lista_romano)}")
    for index, caracter_romano in enumerate(lista_romano):
        if caracter_romano not in rosetta.keys():
            ''' 
                si algun caracter no esta dentro de las claves de numeros
                romanos salgo con error "caracteres no romanos"
            '''
            return (f"caracteres {caracter_romano} no romanos")
        # ~ print (f"\t\t{caracter_romano=}")
        '''ej:
             voy al rosettacionario con la clave romano
                 rosetta[x] y traigo el numero indo-arábigo 10
                 rosetta[V] y traigo el numero indo-arábigo 5
                 rosetta[M] y traigo el numero indo-arábigo 1000
        '''
        numero_indo_arabigo=rosetta[caracter_romano]
        lista_indo_arabigo.append(numero_indo_arabigo)
        if index>=1 and  numero_indo_arabigo > lista_indo_arabigo[index-1]:
            lista_indo_arabigo[index-1] = lista_indo_arabigo[index-1]*-1
        # ~ print (f"\t\t{numero_indo_arabigo=}")
    # ~ print (f"\t\t{lista_indo_arabigo=}")
    return sum(lista_indo_arabigo)

def Solucion2(romano: str) -> int:
    rosetta={  'n_romanos':{'I':1,
                            'V':5,
                            'X':10,
                            'L':50,
                            'C':100,
                            'D':500,
                            'M':1000
                           },
                'grupos': { 'IV':4,
                            'IX':9,
                            'XL':40,
                            'XC':90,
                            'CD':400,
                            'CM':900
                        }
        }
    # ~ print(f"{romano=} {type(romano)}")
    romano = romano.replace(" ","").strip(". ").upper()
    #           1 saco los espacios en puntas   .strip(". ")
    #           2 saco los espacios en el medio .replace(" ","")
    #           3 todo a mayúsculas
    lista_indo_arabigo=[]#list()
    # ~ if clave_romana  in rosetta.keys():
        # si algun caracter no esta dentro de las claves de numeros romanos salgo con error
        # ~ return ("caracteres no romanos")
    lista_no_grupo=[]
    for clave_romana, valor_indo_arabigo in rosetta['grupos'].items():
        if clave_romana  in romano:
            lista_indo_arabigo.append(valor_indo_arabigo)     
            romano=romano.replace(clave_romana,"")

        '''
        voy al dicionario `rosetta` sub diccionario `grupo`
            1ro) chequeo si hay grupos:
                 chequeo si cada clave de grupo esta en el string (no lista) de romano
                    si esta 
                            1) paso el valor (número indo-arábigo a la lista_indo_arabigo )
                            2) remplazo el el grupo encontrado en el string por "" nada
                            string  CXCXIX                  XC IX
                                     ^^ ^^ grupos >>>lista [90, 9]
                            string   C  X   quedan en el string
                            
       ej                     
         rosetta['grupo']['IX'] y coloco el lista_indo_arabigo el numero indo-arábigo 9
                saco los 'IX' del string `romano`
         rosetta['grupo']['IV'] y coloco el lista_indo_arabigo el numero indo-arábigo 4
                saco los 'IV' del string `romano`
         rosetta['grupo']['CM'] y coloco el lista_indo_arabigo el numero indo-arábigo 900               
                saco los 'CM' del string `romano`
        '''
    for clave_romana, valor_indo_arabigo in rosetta['grupos'].items():
        if clave_romana  in romano:
            lista_indo_arabigo.append(valor_indo_arabigo)     
            romano=romano.replace(clave_romana,"")
        '''
        voy al dicionario `rosetta` sub diccionario `n_romanos`
            1ro) chequeo si hay numeros que no hayan sido grupos:
                 chequeo si cada clave de n_romanos esta en el string (no lista) de romano
                    si esta 
                            1) paso el valor (número indo-arábigo a la lista_indo_arabigo )
                            2) remplazo el el grupo encontrado en el string por "" nada
                            lista [90, 9]<<<datos desde grupos (anterior)
                            
                            string que queda  C  X   
                                              ^  ^
                                 lista [90,9,100,10]
       ej                     
         rosetta['n_romanos']['X'] y coloco el lista_indo_arabigo el numero indo-arábigo 10
                saco los 'X' del string `romano`
         rosetta['n_romanos']['V'] y coloco el lista_indo_arabigo el numero indo-arábigo 5
                saco los 'V' del string `romano`
         rosetta['n_romanos']['M'] y coloco el lista_indo_arabigo el numero indo-arábigo 1000               
                saco los 'M' del string `romano`'''
    for clave_romana, valor_indo_arabigo in rosetta['n_romanos'].items():
        # ~ print (f"{romano=}")
        for car_romano in romano:
            if clave_romana  == car_romano:
                lista_indo_arabigo.append(valor_indo_arabigo)     
                romano=romano.replace(clave_romana,"",1)
        
    if len(romano)>0:
        return (f"Error {romano}")
    else:
        return sum(lista_indo_arabigo)

def Solucion3(romano: str) -> int:
    rosetta={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
    total= 0
    prev = 0
    '''    romano_inv = reverse(romano)'''
    romano_inv = romano[::-1]
    
    # ~ print (f"\t\t\t{romano=}\n\t\t\t{romano_inv=}")
    '''
    romano     = CMXCIX (999)'
                 ^    ^
                  \  /
                   \/
                   /\
                  /  \
    romano_inv = XICXMC
    Al estar invertido la condicion es sobre el anterior
    '''
    lista_indo_arabigo=[]
    for caracter_romano in romano_inv:
        if rosetta[caracter_romano] < prev:
            valor_indo_arabigo = -rosetta[caracter_romano]
            lista_indo_arabigo.append(valor_indo_arabigo)     
        else:
            valor_indo_arabigo = +rosetta[caracter_romano]
            lista_indo_arabigo.append(valor_indo_arabigo) 
        prev = rosetta[caracter_romano]
    return sum(lista_indo_arabigo)
    
def Solucion4(romano: str) -> int:
    rosetta={
                "I":1,
                "V":5,
                "X":10,
                "L":50,
                "C":100,
                "D":500,
                "M":1000
            }
    '''    romano_inv = reverse(romano)'''
    romano_inv = romano[::-1]
    lista_indo_arabigo=[ -rosetta[caracter_romano] if rosetta[caracter_romano] < (0 if index==0 else rosetta[romano_inv[index-1]] ) else +rosetta[caracter_romano]    for index, caracter_romano in enumerate(romano_inv) ]
    '''
    lista_indo_arabigo=[]
    for index, caracter_romano in enumerate(romano_inv):
        if index==0:
            previo = 0
        else:
            previo = rosetta[romano_inv[index-1]] 
        if rosetta[caracter_romano] < previo:
            lista_indo_arabigo.append(rosetta[caracter_romano]*-1)
        else:
            lista_indo_arabigo.append(rosetta[caracter_romano]*+1)
    '''
    return sum(lista_indo_arabigo)
def Solucion5(romano: str) -> int:
    rosetta={  'n_romanos':{'I':1,
                            'V':5,
                            'X':10,
                            'L':50,
                            'C':100,
                            'D':500,
                            'M':1000
                           },
                'grupos_especial': {
                        "IV" : -2,
                        "IX" : -2,
                        "XL" : -20,
                        "XC" : -20,
                        "CD" : -200,
                        "CM" : -200,
                        }
        }
        
    '''
    Esta solucion es la mas rapide en recursos de micro  y memoria
        1) suma todo caracter romanos (pasandolos a indo-arábigos) sin preocuparse del orden.
        2) Resta el doble de los grupos (una por el que sumo en el primer paso y el segundo necesaro )
    '''
    # estandar
    '''
    lista_indo_arabigo=[]
    for caracter_romano in romano:
        lista_indo_arabigo.append( rosetta['n_romanos'][caracter_romano])
    for grupo_caracteres_romano in rosetta['grupos_especial'].keys():
        if grupo_caracteres_romano in romano:
            lista_indo_arabigo.append(rosetta['grupos_especial'][grupo_caracteres_romano])
    '''
    # por comprenhesion
    lista_indo_arabigo=[rosetta['n_romanos'][caracter_romano] for caracter_romano in romano]+[rosetta['grupos_especial'][grupo_caracteres_romano] for grupo_caracteres_romano in rosetta['grupos_especial'].keys() if grupo_caracteres_romano in romano]
    print(lista_indo_arabigo)
    return sum(lista_indo_arabigo)

while True:
    print("*"*100)
    romano = input("""Ingrese una cifra en numeros romanos:
                "I"=1
                "V"=5
                "X"=10
                "L"=50
                "C"=100
                "D"=500
                "M"=1000
                'S' para Salir
                    datos:""").upper()
    if romano.upper() =='S':
        exit()
    romano2int =Solucion1(romano)
    print (f"Soluncion1:\n\tsu numero romano {romano} equivale a \n\t\t\t'{romano2int}'' en indo-arabigos")
    romano2int =Solucion2(romano)
    print (f"Soluncion2:\n\tsu numero romano {romano} equivale a \n\t\t\t'{romano2int}'' en indo-arabigos")
    romano2int =Solucion3(romano)
    print (f"Soluncion3:\n\tsu numero romano {romano} equivale a \n\t\t\t'{romano2int}'' en indo-arabigos")
    romano2int =Solucion4(romano)
    print (f"Soluncion4:\n\tsu numero romano {romano} equivale a \n\t\t\t'{romano2int}'' en indo-arabigos")
    romano2int =Solucion5(romano)
    print (f"Soluncion5:\n\tsu numero romano {romano} equivale a \n\t\t\t'{romano2int}'' en indo-arabigos")

exit()

    
