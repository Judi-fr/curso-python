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

col =[ 
        [ 0,4,9,3,"pepe"],
        [ 7,6,5,4,"Ana"],
        [ 6,6,"hola",6,"Bea"],
        [ 1,2,3,4,"Rich"]
    ]

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

{col[2][2]=}
{type(col[2][2])=}
{id(col[2][2])=}


{col[3]=}
{type(col[3])=}
{id(col[3])=}


""")