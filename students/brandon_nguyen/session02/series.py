
#!/usr/bin/env python3
import unittest
#Week2 Excercise #2
#Student: Brandon Nguyen - Au2018
def fibonacci(n):
    """
    The function have one parameter n which represents the index.
    The function returns the nth's value of the index n in fibonacci series (starting with zero indiex).
    0, 1, 1, 2, 3, 5, 8, 13, ...
    """
    if (n==0 or n==1): 
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def lucas(n):
    """
    The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1. 
    The resulting series looks like this:2, 1, 3, 4, 7, 11, 18, 29, ... similiar to f(n)=f(n-1)+f(n-2)
    The function lucas returns the nth value in the lucas numbers series (starting with zero index).
    """
    if (n==0 or n == 1):
        return abs(n-2)
    else:
        return lucas(n-1) + lucas(n-2)
def sum_series(n,n0=0,n1=1):   
    """
    compute the nth value for fibonacci or lucas serie. 
    :param optional or default to n0=0, n1=1 determine the first two values in the series. 

    if n0 == 0 and n1 == 1 do Fibbonacci 
    if n0 == 2 and n1 == 1 do lucas
    elif do other 

    """
    #ask the instructor which is the best way to check args.
    '''
    if (n0==0 and n1==1):
    #do fibonacci
        if (n==0 or n==1): 
            return n
        else:
            return fibbonacci(n-1) + fibbonacci(n-2)
    elif(n0==2 and n1==1):
    #do lucas    
        if (n==0 or n == 1):
            return abs(n-2)
        else:
            return lucas(n-1) + lucas(n-2)
    else:
        print("TODO - Other Series sum to do")

    '''
    #correction after reviewed by instructor
    if n==0:
        return n0
    elif n==1:
        return n1
    elif n >=2:
        return sum_series(n-1,n0=n0,n1=n1) + sum_series(n-2,n0=n0,n1=n1)




#unit test using assert do ask about assertEqual as I am unable to make use of it
if __name__ == "__main__":
    #rename functions to save typing
    f = fibonacci
    l = lucas
    s = sum_series

    assert f(0) == 0
    assert f(1) == 1
    assert f(2) == 1
    assert f(3) == 2
    assert f(4) == 3
    assert f(5) == 5
    assert f(6) == 8
    assert f(7) == 13

    assert l(0) == 2
    assert l(1) == 1

    assert l(4) == 7

    assert s(5) == f(5)

    # test if sum_series matched lucas
    assert s(5, 2, 1) == l(5)

    #some control test of not equal
    assert s(5,2,1) != l(6)
    assert s(5,2,1) != f(6)

    print(" all tests passed including not equal")
#rename functions

  




