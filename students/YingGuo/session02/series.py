

def fibonacci(n):
    """The Fibonacci Series is a numeric series starting with the integers 0 and 1.
    In this series, the next integer is determined by summing the previous two. 
    This function is to write Fibonacci series. N is the length of series. N is an integer starting from 0"""
   
    list1 = list()

    for i in range(n+1):
        if i == 0:
            list1.append(0)
        elif i == 1:
            list1.append(1)
        else:
            x = list1[i-2]+list1[i-1]
            list1.append(x)
    
    return list1[n]


def lucas(n):
    """The Lucas Numbers is like fibonacci series but are start with the values 2 and 1 rather than 0 and 1.
    This function is to write a Lucas series with the length of n. N is integer starting from 0"""
    
    list2 = list()

    for i in range(n+1):
        if i == 0:
            list2.append(2)
        elif i == 1:
            list2.append(1)
        else:
            x = list2[i-2] + list2[i-1]
            list2.append(x)

    return list2[n]

def sum_series (n, a=0, b=1):
    """This function is a more generalized function to write series. N means length of series. A is the first number.
    B is the second number. The number after is the sum of the previous two numbers. the defaul value of a is 0. 
    the default value of b is 1"""

    list3 = list()

    for i in range(n+1):
        if i == 0:
            list3.append(a)
        elif i == 1:
            list3.append(b)
        else:
            x = list3[i-2] + list3[i-1]
            list3.append(x)

    return list3[n]


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
