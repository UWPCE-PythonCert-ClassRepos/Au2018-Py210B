import unittest
from decimal import Decimal

#!/usr/bin/env python3
#Week3 Excercise string formating
#Student: Brandon Nguyen - Au2018

#task 1 and 2

def strTask12():
    strT=( 2, 123.4567, 10000, 12345.67)
    #formt to produce 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    print("\'file_00{}:   {:.2f}, {:.2e}, {:.2e}\'".format(strT[0],strT[1],Decimal(strT[2]),Decimal(strT[3]))) #replace return/print to test

#Task3 - Dynamically Building up format strings.  
def formatter(in_tuple):
    strFrm = "This is {:d}: {:d}"
    #dynamically rebuild the strformat
    for i in range(len(in_tuple)-1):
        strFrm=strFrm+",{:d}"
    return strFrm.format(len(in_tuple),*in_tuple)
#Task4  I feel like I already did that in task 1-2.  but ok.
stp = ( 4, 30, 2017, 2, 27)
#to print out '02 27 2017 04 30'
print("\'{:02d} {:d} {:d} {:02d} {:}".format(stp[3],stp[4],stp[2],stp[0],stp[1]))

print()
#Task 5all about 5 f-string:
def strTask5a():
    lst = ['oranges', 1.3, 'lemons', 1.1]
    #display The weight of an orange is 1.3 and the weight of a lemon is 1.1
    text = f'The weight of an {(lst[0]).replace("s","")} is {lst[1]} and the weight of a {(lst[2]).replace("s","")} is {lst[3]}'
    return text

def strTask5b():
    lst = ['oranges', 1.3, 'lemons', 1.1]
    #display The weight of an orange is 1.3 and the weight of a lemon is 1.1
    text = f'The weight of an { ((lst[0]).replace("s","")).upper()} is {(lst[1]*1.2)} and the weight of a {((lst[2]).replace("s","")).upper()} is {(lst[3]*1.2)}'
    return text
#unit test
#turn in and TODO task6 after.

if __name__ == '__main__':
    #turn the function to return and compare
    #assert strTask12() == 'file_002:   123.46, 1.00e+4, 1.23e+4'
    stp=(2,3,4,5)
    assert formatter(stp) == 'This is 4: 2,3,4,5'
    assert strTask5a() == 'The weight of an orange is 1.3 and the weight of a lemon is 1.1'
    assert strTask5b() == 'The weight of an ORANGE is 1.56 and the weight of a LEMON is 1.32'
    print("Assertions are good")