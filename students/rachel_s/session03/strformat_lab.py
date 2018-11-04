# Task One
# Write a format string that will take the following four element tuple:
# ( 2, 123.4567, 10000, 12345.67)
# and produce:
# 'file_002 :   123.46, 1.00e+04, 1.23e+04'

"file_{:0>3d} :   {:.2f}, {:.2e}, {:.2e}".format(2, 123.4567, 10000, 12345.67)


# Task Two
# Using your results from Task One, repeat the exercise, but this time using an 
# alternate type of format string (hint: think about alternative ways to use 
# .format() (keywords anyone?), and also consider f-strings if you’ve not used 
# them already).

my_str = "file_{first:0>3d} :   {second:.2f}, {third:.2e}, {fourth:.2e}"
my_str.format(first=2, second=123.4567, third=10000, fourth=12345.67)


# Task Three
# Rewrite:
# "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
# to take an arbitrary number of values.

def formatter(*t):
    return f"the {len(t)} numbers are: " + ", ".join(map(str, t))


# Task Four
# Given a 5 element tuple:
# ( 4, 30, 2017, 2, 27)
# use string formating to print:
# '02 27 2017 04 30'

"{3:0>2d} {4} {2} {0:0>2d} {1}".format(4, 30, 2017, 2, 27)


# Tast Five
# Given the following four element list:
# ['oranges', 1.3, 'lemons', 1.1]
# Write an f-string that will display:
# The weight of an orange is 1.3 and the weight of a lemon is 1.1

fruits = ('oranges', 1.3, 'lemons', 1.1)
f"The weight of an {fruits[0][:-1]} is {fruits[1]} and the weight of a {fruits[2][:-1]} is {fruits[3]}"


# Now see if you can change the f-string so that it displays the names of the 
# fruit in upper case, and the weight 20% higher (that is 1.2 times higher).

f"The weight of an {fruits[0][:-1].upper()} is {fruits[1] * 1.2} and the weight of a {fruits[2][:-1].upper()} is {fruits[3] * 1.2}"


# Task Six
# Write some Python code to print a table of several rows, each with a name, an 
# age and a cost. Make sure some of the costs are in the hundreds and thousands 
# to test your alignment specifiers. 

my_colnames = ("NAME", "AGE", "COST")
my_contents = (("Apple", 22, 1234567.89), ("Peach", 1, 200), ("Pear", 14, 12345.00), ("Plum", 170, 2.25), ("Brontosaurus", "old", 2000000.99))

def tabler(colnames, contents):
    fstring = "{name:>12}{age:>6}{cost:>15,.2f}"
    print("{name:>12}{age:>6}{cost:>15}".format(name=colnames[0], age=colnames[1], cost=colnames[2]))
    for i in contents:
        print(fstring.format(name=i[0], age=i[1], cost=i[2]))

tabler(my_colnames, my_contents)


# And for an extra task, given a tuple with 10 consecutive numbers, can you 
# work how to quickly print the tuple in columns that are 5 charaters wide? It 
# can be done on one short line!

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# Here are some tests.

if __name__ == "__main__":
    assert my_str.format(first=2, second=123.4567, third=10000, fourth=12345.67) == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    assert "file_{:0>3d} :   {:.2f}, {:.2e}, {:.2e}".format(2, 123.4567, 10000, 12345.67) == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    assert formatter(1, 2, 3) == "the 3 numbers are: 1, 2, 3"
    assert "{3:0>2d} {4} {2} {0:0>2d} {1}".format(4, 30, 2017, 2, 27) == '02 27 2017 04 30'
    assert f"The weight of an {fruits[0][:-1]} is {fruits[1]} and the weight of a {fruits[2][:-1]} is {fruits[3]}" == "The weight of an orange is 1.3 and the weight of a lemon is 1.1"
