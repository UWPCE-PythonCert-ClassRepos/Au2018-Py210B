a = (('+ '+('- '*4))*2+'+')
b = ('| '+' '*8)*2+'|'

print (a) ; print(b); print(b); print(b); print(b) ; print(a)
print(b); print(b); print(b); print(b) ; print(a)


def grid(n):
    x = (('| '+'  '*(n//2))*2+'|')
    y = (('+ '+'- '*(n//2))*2+'+')
    if n%2==0 or n<2:
        print ('Value of n should be an odd number and greater than 2')
    else:
        for a in range(n+2):
            if a==0 or a==(n+1)//2 or a==n+1:
                print (y)
            elif a!=0 and a!= (n+1)//2:
                print (x)
        
def grid2(n1,n2):
    x = ('| '+'  '*(n2))*n1+'|'
    y = ('+ '+'- '*(n2))*n1+'+'
    v =[y if a==0 else x for a in range(n2+1)]
    for v1 in v*n1:
        print (v1)
    print (y)
    
    
grid(1)
print ("one")
grid(2)
print ("Two")
grid(3)
print ("Three")
grid(4)
print ("four")
grid (11)
print ("Eleven")
grid(15)
print ("Fiveteen")
grid2(3,4)
print ("Three and Four")
grid2(5,3)
print ("Five and Three")
print ("DONE")


