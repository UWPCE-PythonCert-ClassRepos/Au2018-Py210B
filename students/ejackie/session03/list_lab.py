#!/usr/bin/env python3

##################################################
## Author: Jackie Cheung
## Date: 2018/10/23
## Version: 0.1
## Class: Au2018-Py210B
## Description: List Lab - Booleans, Sequences, Iteration, and Strings
##################################################


print("\n----- Series 1 -----\n")

fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print("The list has the following", len(fruits), "items:", fruits)
newfruit = input("what new fruit should be added to the list? ")
fruits.append(newfruit)
print("The list has the following", len(fruits), "items:", fruits)
num = input("Please enter a number between 1 and ", (len(fruits), ": ")
print("You have entered the number:", num, "which is corresponding to:", fruits[int(num)-1])
print("Adding Cantaloupes to the beginning of the list")
fruits = ["Cantaloupes"] + fruits
print("The list has the following", len(fruits), "items:", fruits)
print("Adding another Pomegranates to the beginning of the list")
fruits.insert(0, "Pomegranates")
print("The list has the following", len(fruits), "items:", fruits)
print("Here is the fruits begin with P:")
for item in fruits:
    if item[0] == "P" or item[0] == "p":
        print(item)


print("\n----- Series 2 -----\n")

print("The list has the following", len(fruits), "items:", fruits)
print("Removing the last item from the list")
del fruits[len(fruits)-1]
print("The list has the following", len(fruits), "items:", fruits)
deletefruit = input("which fruit should be deleted from the list? ")
fruits.remove(deletefruit)
print("The list has the following", len(fruits), "items:", fruits)


print("\n----- Series 3 -----\n")

fruits_iteration = fruits[:]
print("The list has the following", len(fruits), "items:", fruits)
for i, item in enumerate(fruits_iteration):
    fruits[item] = item.lower()
    answer = input("Do you like " + fruits[item] + "? ")
    if(answer == "no"):
        del fruits[item]
print("The list has the following", len(fruits), "items:", fruits)


print("\n----- Series 4 -----\n")

print("The list has the following", len(fruits), "items:", fruits)
fruits_copy = fruits[:]
del fruits[len(fruits)-1]
print("The original list with last item removed:", fruits)
for i, item in enumerate(fruits_copy):
    fruits_copy[i] = item[::-1]
print("The copied list with letters reversed in each fruit:", fruits_copy)