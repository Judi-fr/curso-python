print('''
● Reto : 
        dados 3 valors a,b y c devolver el area del triangulo mediante las siguientes ecuaciones:
            Formula Heron:  (s*(s−a)*(s−b)*(s−c))**(1/2)
            donde s=(a+b+c)/2
entrada:              salida:
        heron(3, 4, 5) > > > 6
​''')
 
def solucion():
    pass
    
def heron(a, b, c):
    s = (a + b + c) / 2
    return round((s * (s - a) * (s - b) * (s - c)) ** 0.5, 2)
heron=lambda a,b,c:round(((s:=(a+b+c)/2)*(s-a)*(s-b)*(s-c))**.5,2)
print(f"{heron(3, 4, 5)=}")
