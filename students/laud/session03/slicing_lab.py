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
    modified = seq[4:-4]
    return remove_every_other_item(modified)

# With the elements reversed (just with slicing)
def reverse(seq):
    return seq[::-1]

# With the last third, then first third, 
#  then the middle third in the new order.
def reshuffle(seq):
    one_third = int(len(seq)/3)
    last_third = seq[-one_third:]
    first_third = seq[0:one_third]
    middle_third = seq[one_third:-one_third]
    new_order = last_third + first_third + middle_third
    return new_order



if __name__ == "__main__":
    # Tests
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string)  == "ghis is a strint"
    assert remove_every_other_item(a_tuple) == (2, 13, 5)
    assert first_last_four_every_other(a_string) == " sas"
    assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert reshuffle(a_string) == "tringthis is a s"

    print("All tests passed!")