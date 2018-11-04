#!/usr/bin/env python
'''Slicing Lab exercise for Session 3, Python 210
Written by David K. Arasim - 10/17/18'''

#First and last items exchanged in sequence
def exch_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

#Remove every other item from sequence
def rem_every_other(seq):
    return seq[::2]

#First four and last four items removed, and every other item in remaining sequence
def rem_four_every_other(seq):
    seq = seq[4:-4]
    return seq[1::2]

#Entire sequence in reverse order
def reversed(seq):
    return seq[::-1]

#Sequence with last third, then first third, then the middle third in that order
#Note:  Remainder from division by 3 will be included with the last third
def tri_shuffle(seq):
    third = int(len(seq)/3)  
    return seq[(third*2):] + seq[:third] + seq[third:(third*2)]

#################################################################

x = 'String to exchange first and last'
t = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)

print(exch_first_last(x))
print(exch_first_last(t))
print()

print(rem_every_other(x))
print(rem_every_other(t))
print()

print(rem_four_every_other(x))
print(rem_four_every_other(t))
print()

print(reversed(x))
print(reversed(t))
print()

print(tri_shuffle(x))
print(tri_shuffle(t))
print()

#################################################################

if __name__ == '__main__':
    assert exch_first_last(x) == 'ttring to exchange first and lasS'
    assert exch_first_last(t) == (16,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1)

    assert rem_every_other(x) == 'Srn oecag is n at'
    assert rem_every_other(t) == (1,3,5,7,9,11,13,15)

    assert rem_four_every_other(x) == 'gt xhnefrtad'
    assert rem_four_every_other(t) == (6,8,10,12)

    assert reversed(x) == 'tsal dna tsrif egnahcxe ot gnirtS'
    assert reversed(t) == (16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1)

    assert tri_shuffle(x) == 'st and lastString to exchange fir'
    assert tri_shuffle(t) == (11,12,13,14,15,16,1,2,3,4,5,6,7,8,9,10)

    print('Assert tests passed')