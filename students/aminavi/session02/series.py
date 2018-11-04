def fibonacci(n):
    """fibonacci starting  with 0 and 1"""
    a,b = 0,1
    for i in range(n):
        a,b = b, a+b
    return a

#fibonacci(5)

#

def lucas(n):
    """fibonacci starting  with 2 and 1"""
    a,b = 2,1
    for i in range(n):
        a,b = b, a+b
    return a

#lucas(5)

#

def sum_series(n , min_rang=0 , fo_rang=1):
    """sum_series starting  with defualt 0 and 1 but they are optional"""
    a,b = min_rang, fo_rang
    for i in range(n):
        a,b = b, a+b
    return a

#sum_series(5, 2, 1)

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

