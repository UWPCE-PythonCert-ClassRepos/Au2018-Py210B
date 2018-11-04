##################################################
## Author: Jackie Cheung
## Date: 2018/10/23
## Version: 0.1
## Class: Au2018-Py210B
## Description: String Formatting Exercise
##################################################

print("\n----- Task One -----\n")

task_one = ( 2, 123.4567, 10000, 12345.67)

# output 'file_002 :   123.46, 1.00e+04, 1.23e+04'
print("'file_{:0>3d} :".format(task_one[0]), " {:.2f},".format(task_one[1]), "{:.2e},".format(task_one[2]), "{:.3g}'".format(task_one[3]))


print("\n----- Task Two -----\n")

task_two = ( 2, 123.4567, 10000, 12345.67)

# output 'file_002 :   123.46, 1.00e+04, 1.23e+04' using alternative type
print("'file_%03d :"%(task_two[0]), " %.2f,"%(task_two[1]), "%.2e,"%(task_two[2]), "%.3g'"%(task_two[3]))


print("\n----- Task Three -----\n")

# make a form_string that was the right length for an arbitrary tuple
def formatter(in_tuple):
    do_something_here_to_make_a_format_string

    return form_string.format(in_tuple)


print("\n----- Task Four -----\n")

t = ( 4, 30, 2017, 2, 27)

form_string = "{:0>2d}, {:0>2d}, {:0>2d}, {:0>2d}, {:0>2d}"

# output '02 27 2017 04 30'
form_string.format(t[3], t[4], t[2], t[0], t[1])


print("\n----- Task Five -----\n")

task_five = ['oranges', 1.3, 'lemons', 1.1]

f"The weight of an {task_five[0]} is {task_five[1]} and the weight of a {task_five[2]} is {task_five[3]}"

# displays the names of the fruit in upper case, and the weight 20% higher
f"The weight of an {task_five[0].upper()} is {task_five[1]*1.2} and the weight of a {task_five[2].upper()} is {task_five[3]*1.2}"


print("\n----- Task Six -----\n")

print('{:20}{:20}{:10}{:20}'.format('Firstname', 'Lastname', 'Age', 'cost'))
print('{:20}{:20}{:10}${:20}'.format('Kevin', 'O Leary', '64', '400000000'))
print('{:20}{:20}{:10}${:20}'.format('Barbara', 'Corcoran', '69', '80000000'))
print('{:20}{:20}{:10}${:20}'.format('Daymond', 'John', '49', '250000000'))
print('{:20}{:20}{:10}${:20}'.format('Robert', 'Herjavec', '56', '200000000'))