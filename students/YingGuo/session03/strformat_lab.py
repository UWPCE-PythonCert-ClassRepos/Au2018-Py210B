
#task one: print 'file_002 :   123.46, 1.00e+04, 1.23e+04'
example_tuple = ( 2, 123.4567, 10000, 12345.67)
string01 = "file_{:03d} :   {:.2f}, {:.2e}, {:.2e}".format(2, 123.4567, 10000, 12345.67)
print(string01)


#task two: resultes from take one, repeat with alternate type of format string
a = 2
b = 123.4567
c = 10000
d = 12345.67

string02 = f"file_{a:03d} :   {b:.2f}, {c:.2e}, {d:.2e}"
print(string02)


#task three: in string formatting, take an arbitrary number of values
def formatter(in_tuple):
	unit = ["{:d}"]
	len_tuple = len(in_tuple)
	total_list = unit*len_tuple
	total_string = ", ".join(total_list)
	final_string = "the {} numbers are: " + total_string
	print(final_string.format(len_tuple,*in_tuple))
	
	
a_tuple = (1,2,3,4)
formatter(a_tuple)


#task four: use string formatting to print a tuple. the string should look like '02 27 2017 04 30'
given_tuple = (4,30,2017,2,27)
element1 = given_tuple[-2]
element2 = given_tuple[-1]
element3 = given_tuple[-3]
element4 = given_tuple[0]
element5 = given_tuple[1]

string04 = f"{element1:02d} {element2:d} {element3:d} {element4:02d} {element5:02d}"
print(string04)


#task five:use f-string to display The weight of an orange is 1.3 and the weight of a lemon is 1.1
given_list = ['oranges', 1.3, 'lemons', 1.1]

fruit1 = given_list[0]
fruit2 = given_list[-2]
weight1 = given_list[1]
weight2 = given_list[-1]

string05 = f"The weight of an {fruit1} is {weight1} and the weight of a {fruit2} is {weight2}"
print(string05)

#reprint the string to show the names of the fruit in upper case and show the weight 20% higher
string05_modified = f"The weight of an {fruit1.upper()} is {(weight1-1):.0%} higher and the weight of a {fruit2.upper()} is {(weight2-1):.0%} higher"
print(string05_modified)


#task Six:print a table of several rows, each with a name, an age and a cost.some of the costs in decimals.
tuple06 = ("Tom", 50, 10.5, "Tim", 55, 1000)
string06 = "{:>8} {:>8} {:>8} \n {:>8} {:>8} {:>8} \n {:>8} {:>8} {:>8}".format("Name","Age","Cost",*tuple06)
print(string06)

#extra task: a tuple with 10 consecutive numbers, print in columns that are 5 charaters wide.
tuple_10nums = tuple(range(1,11))
for i in tuple_10nums:
	print("{:>5}".format(i))