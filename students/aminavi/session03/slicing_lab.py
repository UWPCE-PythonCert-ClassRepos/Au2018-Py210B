seq = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
str = "lets do something with this"
# seq
def exchange_first_last(x):
    return x[-1:]+ x[1:-1]+ x[:1]
# print(exchange_first_last(str))
assert exchange_first_last(seq) == [21,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,4]
assert exchange_first_last(str) == 'sets do something with thil'

def return_everyother(x):
	return x[0::2] 
# print(return_everyother(seq))
assert return_everyother(seq) == [4, 6, 8, 10, 12, 14, 16, 18, 20]
assert return_everyother(str) == 'lt osmtigwt hs'

def first_four_everyother(x):
    return x[4:-4:2]
# print(first_four_everyother(str))
assert first_four_everyother(seq) == [8, 10, 12, 14, 16]

def elemets_reversed(x):
    return x[::-1]
# print(elemets_reversed(str))
assert elemets_reversed(seq) == [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4]
assert elemets_reversed(str) == 'siht htiw gnihtemos od stel'

def rearrange(x):
    thrd = len(x)//3
    return x[-thrd:] + x[0:thrd + thrd]
# print(rearrange(str))
assert rearrange(seq) == [16, 17, 18, 19, 20, 21, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

