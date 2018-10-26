#!/usr/bin/env python3
# Declare the "fruits" variable to be globally accessible
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

# Series 1
def series_1():
    global fruits

    print(fruits)
    print()

    fruit_to_add = input('Add another fruit to this list >')
    print()

    if fruit_to_add != '':
        fruits.append(fruit_to_add.capitalize())

    print(fruits)
    print()

    fruit_number = input('Which fruit would you like to see? Enter a number between 1 - 5 >')
    print()
    fruit_to_see = fruits[int(fruit_number) -1]
    print(f'Fruit number {fruit_number} is "{fruit_to_see}"')
    print()

    print(10*'-', 'Adding "Plum" to the beginning of the list', 10*'-')
    fruits = ["Plum"] + fruits
    print(fruits)
    print()

    print(10*'-', 'Inserting "Lemons" to the beginning of the list', 10*'-')
    fruits.insert(1, 'Lemons')
    print(fruits)
    print()

    print(10*'-', 'Printing all fruit names that begin with "P"', 10*'-')
    for fruit in fruits:
        if( fruit[0] == 'P' ):
            print(fruit)
    print()


# Series 2
def series_2():
    global fruits
    
    print(fruits)
    print()

    del fruits[-1]
    print(10*'-', 'Last item removed. Here\'s the new list:', 10*'-')
    print(fruits)
    print()

    print(10*'-', 'Doubling our list', 10*'-')
    fruits = fruits * 2
    print(fruits)
    print()

    fruit_to_remove = input('Type the name of a fruit you\'d like to remove from our list >')
    if( fruit_to_remove.capitalize() in fruits):
        fruits.remove(fruit_to_remove.capitalize())
    print()
    print(10*'-', f'"{fruit_to_remove.capitalize()}" removed. Here\'s the new list:', 10*'-')
    print(fruits)
    print()


# Series 3
def series_3():
    global fruits
    for fruit in fruits[:]:
        response = False
        while not(response):
            yes_no = input(f'Do you like {fruit.lower()}? >')
            if yes_no.capitalize() == 'No':
                response = True
                fruits.remove(fruit)
                break
            elif yes_no.capitalize() == 'Yes':
                response = True
                break
            else:
                print('Please enter yes or no')
            print()
    print(10*'-', 'Ok, here are the fruits you do like:', 10*'-')
    print()
    print(fruits)
    print()


# Series 4
def series_4():
    global fruits
    new_list= fruits.copy()

    for i in range(len(new_list)):
        new_list[i] = new_list[i][::-1]

    print(10*'-', 'Made a clone of the original fruits list. Now reversing the spelling of each fruit name:', 10*'-')
    print(new_list)
    print()

    print(10*'-', 'Here\'s the original list, with the last item removed:', 10*'-')
    del fruits[-1]
    print(fruits)
    print()

    print(10*'-', 'Here\'s the the new, reversed list:', 10*'-')
    print(new_list)
    print()


# Call all 3 methods
series_1()
series_2()
series_3()
series_4()
