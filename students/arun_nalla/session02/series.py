#!use/bin/env python
def fibo(n):
    '''Write a alternative code to get the nth value of the fibonacci series using type (list)
    0th and 1st position should return 0 and 1 and indexing nth position should
    return SUM of previous two numbers'''
    if n ==0: return 0
    elif n ==1: return 1
    my_list = [0,1]
    for x in range(2,n+1):
        y = my_list[-2] + my_list[-1]
        my_list.append(y)
    return my_list[-1]
print (fibo (5))
print (fibo (10))
print ('Done with fibonacci series')
def lucas(n):
    '''a code to get the nth value of the Lucas series using type (list)
        indexing the 0th and 1st position should return 2 and 1,respectively and indexing nth position should
        return SUM of previous two numbers'''
    if n ==0: return 2
    elif n ==1: return 1
    my_list2 = [2,1]
    for x in range(2,n+1):
        y = my_list2[-2] + my_list2[-1]
        my_list2.append(y)
    return my_list2[-1]
print (lucas (5))
print (lucas(10))
print ('Done with lucas series')

def sum_series(n, a=0, b=1):

    list_sum_series = [a,b]
    if n ==0: return a
    elif n ==1: return b
    for x in range (2,n+1):
        y = list_sum_series[-2] + list_sum_series[-1]
        list_sum_series.append(y)
    return list_sum_series[-1]


print (sum_series (10))
print (sum_series(10,2))
print (sum_series(10,2,1))
print (sum_series(10,1))
print (sum_series(10,3,5))
print ('Next is assertion statements')

if __name__ == "__main__":
    # run some tests
    assert fibo(0) == 0
    assert fibo(1) == 1
    assert fibo(2) == 1
    assert fibo(3) == 2
    assert fibo(4) == 3
    assert fibo(5) == 5
    assert fibo(6) == 8
    assert fibo(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7

    assert sum_series(5) == fibo(5)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    print("tests passed")




