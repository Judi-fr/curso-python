'''
para validar un password se requiere que este cumpla con las siguientes condiciones :
                    debe tener minimo de 6 caracteres 
                    al menos una mayuscula, 
                    al menos una minuscula, 
                    al menos un simbolo de teclado y 
                    al menos un numero
'''

simbolos =  ["!","@","#","$","%","^","*","/","+","-","_","(",")","{","}","[","]",":",";",",",".","<",">","?","\\","|","'","~","&","ç","Ç"] 

def funcion_validar_password(password):
    password= list(password)
    # ~ if (len (password)<6):
        # ~ return "incorrecto"
    # ~ flag_may=False
    # ~ flag_min=False
    # ~ flag_sim=False
    # ~ flag_num=False
    # ~ for caracter in password:
        # ~ print (f"cada caracter {caracter=}")
        # ~ if caracter.isupper():
            # ~ flag_may=True
        # ~ if caracter.islower():
            # ~ flag_min=True
        # ~ if caracter in simbolos:
            # ~ flag_sim=True
        # ~ if caracter.isdigit():
            # ~ flag_num=True
            
    # ~ if  flag_may is True and \
        # ~ flag_min is True and \
        # ~ flag_sim is True and \
        # ~ flag_num is True :
            # ~ return "correcto"
    # ~ else:
        # ~ return "in correcto"
    print ([(len (password)>=6) ,
            [True if caracter.isupper() else False for caracter in password] ,
            [True if caracter.islower() else False for caracter in password] ,
            [True if caracter.isdigit() else False for caracter in password] ,
            [True if caracter in simbolos else False for caracter in password]
            )#            [True if caracter.isascii() else False for caracter in password]]
    
    if all([(len (password)>=6) ,
        any([True if caracter.isupper() else False for caracter in password]) ,
        any([True if caracter.islower() else False for caracter in password]) ,
        any([True if caracter.isdigit() else False for caracter in password]) ,
        any([True if caracter in simbolos else False for caracter in password])]):
        return "correcto"
    else:
        return "in correcto"
regreso = ""
while regreso !="correcto":
    password = input("Ingrese su password:")
    regreso = funcion_validar_password(password)
    print (f"su password es {regreso}")

exit()







import re

while True:
    password = input("Ingresa tu contraseña: ")
    if len(password) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
    elif not re.search("[a-z]", password):
        print("La contraseña debe contener al menos una letra minúscula.")
    elif not re.search("[A-Z]", password):
        print("La contraseña debe contener al menos una letra mayúscula.")
    elif not re.search("[0-9]", password):
        print("La contraseña debe contener al menos un número.")
    elif not re.search("[_@$]", password):
        print("La contraseña debe contener al menos uno de los siguientes caracteres especiales: _@$")
    else:
        print("Contraseña válida")
        break


##solucion: 











simbolos =  ["!","@","#","$","%","^","*","/","+","-","_","(",")","{","}","[","]",":",";",",",".","<",">","?","\\","|","'","~","&","ç","Ç"] 
while True:
    usuario = input ("Ingrese un password debe tener minimo de 6 caracteres al menos una mayuscula, al menos una minuscula, al menos un simbolo de teclado y al menos un numero:")
    if len(usuario)<6:
        print("no cumple con 6 caracteres minimo")
    else:
        # ~ usuario =[*usuario.strip()]#.split()
        # ~ usuario = [char for char in usuario]# comprencion funciones en una linea
        # ~ print (usuario)
        print ("upper",any([True if char.isupper() else False for char in usuario ]))
        print ("lower",any([True if char.islower() else False for char in usuario ]))
        print ("numerico",any([True if char.isdecimal() else False for char in usuario ]))
        print ("simbolos", any([True if char in simbolos else False for char in usuario ]))
        if all( [any([True if char.isupper() else False for char in usuario ]),
                 any([True if char.islower() else False for char in usuario ]),
                 any([True if char.isdecimal() else False for char in usuario ]),
                 any([True if char in simbolos else False for char in usuario ])]) is True:
            print("Password aceptado")
            break
        else:
            print("No cumple con las condiciones")

exit()
