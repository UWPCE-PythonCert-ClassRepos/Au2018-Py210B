#!/usr/bin/env python3
import unittest

#slicing lab in lession 3
#Student Brandon Nguyen

"""
Exchange first and last sequence.
"""
def exchange_first_last(seq):
    return seq[-1:]+seq[1:len(seq)-1]+seq[0:1]

"""
Return every other item removed
"""
def return_every_other(seq):
    return seq[::2]

"""
Return a sequence with the first 4 removed, last 4 and every
"""
def first4last4_rm_rtn_everyother(seq):
    return seq[4:-4:2]

"""
Return a sequence with elements in reversed just with slicing.
"""
def reversed_with_slicing(seq):
    return seq[::-1]


"""
Unit test
"""
if __name__ == '__main__':
    #unittest.main()
    #rename long name

    e = exchange_first_last
    rtn = return_every_other
    f = first4last4_rm_rtn_everyother
    rev= reversed_with_slicing

    a_string='this is a string'
    a_tuble=(11,22,33,44,55,66,77)
    a_list=[11,22,33,44,55,66,77,88]

    seqStr='this is a longer string to test'
    seqList=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    seqTuble=(1,2,3,4,5,6,7,8,9,10,11,12,13,14)

    #TDD do the test cases first
    #test exchange
    assert e(a_string) == "ghis is a strint"
    assert e(a_tuble)  == (77,22,33,44,55,66,11)
    assert e(a_list)   == [88,22,33,44,55,66,77,11]

    #first4last4_rm_rtn_everyother
    assert f(seqStr)  ==' salne tigt '
    assert f(seqList) ==[5,7,9]
    assert f(seqTuble)==(5,7,9)

    #test return_every_other item removed
    assert rtn(a_string) == 'ti sasrn'
    assert rtn(a_list)   == [11,33,55,77]
    assert rtn(a_tuble)  == (11,33,55,77)

    #test reversed_with_slicing
    assert rev(a_string) == 'gnirts a si siht'
    assert rev(a_tuble)  == (77,66,55,44,33,22,11)
    assert rev(a_list)   == [88,77,66,55,44,33,22,11]

    print("All tests have passed")