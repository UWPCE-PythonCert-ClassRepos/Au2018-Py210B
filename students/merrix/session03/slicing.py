def exchange_first_last(str_seq):
    strseq = list(str_seq)
    strseq[0], strseq[-1] = strseq[-1], strseq[0]
    
    a_new_sequence = ''.join(strseq)

    return a_new_sequence

a_string = ("this is a string")

def exchange_first_last1(tup_seq):
    tup_seq[0], tup_seq[-1] = tup_seq[-1], tup_seq[0]
    new_sequence = (tup_seq)
    return new_sequence
a_tuple = [2, 54, 13, 12, 5, 32]

assert exchange_first_last1(a_tuple) == [32, 54, 13, 12, 5, 2]



assert exchange_first_last(a_string) == ("ghis is a strint")

