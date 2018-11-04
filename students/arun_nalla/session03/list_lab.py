#!usr/bin/env python
# Series 1
# Create a list containing fruits and print the list
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print (fruit_list)
# users input to add a fruit, add the fruit to list and print list
response = input('Please add a fruit of your interest\n>>> ').title()
fruit_list.append(response)
print (fruit_list)
while True:
    number = int(input('Please enter a number >0 and < to know the place of the fruit in the list: '))
    if number ==0 or number>len(fruit_list):
        print ('Please enter a number that is less than {}'.format(len(fruit_list)))
    else:
        print ('At "{}" position you have "{}".'.format(number, fruit_list[number-1]))
        break

# add a fruit using '+' sign

fruit_list = ['Grape'] + fruit_list
print ("Addition of grape:\n",fruit_list)
fruit_list.insert(0,'Mango')
for i in fruit_list:
    if i.startswith('P'):
        print (i)
#Series2

print (fruit_list)
fruit_list.remove(fruit_list[-1])
print (fruit_list)

while True:
    del_fruit = input("Remove a fruit\n>>> ").title()
    if del_fruit in fruit_list:
        print ('{} has been deleted from the list'.format(del_fruit))
        fruit_list.remove(del_fruit)
        print (fruit_list)
        break
    else:
        print ('Enter correct name')
#series 3
list_fruit = fruit_list[::]

for fruit in fruit_list:
    while True:
        user_likes = input("Do you like {}:\nif yes enter Y\nif no enter N:\n".format(fruit.lower())).upper()
        if user_likes == 'N':
            list_fruit.remove(fruit)
            break
        elif user_likes == 'Y':
            break
        else:
            print ('Please enter either Y (for Yes) or (N for No)')

print("Modified list of fruits", list_fruit)

#series 4
# make a copy of the original list and reverse the letters in the new list
list_fruit = fruit_list[::]
print (list_fruit)
rev_list_fruits = []
for fruit in list_fruit:
    rev_fruit = fruit[::-1]
    rev_list_fruits.append(rev_fruit)
print (fruit_list[:-1]) # del last item from the original
print (rev_list_fruits)
