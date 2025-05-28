import os
from colorama import *
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')

def pausa():
    input("\tPresione enter para continuar")
limpiar();
#################################################################
def Ej_ya_hechos():
    # Con tab colocaremos aqui las practicas hechas
    pass


limpiar()
print(
    """\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║    ╔══════╗    ╦       ╦   ╔═══╦═══╗   ╦       ╦    ╔═════╗    ╔╗      ╦    ║
║    ║      ╚╗   ╚╗     ╔╝       ║       ║       ║   ╔╝     ╚╗   ║╚╗     ║    ║
║    ║       ║    ╚╗   ╔╝        ║       ║       ║   ║       ║   ║ ╚╗    ║    ║
║    ║      ╔╝     ╚╗ ╔╝         ║       ║       ║   ║       ║   ║  ╚╗   ║    ║
║    ╠══════╝       ╚╦╝          ║       ╠═══════╣   ║       ║   ║   ╚╗  ║    ║
║    ║               ║           ║       ║       ║   ║       ║   ║    ╚╗ ║    ║
║    ║               ║           ║       ║       ║   ╚╗     ╔╝   ║     ╚╗║    ║
║    ╩               ╩           ╩       ╩       ╩    ╚═════╝    ╩      ╚╝    ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║      Unidad 2 - Variables, Listas                                           ║
║            * Tipos de variables                                             ║
║            * Procesamiento de cadenas                                       ║
║                                                                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
"""
)

pausa()
limpiar()

obj = 8

print (f"""
{obj=}
{type(obj)=}
{id(obj)=}
{dir(obj)=}
""")
'''
obj=8
type(obj)=<class 'int'>
id(obj)=140722976588936
dir(obj)=['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 

'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
'''


#########################################################################
obj = 9.5

print (f"""
{obj=}
{type(obj)=}
{id(obj)=}
{dir(obj)=}
""")
'''
obj=9.5
type(obj)=<class 'float'>
id(obj)=2401622143984
dir(obj)=['__abs__', '__add__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 

'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
'''

#########################################################################
obj = "HOLA MUNDO IT"

print (f"""
{obj=}
{type(obj)=}
{id(obj)=}
{dir(obj)=}
""")
'''
obj='HOLA MUNDO IT'
type(obj)=<class 'str'>
id(obj)=2401625446960
dir(obj)=['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 

'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
'''













"""
int var ;
var = 1234;

float var ;
var = 12.34;


char var [5];
var = "12.34";
"""

obj = 1234
print (f"""
{obj=}
{type(obj)=}
{dir (obj)=}
""")
"""
dir (obj)=['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 

'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']

"""


print (f"{obj**2=}")

print ("*"*50)##########################################################
obj = 12.34
print (f"""
{obj=}
{type(obj)=}
{dir (obj)=}
""")
"""
dir (obj)=['__abs__', '__add__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 

'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
"""
print (f"{obj**2=}")

print ("*"*50)##########################################################




obj = "1234"
print (f"""
{obj=}
{type(obj)=}
{dir (obj)=}
""")
"""
dir (obj)=['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 

'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

"""
# ~ print (f"{obj**2=}")

漅滽滶漹漜滼 = "漅"
print (f"{漅滽滶漹漜滼}")

if 漅滽滶漹漜滼 == "漅":
    print ("ok")
print ("*"*50)##########################################################

obj = (1,2)
print (f"""
{obj=}
{type(obj)=}
{dir (obj)=}
""")

"""
obj=(1, 2)
type(obj)=<class 'tuple'>
dir (obj)=['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
"""

print ("*"*50)##########################################################
obj = [1,2]
print (f"""
{obj=}
{type(obj)=}
{dir (obj)=}
""")
"""
obj=[1, 2]
type(obj)=<class 'list'>
dir (obj)=['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

"""

print ("*"*50)##########################################################

obj = {1,2}
print (f"""
{obj=}
{type(obj)=}
{dir (obj)=}
""")
"""
obj={1, 2}
type(obj)=<class 'set'>
dir (obj)=['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
"""

print ("*"*50)##########################################################

obj = {1:"hola",2:"chau"}
print (f"""
{obj=}
{type(obj)=}
{dir (obj)=}
""")
"""
obj={1: 'hola', 2: 'chau'}
type(obj)=<class 'dict'>
dir (obj)=['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
"""

obj = 8
print (f"""
{obj=}
{type(obj)=}
{id(obj)=}
""")

obj = 2
print (f"""
{obj=}
{type(obj)=}
{id(obj)=}
""")

obj = "pepe"
print (f"""
{obj=}
{type(obj)=}
{id(obj)=}
""")


col =[ 0,4,9,3,"pepe"]
print (f"""
{col=}
{type(col)=}
{id(col)=}
--------------------
{col[0]=}
{type(col[0])=}
{id(col[0])=}

{col[1]=}
{type(col[1])=}
{id(col[1])=}

{col[2]=}
{type(col[2])=}
{id(col[2])=}

{col[3]=}
{type(col[3])=}
{id(col[3])=}

{col[4]=}
{type(col[4])=}
{id(col[4])=}


""")

#################################################################

#################################################################




