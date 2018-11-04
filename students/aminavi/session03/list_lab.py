#!/usr/bin/env python3

list = ["Apple","Pears","Oranges","Peaches"]

print(list)

#Grapes
fruit = input ("Which fruit would you like to add? ")
list.append(fruit)
print(list)

fruit_number = input ("Which fruit would you like to call?\ Input the number of the fruit:")
fn = int(fruit_number)
print(fruit_number +" "+ list[fn-1]) 

#Watermelon
fruit1 = input ("Which fruit would you like to add? ")
list = [fruit1]+list
print(list)

#Pineapple
fruit2 = input ("Which fruit would you like to add? ")
list.insert(0,fruit2)
print(list)

for i in list:
    if i[0] == "P":
        print(i)

list2 = list[:]
print(list2)
list2.remove("Grapes")
print(list2)

del_fruit = input("Which fruit would you like to delete? \Input the name of the fruit: ")
list2.remove(del_fruit)
print(list2)


list3 = list[:]
result3 = []
for i in list3:
    like_fruit = input('do you like ' + i.lower() + '? ')
    while like_fruit.lower() not in ('no', 'yes'):
        like_fruit = input('do you like ' + i.lower() + '? ')
    if like_fruit.lower() == 'yes':
            result3.append(i.lower())
print(result3)


result4 =[w[::-1] for w in list]
list.remove(list[-1])
print(list)
print(result4)