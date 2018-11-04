
a_vec = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
a_str = "this is a string"

def first_last(seq):
    return seq[-1:]+ seq[1:-1]+ seq[:1]

def everyother(seq):
    return seq[0::2]

def mid_everyother(seq):
    return seq[4:-4:2]

def reverse(seq):
    return seq[::-1]

def thirds(seq):
    thrd = len(seq)//3
    return seq[-thrd:] + seq[0:thrd + thrd]

assert first_last(a_vec) == [15,2,3,4,5,6,7,8,9,10,11,12,13,14,1]
assert first_last(a_str) == "ghis is a strint"

assert everyother(a_vec) == [1,3,5,7,9,11,13,15]
assert everyother(a_str) == "ti sasrn"

assert mid_everyother(a_vec) == [5,7,9,11]
assert mid_everyother(a_str) == " sas"

assert reverse(a_vec) == [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
assert reverse(a_str) == "gnirts a si siht"

assert thirds(a_vec) == [11,12,13,14,15,1,2,3,4,5,6,7,8,9,10]
assert thirds(a_str) == "tringthis is a "

# original lists should not have been modified
assert a_vec == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
assert a_str == "tringthis is a s "