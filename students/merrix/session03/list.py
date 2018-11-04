#!/usr/bin/env python3

ls = ["Apples", "Pears", "Oranges", "Peaches"]
response = input("Please enter a fruit to add to the list: ")
if response == (" "):
    ls.append(response)
print (ls)

ls2 = ls
response2 = int(input("enter a number to find the corresponding fruti"))
pos = ls2[response2]
print (pos)
