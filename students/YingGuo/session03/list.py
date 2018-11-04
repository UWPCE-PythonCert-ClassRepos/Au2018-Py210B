#!/usr/bin/env python3

"""Series 1 """

#Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
l = ["Apples","Oranges","Peaches"]

#Display the list.
print("The current fruit list is {}".format(l))

#Ask the user for another fruit and add it to the end of the list.
new = input("What fruit do you want to add").capitalize()
l.append(new)

#Display the list.
print("The new list is {}".format(l))

#Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis)
user_input = int(input("Which number you want to pick? The range is {}, starting from 1".format(len(l))))
print("The fruit you pick is {}".format(l[user_input-1]))

#Add another fruit to the beginning of the list using “+” and display the list.
l = ["Kiwi"] + l
print(l)

#Add another fruit to the beginning of the list using insert() and display the list.
l.insert(0,"Banana")
print(l)

#Display all the fruits that begin with “P”, using a for loop.
for i in range(len(l)):
    if l[i][0] is "P":
        print(l[i])
    else:
        pass


"""Series 2"""
#Display the list.
import copy
l2 = copy.deepcopy(l)
print(l2)

#Remove the last fruit from the list.
l2.remove(l2[-1])

#Display the list.
print(l2)

#Ask the user for a fruit to delete, find it and delete it.
user_input2 = input("Which fruite you want to delete?").capitalize()

if user_input2 in l2:
    l2.remove(user_input2)

print(l2)


"""Series 3"""
#using the list from series 1
import copy
l3 = copy.deepcopy(l)
"""Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
For each “no”, delete that fruit from the list.
For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
Display the list."""
for x in l3:
   while True:
        user_input3 = input("Do you like{}? answer Yes or No".format(x))
        if user_input3.capitalize() == "No":
            l3.remove(x)
            break
        if user_input3.capitalize() == "Yes":
            break
        else:
            print("please say Yes or No")
        
print(l3)

"""Series 4"""
#using the list from series 1
import copy
l4 = copy.deepcopy(l)
print("this is list from series 1", l4)

"""Make a copy of the list and reverse the letters in each fruit in the copy.
Delete the last item of the original list. Display the original list and the copy."""
import copy
l4_copy = copy.deepcopy(l4)

for i, x in enumerate(l4[:]):
    l4_copy[i] = x[::-1]

l4.remove(l4[-1])

print("original", l4)

print("copy", l4_copy)