obj = "hola MuNdO It"
print (f"""
{obj=}
{type(obj)=}
""")
"""
dir (obj)=['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 

'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""



print ("*"*50)
print ("*","METODOS DE ESTILO".center(46),"*")
print ("*"*50)
m=['capitalize', 'casefold',  'lower', 'swapcase', 'title', 'upper']

print (f"""
{obj.upper()=}
{type(obj.upper())=}
""")
print (f"""
{obj.lower()=}
{type(obj.lower())=}
""")
print (f"""
{obj.capitalize()=}
{type(obj.capitalize())=}
""")
obj = obj.upper()

#########################################################################
print ("*"*50)
print ("*","METODOS DE PLACE".center(46),"*")
print ("*"*50)
m='center',"ljust","rjust"


print (f"""
{obj.rjust(50)=}
{type(obj.rjust(50))=}
""")
print (f"""
{obj.ljust(50)=}
{type(obj.ljust(50))=}
""")
print (f"""
{obj.center(50)=}
{type(obj.center(50))=}
""")
#########################################################################
print (f"""
{obj.center(50).upper()=}
{type(obj.center(50).upper())=}
""")
print (f"""
{obj.upper().center(50)=}
{type(obj.upper().center(50))=}
""")
print (f"""
{obj.lower().upper()=}
{type(obj.lower().upper())=}
""")

#########################################################################







print ("*"*50)
print ("*","METODOS DE BOOLEANO".center(46),"*")
print ("*"*50)


m= ['isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper','startswith', 'endswith']





obj = "123456"

print (f"{obj=}")
print (f"{obj.center(50)=}")
print (f"{obj.upper()=}")
print (f"{obj.isalnum()=}")
print (f"{obj.isalpha()=}")
print (f"{obj.isdecimal()=}")
print (f"{obj.isdigit()=}")
print (f"{obj.isnumeric()=}")


#########################################################################
print ("*"*50)
print ("*","METODOS DE REPLACE".center(46),"*")
print ("*"*50)
m='replace'



obj = "123.4056"

print (f"{obj=}")
print (f"{obj.center(50)=}")
print (f"{obj.upper()=}")
print (f"{obj.isalnum()=}")
print (f"{obj.isalpha()=}")
print (f"{obj.isdecimal()=}")
print (f"{obj.isdigit()=}")
print (f"{obj.isnumeric()=}")

print (f"{obj.replace('.','',1).isdecimal()=}")
print (f"{obj.replace('.','',1).isdigit()=}")
print (f"{obj.replace('.','',1).isnumeric()=}")
#################################################################



obj = "12,34"
if obj.isdigit() is True:
    print (f"""
                        casting a int
    {obj=}
        {type(obj)=}
        {id(obj)=}
        {dir(obj)=}
    """)
    obj= int(obj)

elif obj.replace(".","",1).isdigit() is True:
    print (f"""
                        casting a float
    {obj=}
        {type(obj)=}
        {id(obj)=}
        {dir(obj)=}
    """)
    obj= float(obj)
elif obj.replace(",",".",1).replace(".","",1).isdigit() is True:
    print (f"""
                        casting a float con error habia coma, no punto
    {obj=}
        {type(obj)=}
        {id(obj)=}
        {dir(obj)=}
    """)
    obj = obj.replace(",",".")
    obj = float(obj)

else:
    
    
    print (f"""
                        no puedo hacer el casting
    {obj=}""")


print (f"""

                        salida 
{obj=}
    {type(obj)=}
    {id(obj)=}
    {dir(obj)=}
""")














exit()

print ("*"*50)
print ("*","OTROS METODOS".center(46),"*")
print ("*"*50)
m =  ['count', 'encode',  'expandtabs', 'find', 'format', 'format_map', 'index', 'join', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', '', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'strip', 'translate',  'zfill']




exit()
#################################################################
# Clase_Variables_04
print(
    """\033[1;37;44m\n
╔══════════════════════════╦══════════════════════════╦══════════════════════════╗
║                          ║                          ║                          ║
║    + Suma                ║         a += b           ║           a = a + b      ║
║    - Resta               ║         a -= b           ║           a = a - b      ║
║    * Multiplicación      ║         a *= b           ║           a = a * b      ║
║    ** Exponente          ║         a **= b          ║           a = a ** b     ║
║    / División            ║         a /= b           ║           a = a / b      ║
║    // División entera    ║         a //= b          ║           a = a // b     ║
║    % Módulo              ║         a %= b           ║           a = a % b      ║
║                          ║                          ║                          ║
╚══════════════════════════╩══════════════════════════╩══════════════════════════╝\033[0;m
"""
)
# Precedencia (jerarquía) de operadores:

from math import sqrt

resultado = 5 / 2 + 4
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

resultado = 4 + 5 / 2
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

resultado = 5 / (2 + 4)
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

resultado = 5 / (2 + 4) + sqrt(25)
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

resultado = 25 ** 1 / 2
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

resultado = 25 ** (1 / 2)
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

resultado = (13 + 3) ** (1 / 2)
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = sum(numeros[0:5])
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

numero = -100

resultado = -(100 ** (1 / 2))
print("El contenido de la variable `resultado` es:", resultado)

pausa()
#################################################################

resultado = -(numero ** (1 / 2))
print("El contenido de la variable `resultado` es:", resultado)
print("Tipo de dato de la variable `resultado`:", type(resultado).__name__)

pausa()
#################################################################

resultado = (-numero) ** (1 / 2)
print("El contenido de la variable `resultado` es:", resultado)
print("Tipo de dato de la variable `resultado`:", type(resultado).__name__)

#################################################################
a = 1
b = 2
c = 3
d = 16
resultado = a / (b * c) / d ** (1 / 2) ** 3
print("Resultado:", resultado)
pausa()
#################################################################
e = 7
resultado = (a ** 3) ** 2 - b * c / (d * e)
print("Resultado:", resultado)
#################################################################
numero = int(input("Ingrese un numero: "))
if numero >= 0:
    factorial = 1

    if numero == 0 or numero == 1:
        factorial = 1
    else:
        for i in range(1, numero + 1):
            factorial *= i

    print(f"{numero}! = {factorial}")
else:
    print(
        "MENSAJE: Ha escrito un valor negativo. La función factorial no está definida para los números negativos."
    )
#################################################################