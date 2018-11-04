from decimal import *

#Task One
print("Task One")
print("File_{:03d} :  {:.2f}, {:.2e}, {:.3g}".format(2, 123.4567, 10000, 12345.67))

#Task Two
print("\nTask Two")
value1=2
value2=123.4567
value3=10000
value4=12345.67
#?? trying to get significance of 3
getcontext().prec = 3 
#??not sure about 3 significant figures for value4
print(f"File_{str(value1).zfill(3)} :  {round(value2,2)}, {Decimal(value3):.2e}, {Decimal(value4):.2e}")

#Task Three
#??No commas? 
print("\nTask Three")
def formatter(in_tuple):
    form_string = f'the {str(len(in_tuple))} numbers are:  {("{:2}" * len(in_tuple))}'
    return form_string.format(*in_tuple)

print(formatter((2,3,5,7,9)))


#Task Four
print("\nTask Four")
print("{3:02} {4:02} {2:02} {0:02} {1:02}".format(4, 30, 2017, 2, 27))

#Task Five
print("\nTask Five")
tasklist = ['oranges', 1.3, 'lemons', 1.1]

print(f"The weight of an {tasklist[0][0:-1]} is {tasklist[1]} and the weight of a {tasklist[2][0:-1]} is {tasklist[3]}")

print(f"The weight of an {tasklist[0][0:-1].upper()} is {(tasklist[1] * .2) + tasklist[1]} and the weight of a {tasklist[2][0:-1].upper()} is {(tasklist[3] * .2) + tasklist[3]}")

#Task Six
#Part 1 of Task Six
print("\nTask Six Part 1")

taskdata = [("Mary Jane",26 , 25.00),
            ("John Blanchard", 40, 500.00),
            ("Bernard Barb", 50, 2000.00)
            ]

for name, age, cost in taskdata:
    print("{:<20} {:>}  ${:>8.2f}".format(name, age, cost))

#Part 2 of Task Six
print("\nTask Six Part 2")
tasktuple = tuple(range(10))

print(("{:>5}" * len(tasktuple)).format(*tasktuple))