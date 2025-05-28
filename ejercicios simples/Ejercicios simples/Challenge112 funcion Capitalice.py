
'''
DESAFIO N~'16
 * EN MAYÚSCULA
 * Dificultad: FÁCIL
Complete el método o la función para que convierta las palabras delimitadas por guiones o guiones bajos en mayúsculas y minúsculas . 
    El primer caracter de la primera palabra dentro de la salida debe estar en mayúsculas solo si el original estaba en mayúsculas 
                (conocido como Upper Camel Case, también conocido como caso Pascal). 
    Las siguientes palabras deben estar siempre con el primer caracter en mayúscula.
Examples
"the-stealth-warrior" gets converted to "the Stealth Warrior"
"The_Stealth_Warrior" gets converted to "The Stealth Warrior"
'''





















exit()
def to_camel_case1(text):
    camel_caseText=''
    for index,caracter in enumerate(text):
        if index ==0 :
            camel_caseText +=caracter
        elif text[index-1]in ["-","_"]:
            camel_caseText +=caracter.upper()
        else:
            camel_caseText +=caracter.lower()
    return camel_caseText.replace("_"," ").replace("-"," ")
################################################################################################
def to_camel_case2(text):

    camel_caseText=       [  caracter       if index ==0  else caracter.upper() if text[index-1]in ["-","_"] else caracter.lower()  for index,caracter in enumerate(text)]
    # ~ print(camel_caseText)
    camel_caseText="".join(camel_caseText).replace("_"," ").replace("-"," ") 
    # ~ print(camel_caseText)
    return camel_caseText  
################################################################################################
def to_camel_case3(text):
    return text[:1] + text.title()[1:].replace('_', ' ').replace('-', ' ')
################################################################################################
import re
def to_camel_case4(text):
    return re.sub('[_-](.)',lambda c:c[1].upper(),text)
################################################################################################
def to_camel_case5(text):
    return "".join([i if n==0 else i.capitalize() for n,i in enumerate(text.replace("-","_").split("_"))])
################################################################################################
print ("*"*54)
print ("*","solución 1".center(50),"*")
print ("*"*54)
print(f'{to_camel_case1("the-stealth-warrior")=}')
print(f'{to_camel_case1("The_Stealth_Warrior")=}')
print ("*"*54)
print ("*","solución 2".center(50),"*")
print ("*"*54)

print(f'{to_camel_case2("the-stealth-warrior")=}')
print(f'{to_camel_case2("The_Stealth_Warrior")=}')
print ("*"*54)
print ("*","solución 3".center(50),"*")
print ("*"*54)

print(f'{to_camel_case3("the-stealth-warrior")=}')
print(f'{to_camel_case3("The_Stealth_Warrior")=}')
print ("*"*54)
print ("*","solución 4".center(50),"*")
print ("*"*54)

print(f'{to_camel_case2("the-stealth-warrior")=}')
print(f'{to_camel_case2("The_Stealth_Warrior")=}')
print ("*"*54)
print ("*","solución 5".center(50),"*")
print ("*"*54)

print(f'{to_camel_case3("the-stealth-warrior")=}')
print(f'{to_camel_case3("The_Stealth_Warrior")=}')


