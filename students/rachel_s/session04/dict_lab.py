#!/usr/bin/env python3

# DICTIONARIES 1
# Create a dictionary containing “name”, “city”, and “cake” for “Chris” from 
# “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and 
# values: “Chris”, etc.)

d = {"name": "Chris", "city": "Seattle", "cake": "chocolate"}

# Display the dictionary.
d

# Delete the entry for “cake”.
d.pop("cake")

# Display the dictionary.
d

# Add an entry for “fruit” with “Mango” and display the dictionary.
d["fruit"] = "Mango"

# Display the dictionary keys.
d.keys()

# Display the dictionary values.
d.values()

# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
"cake" in d

# Display whether or not “Mango” is a value in the dictionary (i.e. True).
"Mango" in d.values()


# Using the dictionary from item 1: Make a dictionary using the same keys but 
# with the number of ‘t’s in each value as the value (consider upper and lower 
# case?).
d2 = {}

for key, value in d.items():
    d2[key] = value.lower().count("t")

d2


# SETS 1
# Create sets s2, s3 and s4 that contain numbers from zero through twenty, 
# divisible by 2, 3 and 4.
s2 = set(range(0, 21, 2))
s3 = set(range(0, 21, 3))
s4 = set(range(0, 21, 4))

# Display the sets.
s2
s3
s4

# Display if s3 is a subset of s2 (False)
s3.issubset(s2)

# and if s4 is a subset of s2 (True).
s4.issubset(s2)

# SETS 2
# Create a set with the letters in ‘Python’ and add ‘i’ to the set.
pythoni = set(list("python"))
pythoni.add("i")

# Create a frozenset with the letters in ‘marathon’.
marathon = frozenset(list("marathon"))

# display the union and intersection of the two sets.
marathon.union(pythoni)
pythoni.intersection(marathon)
