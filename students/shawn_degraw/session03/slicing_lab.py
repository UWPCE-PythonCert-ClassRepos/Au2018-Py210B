def exchange_first_last(seq):
    """ Provide any type of sequence and return the first and last items exchanged """
    return seq[-1:] + seq[1:len(seq)-1] + seq[:1]

def remove_every_other(seq):
    """ Return every other item in the provided sequence """
    return seq[::2]

def double_minus_four(seq):
    """ remove first 4 and last 4 and then return every other item """
    return seq[4:len(seq)-4:2]

def reverse_elements(seq):
    """ reverse all elements in the provided sequence """
    return seq[::-1]

def rearrange_by_thirds(seq):
    """ Return last third, then first third and then middle third from provided sequence """
    split_value = len(seq) // 3
    return seq[-split_value:] + seq[:split_value] + seq[split_value:-split_value]

if __name__ == "__main__":
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert exchange_first_last(a_list) == [15, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1]

    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)
    assert remove_every_other(a_list) == [1, 3, 5, 7, 9, 11, 13, 15]

    assert double_minus_four(a_string) == " sas"
    assert double_minus_four(a_tuple) == ()
    assert double_minus_four(a_list)  == [5, 7, 9, 11]

    assert reverse_elements(a_string) == "gnirts a si siht"
    assert reverse_elements(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert reverse_elements(a_list) == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    assert rearrange_by_thirds(a_string) == "tringthis is a s"
    assert rearrange_by_thirds(a_tuple) == (5, 32, 2, 54, 13, 12)
    assert rearrange_by_thirds(a_list) == [11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("All tests passed.")