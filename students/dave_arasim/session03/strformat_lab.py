#!/usr/bin/env python
'''String Format Lab exercise for Session 3, Python 210
Written by David K. Arasim - 10/21/18'''

#Task 1
print('file_{:03} : {:.2f}, {:.2e}, {:.2e}'.format(2, 123.4567, 10000, 12345.67))

#Task 2
file_name_seq  = '2'.zfill(3)
float_two_dec  = format(123.4567, '.2f')
scientific_int = format(10000, '.2e')
scientific_flt = format(12345.67, '.2e')

print(f'file_{file_name_seq} : {float_two_dec}, {scientific_int}, {scientific_flt}')

#Task 3
def formatter(*t):
    len_t = len(t)
    f_cnt = ''

    for x in range(len_t):
        if f_cnt != '':
            f_cnt += ', '
        f_cnt +='{:d}'

    f_str = 'The {:d} numbers are: '
    f_str += f_cnt
    f_str = f_str.format(len_t, *t)
    return f_str

t = (1,2,3,4,5,6)
print (formatter(*t))

t = (10,4,6,7,42)
print (formatter(*t))

#Task 4
print('{3:02} {4} {2} {0:02} {1}'.format(4, 30, 2017, 2, 27))

#Task 5
f_elements = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {f_elements[0][:-1]} is {f_elements[1]} and the weight of a {f_elements[2][:-1]} is {f_elements[3]}')
print(f'The weight of an {f_elements[0][:-1].upper()} is {f_elements[1]*1.2} and the weight of a {f_elements[2][:-1].upper()} is {f_elements[3]*1.2}')

#Task 6
print('{:10}  {:>5}  {:>10}'.format('Fred', 42, '$4.32'))
print('{:10}  {:>5}  {:>10}'.format('Barney', 36, '$27.86'))
print('{:10}  {:>5}  {:>10}'.format('Charles', 2, '$150.57'))
print('{:10}  {:>5}  {:>10}'.format('Ted', 101, '$1004.32'))

t = (1,2,3,4,5,6,7,8,9,10)
print('{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}'.format(*t))