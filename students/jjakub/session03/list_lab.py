#!/usr/bin/env python3

### Series 1
list_fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(list_fruit)

user_fruit = input("Which fruit would you like to add? ")
list_fruit.append(user_fruit)
print(list_fruit)

user_num = input("Provide the number of the fruit to return: ")
print(user_num + " " + list_fruit[int(user_num)-1])

user_fruit_02 = input("Which fruit would you like to add? ")
list_fruit = [user_fruit_02] + list_fruit
print(list_fruit)

user_fruit_03 = input("Which fruit would you like to add? ")
list_fruit.insert(0,user_fruit_03)
print(list_fruit)

for frt in list_fruit:
    if frt[0] == "P":
        print(frt)

### Series 2
print(list_fruit)

list_fruit = list_fruit[:-1]
print(list_fruit)

del_fruit = input("Which fruit would you like to delete? ")
list_fruit.remove(del_fruit)
print(list_fruit)

### Series 3
mod_list = list_fruit[:]
for frt in list_fruit:
    user_pref = input("Do you like " + frt.lower() + "? ")
    while user_pref.lower() not in ("yes", "no"):
        user_pref = input("Please answer yes or no: ")
    if user_pref.lower() == 'no':
            mod_list.remove(frt)
print(mod_list)

rev_lst = [frt[::-1] for frt in list_fruit]
list_fruit.remove(list_fruit[-1])
print(list_fruit)
print(rev_lst)