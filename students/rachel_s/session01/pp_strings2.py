# Given a string, return a string where for every char in the original, there 
# are two chars.
def double_char(str):
    newstring = ''
    for i in str:
        newstring = newstring + i + i
    return newstring


# Return the number of times that the string "hi" appears anywhere in the given 
# string.
def count_hi(str):
    count = 0
    for i in range(len(str) - 1):
        if(str[i:i+2] == "hi"):
            count += 1
    return count


# Return True if the string "cat" and "dog" appear the same number of times in 
# the given string.
def cat_dog(str):
    count_cat = 0
    count_dog = 0
    for i in range(len(str) - 1):
        trigram = str[i:i+3]
        if(trigram == "cat"):
            count_cat += 1
        elif(trigram == "dog"):
            count_dog += 1
    return count_cat == count_dog


# Return the number of times that the string "code" appears anywhere in the 
# given string, except we'll accept any letter for the 'd', so "cope" and 
# "cooe" count.
def count_code(str):
    count = 0
    for i in range(len(str) - 3):
        quad = str[i:i+4]
        if(quad[:2] == "co" and quad[3] == "e"):
            count += 1
    return count


# Given two strings, return True if either of the strings appears at the very 
# end of the other string, ignoring upper/lower case differences (in other 
# words, the computation should not be "case sensitive"). Note: s.lower() 
# returns the lowercase version of a string.
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if len(a) > len(b):
        return b == a[-len(b):]
    else:
        return a == b[-len(a):]


# Return True if the given string contains an appearance of "xyz" where the xyz 
# is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does 
# not.
def xyz_there(str):
    for i in range(len(str) - 2):
        if str[i:i+3] == "xyz":
            if i == 0:
                return True
            elif str[i-1] != ".":
                return True
    return False