# with the first and last items exchanged.
def swap_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

# with every other item removed.
def every_second(seq):
    return(seq[::2])

# with the first 4 and the last 4 items removed, and then every other item in 
# the remaining sequence.
def first_last_four_even(seq):
    return(seq[4:-4:2])

# with the elements reversed (just with slicing).
def reversed(seq):
    return(seq[::-1])

# with the last third, then first third, then the middle third in the new order.
def scrambled_thirds(seq):
    third = len(seq) // 3
    return seq[third*2:] + seq[:third] + seq[third:third*2]


a_string = "the quick brown"
a_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
short_string = "dog"
short_list = [1, 2]

if __name__ == "__main__":
    assert swap_first_last(a_string) == "nhe quick browt"
    assert swap_first_last(a_tuple) == (15, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1)
    assert swap_first_last(short_string) == "god"
    assert swap_first_last(short_list) == [2, 1]

    assert every_second(a_string) == "teqikbon"
    assert every_second(a_tuple) == (1, 3, 5, 7, 9, 11, 13, 15)
    assert every_second(short_string) == "dg"
    assert every_second(short_list) == [1]

    assert first_last_four_even(a_string) == "qikb"
    assert first_last_four_even(a_tuple) == (5, 7, 9, 11)
    assert first_last_four_even(short_string) == ''
    assert first_last_four_even(short_list) == []

    assert reversed(a_string) == "nworb kciuq eht"
    assert reversed(a_tuple) == (15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
    assert reversed(short_string) == "god"
    assert reversed(short_list) == [2, 1]

    assert scrambled_thirds(a_string) == "brownthe quick "
    assert scrambled_thirds(a_tuple) == (11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    assert scrambled_thirds(short_string) == "gdo"
    assert scrambled_thirds(short_list) == [1, 2]