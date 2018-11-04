''' Demonstrating recursion through Fibonacci and Lucas series.
    Includes 'custom' series to accept any seed numbers--with Fibonacci series as default. 
    Written by David K. Arasim, 10/15/18'''

#Functions section

def fibonacci(n):
#Fibonacci series with seed numbers 0 and 1
    if n <= 0:
        result = 0
    elif n == 1:
        result = 1
    elif n > 1:
        result = fibonacci(n-2) + fibonacci(n-1)
    return result

def lucas(n):
#Lucas series with seed numbers 2 and 1
    if n <= 0:
        result = 2
    elif n == 1:
        result = 1
    elif n > 1:
        result = lucas(n-2) + lucas(n-1)
    return result

def sum_series(n, n0=0, n1=1):
#Custom series with configurable seed numbers (0 and 1 by default)
    if n <= 0:
        result = n0
    elif n == 1:
        result = n1
    elif n > 1:
        result = sum_series(n-2, n0, n1) + sum_series(n-1, n0, n1)
    return result

##################################################################################	
#User interfaces for functions

#fibonacci()
print('Enter Fibonacci series number to compute: ', end='')
fib_num = int(input())
print('Fibonacci series number for ', fib_num, ' is: ', fibonacci(fib_num))

#lucas()
print('Enter Lucas series number to compute: ', end='')
luc_num = int(input())
print('Lucas series number for ', luc_num, ' is: ', lucas(luc_num))

#sum_series()
print('Enter Sum series number to compute: ', end='')
sum_num = int(input())
print('Enter first Sum series seed number (0 = default): ', end='')
seed1 = input()
try:
    seed1 = int(seed1)
except ValueError:
    seed1 = ''
print('Enter second Sum series seed number (1 = default): ', end='')
seed2 = input()
try:
    seed2 = int(seed2)
except ValueError:
    seed2 = ''
if (seed1 == '') or (seed2 == ''):
    print('Sum series number for ', sum_num, 'using default seed numbers 0 and 1 is: ', sum_series(sum_num))
else:
    print('Sum series number for ', sum_num, ' using seed numbers ', seed1, ' and ', seed2, ' is: ', sum_series(sum_num, seed1, seed2))

##################################################################################	

#Assertions for functions

if __name__ == '__main__':
    # run some tests
    #fibonacci()
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    #lucas()
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7

    #test if sum_series matched fibonacci
    assert sum_series(5) == fibonacci(5)

    #test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)
	
    print("tests passed")