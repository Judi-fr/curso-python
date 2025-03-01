# Operadores lógicos

# and, or y not

# AND: Ambas condiciones deben ser verdaderas para que la expresión sea verdadera
estoy_vivo = True
doy_clases = True
print(estoy_vivo and doy_clases)
if estoy_vivo and doy_clases:
    print("Estoy vivo y doy clases")
else:
    print("No estoy vivo o no doy clases")

# OR: Al menos una condición debe ser verdadera para que la expresión sea verdadera
cliente_1_trabaja = False
cliente_2_trabaja = True
print("¿Debo prestar dinero a algún cliente?")
print(cliente_1_trabaja or cliente_2_trabaja)
if cliente_1_trabaja or cliente_2_trabaja:
    print("Sí, prestar dinero")
else:
    print("No, no prestar dinero")

# NOT: Invierte el valor de la condición
print("¿Estoy en casa?")
estoy_en_casa = True
if not estoy_en_casa:
    print("No, no estoy en casa")
else:
    print("Sí, estoy en casa")

if estoy_en_casa:
    print("Sí, estoy en casa")
else:
    print("No, no estoy en casa")
