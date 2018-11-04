def fibonacci(n):
    """Return the nth value in the fibonacci series starting with 0 index"""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """Return the nth value in the Lucas numbers series starting with 0 index"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, n0=0, n1=1):
    """Return the nth value in a series with arbitrary 0th and 1st elements

    Keyword Arguments:
    n0=0: value of the zeroth element in the series
    n1=1: value of the first element in the series"""
    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sum_series(n-1, n0=n0, n1=n1) + sum_series(n-2, n0=n0, n1=n1)


if __name__ == "__main__":
    # Test fibonacci function
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    # Test lucas function
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7

    # Test if sum series matches fibonacci with default params
    assert sum_series(5) == fibonacci(5)

    # test if sum_series matched lucas with appropriate params
    assert sum_series(5, 2, 1) == lucas(5)
    print("tests passed")
