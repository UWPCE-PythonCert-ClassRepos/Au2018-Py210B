#!/usr/bin/env python3

# The first and last items exchanged
# example sequence: a_string = "this is a string"
def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

# With every other item removed
def remove_every_other_item(seq):
    return seq[::2]

# With the first 4 and the last 4 items removed, 
# and then every other item in the remaining sequence.
def first_last_four_every_other(seq):
    modified = seq[4:-4:2]
    return remove_every_other_item(modified)

# With the elements reversed (just with slicing)
def reversed(seq):
    return seq[::-1]

# With the last third, then first third, 
#  then the middle third in the new order.
def reshuffle(seq):
    one_third = int(len(sequence)/3)
    last_third = sequence[-one_third:]
    first_third = sequence[0:one_third]
    middle_third = sequence[one_third:-one_third]