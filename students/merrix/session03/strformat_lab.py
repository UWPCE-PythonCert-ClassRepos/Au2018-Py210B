elements = (2, 123.4567, 10000, 12345.67)
num_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)

element_tuple = (4, 30, 2017, 2, 27)
element_list = ['oranges', 1.3, 'lemons', 1.1]
data_in_column = [('john', 22, 650),
                 ('Eric', 15, 70), ('James', 35, 3500),
                 ('michael', 50, 4200)]


def first_task(elements):
    print("first task")
    print('file_{0:03} :  {1:9.2f}, {2:.2e}, {3:.2e}'.format(*elements))

def second_task(elements):
    print("\nsecond task")
    print(f'file_{elements[0]:03} :  {elements[1]:9.2f}, {elements[2]:.2e}, {elements[3]:.2e}')

def third_task(elements):
    print("\nthird task")
    num = ('{:d},'*len(elements)).format(*elements).strip(',')
    print(f'the {len(elements)} numbers are: {num}')

def fourth_task(element_tuple):
    print("\nfourth task")
    print(f'{element_tuple[3]:02} {element_tuple[4]:02} {element_tuple[2]:02} {element_tuple[0]:02} {element_tuple[1]:02} ')

def fifth_task(element_list):
    print("\nfifth task")
    print(f'The weight of {element_list[0]} is {element_list[1]} and the weight of a {element_list[2]} is {element_list[3]}')

    print("\nfifth task2")
    print(f'The weight of {element_list[0].upper()} is {element_list[1]*1.2} and the weight of a {element_list[2].upper()} is {element_list[3]*1.2}')

def sixth_task(data):
    print("\nsix task")
    for d in data:
        print('{:10}{:10}{:10}'.format(*d))

def final_task(data_range):
    print("\nfinal task")
    print(('{:5}'*10).format(*data_range))

first_task(elements)
second_task(elements)
third_task(num_tuple)
fourth_task(element_tuple)
fifth_task(element_list)
sixth_task(data_in_column)
final_task(range(1,11))
