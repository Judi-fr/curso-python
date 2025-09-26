class Nodo():
    def __init__(self,valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario():
    
    def __init__(self):
        self.raiz = None
    
    def insertar(self,valor):
        if self.raiz == None:
            self.raiz = Nodo(valor)
        else: self.insertar_recursiva(self.raiz,valor)

    def insertar_recursiva(self,nodo,valor):
        if valor < nodo.valor:
            if nodo.izquierda == None:
                nodo.izquierda = Nodo(valor)
            else:
                self.insertar_recursiva(nodo.izquierda,valor)
        elif valor > nodo.valor:
            if nodo.derecha == None:
                nodo.derecha = Nodo(valor)
            else:
                self.insertar_recursiva(nodo.derecha,valor)
    
    def inorden(self):
        return self.inorden_recursivo(self.raiz)
    
    def inorden_recursivo(self, nodo):
        if nodo == None:
            return []
        return self.inorden_recursivo(nodo.izquierda) + [nodo.valor] + self.inorden_recursivo(nodo.derecha)
    

arbol = ArbolBinario()
numeros = [8,9,6,7,5,4,3,2,1,]
for v in numeros:
    arbol.insertar(v)
print(arbol.inorden())