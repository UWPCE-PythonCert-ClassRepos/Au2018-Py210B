#!/usr/bin/env python3
import itertools
# import inflection
from inflection import singularize


# Task One utility methods
def first_place(tuple_in):
    first = str(tuple_in[0]).zfill(3)
    return first

def second_place(tuple_in):
    second = str(round(tuple_in[1], 2))
    return second

def third_place(tuple_in):
    third = format(tuple_in[2]/10000, '.2f')
    # third = str(round(tuple_in[2]/10000, 2))
    return third

def fourth_place(tuple_in):
    fourth = format(tuple_in[3]/10000, '.2f')
    # fourth = tuple_in[3]
    return fourth


def task_one(in_tuple):
    """
    Write a format string that will take the following four element tuple
        ( 2, 123.4567, 10000, 12345.67)
    and produce:
        file_002 :   123.46, 1.00e+04, 1.23e+04
    """  
    first = first_place(in_tuple)
    colon = ':'
    second = second_place(in_tuple)  
    third = third_place(in_tuple)
    fourth = fourth_place(in_tuple)
    formatted = 'file_{} {}  {}, {}, {}'.format(first, colon, second, third, fourth)
    return formatted

def task_two(in_tuple):
    """
    Write a format string that will take the following four element tuple
        ( 2, 123.4567, 10000, 12345.67)
    and produce:
        file_002 :   123.46, 1.00e+04, 1.23e+04
    """  
    first = first_place(in_tuple)
    colon = ':'
    second = second_place(in_tuple)  
    third = third_place(in_tuple)
    fourth = fourth_place(in_tuple)
    formatted = 'file_%s %s  %s, %s, %s'.format(first, colon, second, third, fourth)
    return formatted

def task_three(in_tuple_2):
    tuple_length = len(in_tuple_2)
    form_string = f'The {tuple_length} numbers are: '
    for x in range(tuple_length):
        form_string += '{}, '
    return form_string.format(*in_tuple_2)


def task_four(in_tuple_3):
    """ Use string formatting to convert (4, 30, 2017, 2, 27)
    into: '02 27 2017 04 30'
    """
    l = list(in_tuple_3)
    formatted = '{} {} {} {} {}'.format(str(l[3]).zfill(2),l[4],l[2],str(l[0]).zfill(2),l[1])
    return formatted


def task_five(in_string):
    """
    Write an f-string that will take ['oranges', 1.3, 'lemons', 1.1]
    And return: The weight of an orange is 1.3 and the weight of a lemon is 1.1
    """
    coupler = ' and the weight of '
    string = []
    string_length = len(in_string)
    """ Create tuples pairs from list """
    for x in in_string:
        tupled = [(in_string[i],in_string[i+1]) for i in range(0,len(in_string),2)]
    for y,z in tupled:
        singular = singularize(str(y))
        first_letter = singular[1]
        """ Determine the indefinite article to prefix, based on spelling """
        if(first_letter) in ('a', 'e', 'i', 'o', 'u'):
            prefix = 'a'
        else:
            prefix = 'an'
            """ For each pair, create a formatted string """
        string.append('{} {} {} {}'.format(prefix, singular.upper(), 'is', z+(0.2*z) )) 
    formatted = 'The weight of ' +  coupler.join(string)
    return formatted


def task_six(table_data):
    list = table_data.split()
    rows = ''
    for i in range(0, len(list), 3):
        row = ''
        tupled = list[i:i + 3]
        string = ','.join(tupled)
        print('{:10} {:>5} {:>10}'.format(*tupled))
    
if __name__ == "__main__":
    # Declare the supplied tuple as a globally accessible variable
    global tuple_in
    in_tuple = (2, 123.4567, 10000, 12345.67)
    in_tuple_2 = (1,2,3)
    in_tuple_3 = ( 4, 30, 2017, 2, 27)
    in_string = ['oranges', 1.3, 'lemons', 1.1]
    table_data = "Hosung 45 $36.32 David 34 $90.12 Alan 45 $60.42 Josh 51 $6.32 Ryan 25 $15.00"
    
    task_one = task_one(in_tuple)
    task_two = task_two(in_tuple)
    task_three = task_three(in_tuple_2)
    task_four = task_four(in_tuple_3)
    task_five = task_five(in_string)
    task_six = task_six(table_data)

    # print(task_one)
    print(task_two)
    # print(task_three)
    # print(task_four)
    # print(task_five)
    # print(task_six)