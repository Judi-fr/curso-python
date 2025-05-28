print(f'''
● Escriba una función para encontrar la cadena de prefijo común más larga entre una matriz de cadenas.

Si no hay un prefijo común, devuelve una cadena vacía "".
''')
 
'''
Ejemplo 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
'''

class Solution:
    def prefijo_comun_mayor(self, strs: list[str]) -> str:
        ultima_cant=0
        cant =len(strs[0])+1
        char = 0
        for word in strs[1:]:
            print("word[0]",strs[0],"//    word",word)
            print("-------------------")
            for char in range(1,len(strs[0])+1) :
                
                print  ('word[:char]',word[:char])
                print ('char',char,'cant',cant)
                
                print  (word.startswith(strs[0][:char]))
                if not word.startswith(strs[0][:char]) or char>=cant:
                    print ("break")
                    break

            cant=char
        return strs[0][:cant-1]




strs = ["flow","flowight","flower"]
strs = ["abcde2222222222","aabcde233flow","cabcde1"]
strs = ["abcd2","abcd1+1","abcde2"]
# ~ strs = ["aa","a"]
x=Solution()
char=x.prefijo_comun_mayor(strs)
print("/////////////////////////")

print (char) 







def prefijo_comun_mayor(strs: list[str]) -> str:
    cant =len(strs[0])
    char = 0
    for word in strs[1:]:
        # ~ print(word)
        for char in range(len(strs[0])+1) :
            if not word.startswith(strs[0][:char]) or char>=cant:
                break
        cant=char-1
    return strs[0][:cant]




strs = ["flower","flow","flight"]
# ~ strs = ["abcde2222222222","aabcde233flow","cabcde1"]
# ~ strs = ["aa","a"]

char = prefijo_comun_mayor(strs)

print (char) 


