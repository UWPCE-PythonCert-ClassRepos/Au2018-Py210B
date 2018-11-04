#!/usr/bin/env python3

"""Dict1 Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
Display the dictionary.
Delete the entry for “cake”.
Display the dictionary.
Add an entry for “fruit” with “Mango” and display the dictionary.
Display the dictionary keys.
Display the dictionary values.
Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
Display whether or not “Mango” is a value in the dictionary (i.e. True)."""

dict1 = {"name":"Chris","city":"Seattle","cake":"chocolate"}
print(dict1)
a = dict1.pop("cake")
#pop value, dict1 is modified
print(dict1)
print(a)
print(type(a))

dict1["fruit"] = "Mango"
print(dict1)

print(dict1.keys())

print(dict1.values())

print(dict1.get("cake","doesn't exist"))

for x, y in dict1.items():
    if y == "Mango":
        print("{} is a value in dict".format(y))
    else:
        pass

#how to enable autocomplete????

"""Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value as the value (consider upper and lower case?)"""

dict2 = {}
for x, y in dict1.items():
    dict2[x] = y.count["t"]

print(dict2)


"""Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
Display the sets.
Display if s3 is a subset of s2 (False)
and if s4 is a subset of s2 (True)"""

s2 = set()
s3 = set()
s4 = set()

for i in range(0,21):
    if i%2 == 0:
        s2.update([i])
    if i%3 == 0:
        s3.update([i])
    if i%4 == 0:
        s4.add(i)
    else:
        pass

print("\n",s2,"\n",s3,"\n",s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

"""Create a set with the letters in ‘Python’ and add ‘i’ to the set.
Create a frozenset with the letters in ‘marathon’.
display the union and intersection of the two sets."""

sa = set("Python")
sa.update("i")
print(sa)

sb = frozenset("marathon")
print(sb)

print(sa.union(sb))
print(sa.intersection(sb))


