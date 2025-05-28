'''
validar un password:
    debe tener minimo de 6 caracteres
    al menos una mayuscula,
    al menos una minuscula,
    al menos un simbolo de teclado y
    al menos un numero
'''
print( [x**2   for x in range(1, 11)                if x % 2 == 0 ] )
print( [x**2   if  x % 2 == 0  else  x+1    for x in range(1, 11) ]  )
exit()
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
