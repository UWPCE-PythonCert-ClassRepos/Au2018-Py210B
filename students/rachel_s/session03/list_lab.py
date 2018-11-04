#!/usr/bin/env python3


# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
og_fruits = fruits.copy()

# Display the list (plain old print() is fine…).
print(fruits)

# Ask the user for another fruit and add it to the end of the list.
response = input("Please tell me another fruit > ")
fruits.append(response.capitalize())

# Display the list.
print(fruits)

# Ask the user for a number and display the number back to the user and the 
# fruit corresponding to that number (on a 1-is-first basis). Remember that 
# Python uses zero-based indexing, so you will need to correct.
my_num = input("Pick a number between 1 and 6 > ")

if int(my_num) in range(7):
    print("{}. {}".format(my_num, fruits[int(my_num)-1]))
else:
    y_num = input("No no no, pick a number between 1 and 6 > ")

# Add another fruit to the beginning of the list using “+” and display the list.
fruits = ["Persimmon"] + fruits
print(fruits)

# Add another fruit to the beginning of the list using insert() and display the 
# list.

fruits.insert(0, "Kiwi")
print(fruits)

# Display all the fruits that begin with “P”, using a for loop.
for i in fruits:
    if i.lower()[0] == "p":
        print(i)
print()


# Display the list.
fruits = og_fruits.copy()
print(fruits)

# Remove the last fruit from the list.
del fruits[0]

# Display the list.
print(fruits)

# Ask the user for a fruit to delete, find it and delete it.
response = input("Please tell me a fruit to remove > ").capitalize()

while response not in fruits:
    response = input("That fruit isn't in my list. Name a fruit in my list > ").capitalize()
fruits.remove(response)

# (Bonus: Multiply the list times two. Keep asking until a match is found. Once 
# found, delete all occurrences.)
fruits = fruits * 2
while response in fruits:
    fruits.remove(response)

print(fruits)

# Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
# For each “no”, delete that fruit from the list.
# For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
# Display the list.

fruits = og_fruits.copy()

to_remove = []
for i in fruits:
    response = input("Do you like {}? ".format(i.lower())).lower()
    while response not in ["yes", "no"]:
        response = input("Please answer yes or no. Do you like {}? ".format(i.lower())).lower()
    if response == "no":
        to_remove.append(i)

for i in to_remove:
    fruits.remove(i)

print(fruits)

# Make a copy of the list and reverse the letters in each fruit in the copy.
# Delete the last item of the original list. Display the original list and the 
# copy.

fruits = og_fruits.copy()
backwards_fruits = fruits.copy()

for i in range(len(backwards_fruits)):
    backwards_fruits[i] = backwards_fruits[i][::-1]
print(backwards_fruits)

del fruits[0]
print(fruits)