def exchange_first_last(data):
    return data[-1:] + data[1:-1] + data[0:1]

def remove_every_other(data):
    return data[::2]

def remove_first_last_keep_every_other(data):
    return data[4:-4:2]

def reverse_element(data):
    return data[::-1]

def reoder_last_first_middle(data):
    first = len(data) // 3
    middle = first * 2
    return data[middle:] + data[:first] + data[first:middle]

a_list = [1,2,3,4,5]
a_long_list = [1,2,3,4,5,6,7,8,9]
a_tuple = (2,4,6,8,10)
a_string = 'without justice, courage is week'

assert exchange_first_last(a_list) == [5,2,3,4,1]
assert exchange_first_last(a_tuple) == (10,4,6,8,2)
assert remove_every_other(a_list) == [1,3,5]
assert remove_first_last_keep_every_other(a_string) == 'otjsie org s'
assert reverse_element(a_list) == [5,4,3,2,1]
assert reoder_last_first_middle(a_long_list) == [7,8,9,1,2,3,4,5,6]
print('All tests passed!')