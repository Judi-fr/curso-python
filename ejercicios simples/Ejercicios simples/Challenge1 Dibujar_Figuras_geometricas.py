
cant =""
while cant.isnumeric() is False:
    cant = input ("ingrese el largo del cuadrado en caracteres:")# todo input devuelve un string
cant = int(cant)# un objeto str pasa a se int = casting

limite_inf_sup = f"+{'-'*(cant-2)}+"

print (limite_inf_sup.center(cant*2))
for x in range (0,cant-2):
    print ( f"|{' '*(cant-2)}|".center(cant*2))
print (limite_inf_sup.center(cant*2))
#-------------------------------------------------------------------------
print ("*"*100)
if cant%2!=0:
    cant=cant+1

for x in range (0,int(cant)):
    print (f"/{' '*(x*2)}\\".center(cant*2))
limite_inf_sup = f"{'-'*(cant*2)}"
print (limite_inf_sup.center(cant*2))
#-------------------------------------------------------------------------
print ("*"*100)
if cant%2!=0:
    cant=cant+1

for x in range (0,int(cant/2)):
    print (f"/{' '*(x*2)}\\".center(cant*2))

for x in range (int((cant-1)/2),-1,-1):
    print (f"\\{' '*(x*2)}/".center(cant*2))


#-------------------------------------------------------------------------
print ("*"*100)








