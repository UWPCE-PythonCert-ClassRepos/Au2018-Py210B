#!usr/bin/env python

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

def exchange_first_last(seq):
    return seq[-1:]+seq[1:-1]+seq[:1] # exchange first char with last and vice versa
def alternative_item_remove(seq):
    return seq[::2] # every other char removed using slicing with step 2
def first_last_4_removed(seq):
    return seq[4:-4] # removing first four (slicing starts with 5th char[4th index])
    # and last four (end by negative index -4)
def reverse_seq(seq):
    return seq[::-1] # open slicing and include step -1 indicating read from last char
def last3_first3_mid3(seq):
    return seq[-len(seq)//3:]+seq[:len(seq)//3]+seq[len(seq)//3:-len(seq)//3]
    # new sequence with last third followed by first third and remaining- mid third using len and floor division 3
    
assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert last3_first3_mid3(a_string) =="stringthis is a "
assert last3_first3_mid3(a_tuple) == (5, 32, 2, 54, 13, 12)
assert first_last_4_removed(a_tuple)==()
assert first_last_4_removed(a_string)== ' is a st'

"""s = 'Hello this a string!'

tup3 = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)
print (s); print (tup3)
print (exchange_first_last(s))
print (exchange_first_last(tup3))
print (reverse_seq(s))
print (reverse_seq(tup3))
print (first_last_4_removed(s))
print (first_last_4_removed(tup3))
print (last3_first3_mid3(s))
print (last3_first3_mid3(tup3))"""

