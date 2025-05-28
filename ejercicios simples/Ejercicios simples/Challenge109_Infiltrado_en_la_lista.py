print(f'''
● Ejercicio : dada un vector de n datos n donde todos excepto uno es diferente. Detectar cuan es el diferente
''')
def Solucion():
    pass
    
    
# ~ def find_uniq(arr):
    # ~ par=list(set(arr))
    # ~ if arr.count(par[0])==1:
        # ~ arr = par[0]
    # ~ else:
        # ~ arr = par[1]
    # ~ return arr
def find_uniq(arr):
    return [x for x in set(arr) if arr.count(x) == 1][0]
print(find_uniq([ 1, 1, 1, 2, 1, 1 ])) #== 2
print(find_uniq([ 0, 0, 0.55, 0, 0 ]) )#== 0.55
print(find_uniq([ 8, 0, 0, 0, 0 ]) )#== 0.55
print(find_uniq([ "0","0","0","0","0","0","0","O","0"])) #== 2
