#!/usr/bin/env python
'''List Lab exercise for Session 3, Python 210
Written by David K. Arasim - 10/17/18'''

print('*'*20, ' Series 1 requirements ', '*'*20)
print()

fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

print(fruit_list)
print()

print('Please enter another fruit to add to the list: ', end='')
new_fruit = input()
print()

if new_fruit != '':
    fruit_list.append(new_fruit)

print(fruit_list)
print()

fruit_list_ct = len(fruit_list)

print('Please enter the fruit number to display (1 - ', fruit_list_ct, '): ', sep='', end='')
fruit_num = input()
try:
    fruit_num = int(fruit_num)
except ValueError:
    fruit_num = ''

if fruit_num == '':
    print('Sorry, but that is not a number')
else:
    if (fruit_num >= 1) and (fruit_num <= fruit_list_ct):
        print(fruit_num, ': ', fruit_list[(fruit_num-1)], sep='')
    else:
        print('That fruit number: ', fruit_num, ' is out of range', sep='')
print()

print(fruit_list)
print()

print('Please enter another fruit to insert at the beginning of the list: ', end='')
new_fruit = input()
print()

if new_fruit != '':
    fruit_list = [new_fruit] + fruit_list  #Inserting using '+'

print(fruit_list)
print()

print('Please enter another fruit to insert at the beginning of the list: ', end='')
new_fruit = input()
print()

if new_fruit != '':
    fruit_list.insert(0, new_fruit)      #Inserting using insert()

print(fruit_list)
print()

search_letter = 'P'

print('Here are the fruits that begin with "', search_letter, '": ', sep='')
for this_fruit in fruit_list:
    if this_fruit[0] == search_letter:
        print(this_fruit, end=' ')
print()
print()

###################################################################################################

print('*'*20, ' Series 2 requirements ', '*'*20)
print()

print(fruit_list)
print()

fruit_list.pop()

print('Removing last fruit in list with pop():')
print(fruit_list)
print()

print('Fruit to delete: ', end='')
fruit_name = input()
print()

if fruit_name == '':
    print('Nothing input...delete cancelled.')
else:
    fruit_found = False
    for i,this_fruit in reversed(list(enumerate(fruit_list))):
        #Run index in reverse order to prevent pop() indexing issues
        if this_fruit == fruit_name:
            fruit_list.pop(i)
            fruit_found = True
    if not(fruit_found):
	    print('Fruit not found: ', fruit_name)
    print()

print(fruit_list)
print()

print('List is now doubled (Series 2 Bonus):')
fruit_list = fruit_list * 2

fruit_found = False
while not(fruit_found):
    print(fruit_list)
    print()

    print('Forced delete, choose fruit from double-entry list (delete required): ', end='')
    fruit_name = input()
    print()

    if fruit_name == '':
        print('Nothing input...')
    else:
        for i,this_fruit in reversed(list(enumerate(fruit_list))):
            #Run index in reverse order to prevent pop() indexing issues
            if this_fruit == fruit_name:
                fruit_list.pop(i)
                fruit_found = True
        if not(fruit_found):
	        print('Fruit not found: ',fruit_name)
        if fruit_list == []:
            #This probably never will happen here, but just to be safe for empty list conditions
            print('List is now empty')
            fruit_found = True
    print()

print(fruit_list)
print()

###################################################################################################

print('*'*20, ' Series 3 requirements ', '*'*20)
print()

fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

print('Restored list from Series 1:')
print(fruit_list)
print()

for this_fruit in fruit_list[:]:
    yes_or_no = False
    while not(yes_or_no):
        print('Do you like ', this_fruit.lower(), '? ', sep='', end='')
        fruit_like = input()
        if fruit_like == 'no':
            yes_or_no = True
            fruit_list.remove(this_fruit)
        elif fruit_like == 'yes':
            yes_or_no = True
        else:
            print('Please enter yes or no')
        print()
        print(fruit_list)
        print()

###################################################################################################

print('*'*20, ' Series 4 requirements ', '*'*20)
print()

fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

print('Restored list from Series 1:')
print(fruit_list)
print()

new_list = []
for i,this_fruit in list(enumerate(fruit_list)):
    new_list.append(this_fruit[::-1])

fruit_list.pop()

print('Original List:')
print(fruit_list)
print()

print('New List:')
print(new_list)
print()
