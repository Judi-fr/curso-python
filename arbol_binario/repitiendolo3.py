class Nodo():
    def __init__(self,valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class arbol_binario():
    def __init__(self):
        self.raiz = None

    def insertar(self,valor):
        if self.raiz == None:
            self.raiz = Nodo(valor)
        else: self.insertar_recursividad(self.raiz,valor)

    def insertar_recursividad(self,nodo,valor):
        if valor < nodo.valor:
            if nodo.izquierdo == None:
                nodo.izquierdo = Nodo(valor)
            else:
                self.insertar_recursividad(nodo.izquierdo,valor)
        elif valor > nodo.valor:
            if nodo.derecho == None:
                nodo.derecho = Nodo(valor)
            else:
                self.insertar_recursividad(nodo.derecho,valor)
    
    def inorden(self):
        return self.inorden_recursivo(self.raiz)
    
    def inorden_recursivo(self,nodo):
        if nodo == None:
            return []
        return self.inorden_recursivo(nodo.izquierdo) + [nodo.valor] + self.inorden_recursivo(nodo.derecho)
    

arbol = arbol_binario()
numericos_tio = [9,7,5,2,1,4,6,8,9]

for v in numericos_tio:
    arbol.insertar(v)
print(arbol.inorden())