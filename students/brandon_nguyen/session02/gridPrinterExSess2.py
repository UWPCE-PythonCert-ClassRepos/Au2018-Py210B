#!/usr/bin/env python3
#Grid Printer Excercise in session02 Au2018-Py210B
plus    = '+'
minusSp   = '- '
bar     = '|'
sP  = ' '
n = 11
m = 9
spCnt = int(round((n-3)/2))
#row line
print(plus, end=' ')
print(minusSp*spCnt+plus,end=' ')
print(minusSp*spCnt+plus)

#Col lines
print(bar+sP*m+bar+sP*m+bar)
print(bar+sP*m+bar+sP*m+bar)
print(bar+sP*m+bar+sP*m+bar)
print(bar+sP*m+bar+sP*m+bar)


#row line middle
print(plus, end=' ')
print(minusSp*spCnt+plus,end=' ')
print(minusSp*spCnt+plus)

#col end
print(bar+sP*m+bar+sP*m+bar)
print(bar+sP*m+bar+sP*m+bar)
print(bar+sP*m+bar+sP*m+bar)
print(bar+sP*m+bar+sP*m+bar)

#last row
print(plus, end=' ')
print(minusSp*spCnt+plus,end=' ')
print(minusSp*spCnt+plus)


def print_grid(n):
    """
    This fucntion takes a value input and prints out 4 squares grid.
    :param n : any n that is lower and equal to 3 will print out the exact grid size.

    """
    plus    = '+'
    minusSp   = '- '
    bar     = '|'
    sP  = ' '
    #controling the odd and even value of n
    if n%2==1:
        spCnt = int(round((n-2)/2))
    else:
        spCnt = int(round((n-1)/2))
    #controling smallest n anything 3 or less 
    if spCnt >= 1:
        spCnt=spCnt
    else:
        spCnt = 1
    for i in range(1,3):
        print(plus, end=' ')
        print(minusSp*spCnt+plus,end=' ')
        print(minusSp*spCnt+plus)
        for j in range(0,spCnt):
            print(bar+sP*(spCnt*2+1)+bar+sP*(spCnt*2+1)+bar)
    print(plus, end=' ')
    print(minusSp*spCnt+plus,end=' ')
    print(minusSp*spCnt+plus)        

def print_grid2(n,m):
    """
    This function will print out grid based on input n,m.
    :param n will be used to compute col spaces and -
    :param m will be used to compute row bars

    """
    plus    = '+'
    minusSp   = '- '
    bar     = '|'
    sP  = ' '
    #controling the odd and even value of n
    spCnt = m
    #print(plus + ' ', end=' ')
    '''
    #print bars in loops
    for i in range(0,m):
        print(bar,end=' ')
        for j in range(0,n):
            print(sP*(spCnt*2)+bar,end=' ')
        print()
    '''

     #brute force -- not good a way to code it.
    for i in range(0,n):
        print(plus, end=' ') 
        print(minusSp*spCnt+plus,end=' ')
        for j in range(1,n):
            print(minusSp*spCnt+plus,end=' ')
        print()
        for k in range(0,m):
            print(bar,end=' ')
            for l in range(0,n):
                print(sP*(spCnt*2)+bar,end=' ')
            print()
    #print the last line with         
    for i in range(0,1):
        print(plus, end=' ') 
        print(minusSp*spCnt+plus,end=' ')
        for j in range(1,n):
            print(minusSp*spCnt+plus,end=' ')
