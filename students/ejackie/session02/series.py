#!/usr/bin/env python3

"""
a template for the series assignment
"""


def fibonacci(n):
    """ compute the nth Fibonacci number """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)


def lucas(n):
    """ compute the nth Lucas number """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)


def sum_series(n, n0=0, n1=1):
    """
    compute the nth value of a summation series.

    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series

    if n0 == 0 and n1 == 1, the result is the Fibbonacci series

    if n0 == 2 and n1 == 1, the result is the Lucas series
    """
    if n0 == 0 and n1 == 1:
        return fibonacci(n)
    if n0 == 2 and n1 == 1:
        return lucas(n)


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
