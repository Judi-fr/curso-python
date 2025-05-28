# ~ from random import randint
# ~ def returnInputNumber(n):
    # ~ matrix1 = [0,0,0,0,0], [0,0,0,0,0]
    # ~ matrix2 = [0,0,0,0,0], [0,0,0,0,0]
    # ~ x, y = randint(0,4), randint(0,4)
    # ~ for i in range(5):
        # ~ matrix1[0][i] = randint(-100, 100)
        # ~ matrix1[1][i] = randint(-100, 100)
    # ~ matrix1[0][x] = n//2
    # ~ matrix1[1][y] = n-n//2
    # ~ for i in range(5):
        # ~ matrix2[0][i] = i-x
        # ~ matrix2[1][i] = i-y
    # ~ for i in matrix2[0]:
        # ~ if i == 0:
            # ~ if matrix2[0][0] == 0: q = 0
            # ~ if matrix2[0][1] == 0: q = 1
            # ~ if matrix2[0][2] == 0: q = 2
            # ~ if matrix2[0][3] == 0: q = 3
            # ~ if matrix2[0][4] == 0: q = 4
    # ~ for i in matrix2[1]:
        # ~ if i == 0:
            # ~ if matrix2[1][0] == 0: w = 0
            # ~ if matrix2[1][1] == 0: w = 1
            # ~ if matrix2[1][2] == 0: w = 2
            # ~ if matrix2[1][3] == 0: w = 3
            # ~ if matrix2[1][4] == 0: w = 4
    # ~ number = matrix1[0][q]+matrix1[1][w]
    # ~ print(feel_lonely)
    # ~ return number if number == n else None
    
'''
Complete the function that accepts a valid string and returns an integer.

Wait, that would be too easy! Every character of the string should be converted to the hex value of its ascii code, then the result should be the sum of the numbers in the hex strings (ignore letters).

Examples
"Yo" ==> "59 6f" ==> 5 + 9 + 6 = 20
"Hello, World!"  ==> 91
"Forty4Three"    ==> 113
'''

y=[]
text="Forty4Three"
text="Yo"
for c in text:

    x= [int(z) for z in hex(ord(c)) if z.isdecimal()]
    print(x )
    y.append(sum(x))
    print( y)
print (sum(y))
text="Yo"



for c in text:

    x=[ sum([int(z) for z in hex(ord(c)) if z.isdecimal()])]
    print(f"{x=}" )
    y.append(sum(x))
    print(f"{y=}" )
print (sum(y))


text="Forty4Three"





x=[ sum([int(z) for z in hex(ord(c)) if z.isdecimal()]) for c in text ]
print(f"{sum(x)=}" )







exit()





# ~ y= [z  for z in str(hex(ord(c))) for c in text if z.isdecimal()]
# ~ print (y)
x=[]
for c in text:
    for z in str(hex(ord(c)))  :
       if z.isdecimal():
           x.append(z)  

print (x)
text="Yo"
x=[  y       for y in str(hex(ord(z))) for z  in text]
  

print (x)



