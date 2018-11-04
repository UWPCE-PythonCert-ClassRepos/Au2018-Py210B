# Fibonacci Function
def fibonacci(n):
    """Returns the nth value in the fibonacci series (starting with zero)"""
    if n<2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

fib_result = fibonacci(8) # Input
print(fib_result)

# Lucas Function
def lucas(n):
    """Returns the nth value in the lucas series (starting with zero)"""
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)

luc_result = lucas(8) # Input
print(luc_result)

# Sum Series
def sum_series(n, val01=0, val02=1):
    """Returns the nth value in a custom series (starting with zero)"""
    if n==0:
        return val01
    elif n==1:
        return val02
    else:
        return sum_series(n-1,val01,val02)+sum_series(n-2,val01,val02)

ss_result = sum_series(8,2,1) # Input
print(ss_result)


if __name__ == "__main__":
    # run some tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7

    assert sum_series(5) == fibonacci(5)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    print("tests passed")