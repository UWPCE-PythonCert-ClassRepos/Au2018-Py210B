def task_one(in_tuple):
    print('file_{0:03} :  {1:9.2f}, {2:.2e}, {3:.2e}'.format(*in_tuple))

def task_two(in_tuple):
    print(f'file_{in_tuple[0]:03} :  {in_tuple[1]:9.2f}, {in_tuple[2]:.2e}, {in_tuple[3]:.2e}')

def task_three(in_tuple):
    num = ('{: d},'*len(in_tuple)).format(*in_tuple).strip(',')
    print(f'the {len(in_tuple)} numbers are: {num}')

def task_four(five_element_tuple):
    print(f'{five_element_tuple[3]:02} {five_element_tuple[4]:02} {five_element_tuple[2]:02} {five_element_tuple[0]:02} {five_element_tuple[1]:02} ')

def task_five(element_list):
    print(f'The weight of {element_list[0]} is {element_list[1]} and the weight of a {element_list[2]} is {element_list[3]}')
    
    print(f'The weight of {element_list[0].upper()} is {element_list[1]*1.2} and the weight of a {element_list[2].upper()} is {element_list[3]*1.2}')

def task_six(data):
    for d in data:
        print('{:10}{:10}{:10}'.format(*d))

def task_extra(data_range):
    print(('{:5}'*10).format(*data_range))

in_tuple = (2, 123.4567, 10000, 12345.6799999999)
num_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
five_element_tuple = (4, 30, 2017, 2, 27)
element_list = ['oranges', 1.3, 'lemons', 1.1]
data_in_column = [('Lisa', 22, 650), ('Bayton', 15, 70), ('Jackie', 35, 3500),('Kyle', 50, 4200)]

task_one(in_tuple)
task_two(in_tuple)
task_three(num_tuple)
task_four(five_element_tuple)
task_five(element_list)
task_six(data_in_column)
task_extra(range(1,11))