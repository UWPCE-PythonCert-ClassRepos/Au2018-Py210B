#!/usr/bin/env python3

##################################################
## Author: Jackie Cheung
## Date: 2018/10/23
## Version: 0.1
## Class: Au2018-Py210B
## Description: Slicing Lab - Get the basics of sequence slicing down
##################################################

def exchange_first_last(seq):
    """ with the first and last items exchanged """

    first = seq[:1]
    last = seq[-1:]
    mid = seq[1:-1]
    a_new_sequence = last + mid + first

    return a_new_sequence

def remove_first_4_last_4_every_other_remain(seq):
    """ with the first 4 and the last 4 items removed, and then every other item in the remaining sequence """

    a_new_sequence = seq[4:-4:2]

    return a_new_sequence

def reverse_element(seq):
    """ with the elements reversed (just with slicing) """

    a_new_sequence = seq[::-1]

    return a_new_sequence

def new_order_last_third_first_third_middle_third(seq):
    """ with the last third, then first third, then the middle third in the new order """

    # number of items for a third of the sequence
    num_third = int(len(seq)/3)

    # Note: first third and middle third are already in sequence, so only need to find out first third
    last_third = seq[-num_third:]
    two_third = seq[:-num_third]
    a_new_sequence = last_third + two_third

    return a_new_sequence

if __name__ == "__main__":
    # run some tests

    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    b_string = "this is a much longer string for testing"
    b_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)

    assert remove_first_4_last_4_every_other_remain(b_string) == " samc ogrsrn o e"
    assert remove_first_4_last_4_every_other_remain(b_tuple) == (4, 6, 8, 10, 12, 14)

    assert reverse_element(a_string) == "gnirts a si siht"
    assert reverse_element(a_tuple) == (32, 5, 12, 13, 54, 2)

    assert new_order_last_third_first_third_middle_third(b_string) == "g for testingthis is a much longer strin"
    assert new_order_last_third_first_third_middle_third(b_tuple) == (14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

    print("tests passed")
