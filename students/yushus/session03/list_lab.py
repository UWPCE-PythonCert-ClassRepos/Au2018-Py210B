def series_1():
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print('Initial fruit list:')
    print(fruits)

    new_fruit = input('Please enter your favorite fruit: ')
    fruits.append(new_fruit.strip())
    print('The new fruit list with your favorite one included at last:')
    print(fruits)

    num = input('Please tell me what fruit you like the most, use a number: ')
    index = int(num.strip())-1
    if 0 <= index < len(fruits):
        print('Wow, your favorite fruit is {num} {fruit}'.format(num=num, fruit=fruits[index]))
    else:
        print("Fruit not in the list. Sorry...")

    add_fruit = ['kiwi']
    fruits = add_fruit + fruits
    print('A new secret fruit just got added in front: ') 
    print('Here is all the fruits now:') 
    print(fruits)

    insertFront_fruit = 'dragonfruit'
    fruits.insert(0,insertFront_fruit)
    print('Another secret fruit got added in front: ')
    print(fruits)

    print('Fruits start with \'P\': ')
    for i in fruits:
        if i.startswith('P'):
            print(i)

def series_2():
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print(fruits)

    fruits.remove(fruits[-1])
    print(fruits)

    fruit_to_delete = input("Please choose a fruit to delete: ")
    fruits_copy = fruits[:]
    for f in fruits:
        if f.lower() == fruit_to_delete.strip().lower():
            fruits_copy.remove(f)
    print(fruits_copy)

    new_fruits = fruits*2
    new_fruits_copy = new_fruits[:]
    found = False
    while not found:
        fruit_to_delete = input("Please try again: ").strip()
        for f in new_fruits:
            if f.lower() == fruit_to_delete.lower():
                new_fruits_copy.remove(f)
                found = True
    print(new_fruits_copy)

def series_3():
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    fruits = [f.lower() for f in fruits]

    keep = []
    for fruit in fruits:
        while True:
            ans = input(f'Do you like {fruit}? Please enter "yes" or "no" ').strip().lower()
            if ans.lower() == 'yes':
                keep.append(fruit)
                break
            elif ans.lower() == 'no':
                break
    print(keep)

def series_4():
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    fruits_copy = fruits[:]
    fruits_copy = [f[::-1] for f in fruits_copy ]
    fruits.remove(fruits[-1])
    
    print(fruits)
    print(fruits_copy)
    
series_1()
series_2()
series_3()
series_4()