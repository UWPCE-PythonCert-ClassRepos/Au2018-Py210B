#hw3, slicing practice

def sequence_1(sequence):
    """first and last items exchanged"""
    first = sequence[0]
    last = sequence[-1]
    rest = sequence[1:-1]
    new_sequence = last + rest + first

    return new_sequence

def sequence_2(sequence):
    """every other item removed"""
    sequence = sequence[::2]

    return sequence

def sequence_3(sequence):
    """with the first 4 and the last 4 items removed, and then every other item in the remaining sequence"""
    sequence = sequence[4:-5:2]

    return sequence

def sequence_4(sequence):
    """revers elements with slicing"""
    sequence = sequence[::-1]

    return sequence

def sequence_5(sequence):
    """with the last third, then first third, then the middle third in the new order."""
    sequence_unit = int(len(sequence)/3)
    last_third = sequence[-sequence_unit:]
    first_third = sequence[0:sequence_unit]
    middle_third = sequence[sequence_unit:-sequence_unit]
    new_sequence = last_third + first_third + middle_third

    return(new_sequence)


#test
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
a_long_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
a_list = ["a","a","b","b","c","c"]

assert sequence_1(a_string) == "ghis is a strint"
assert sequence_2(a_tuple) == (2, 13, 5)
assert sequence_3(a_long_list) == ['e', 'g', 'i']
assert sequence_4(a_tuple) == (32, 5, 12, 13, 54, 2)
assert sequence_5(a_list) == ["c","c","a","a","b","b"]

