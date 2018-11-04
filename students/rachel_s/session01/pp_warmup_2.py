# Given a string and a non-negative int n, return a larger string that is n 
# copies of the original string
def string_times(str, n):
    newstr = ''
    for i in range(n):
        newstr += str
    return newstr


# Given a string and a non-negative int n, we'll say that the front of the 
# string is the first 3 chars, or whatever is there if the string is less than 
# length 3. Return n copies of the front;
def front_times(str, n):
    newstr = ''
    if(len(str) <= 3):
        front = str
    else:
        front = str[:3]
    for i in range(n):
        newstr += front
    return newstr


# Given a string, return a new string made of every other char starting with 
# the first, so "Hello" yields "Hlo".
def string_bits(str):
    newstr = ''
    for i in range(len(str)):
        if(i % 2 == 0):
            newstr += str[i]
    return newstr


# Given a non-empty string like "Code" return a string like "CCoCodCode"
def string_splosion(str):
    newstr = ''
    for i in range(len(str)):
        newstr += str[:i]
    return newstr + str


# Given a string, return the count of the number of times that a substring 
# length 2 appears in the string and also as the last 2 chars of the string, so 
# "hixxxhi" yields 1 (we won't count the end substring).
def last2(str):
    count = 0
    if len(str) > 1:
        count = -1
        last = str[-2:]
        for i in range(len(str)):
            bigram = str[i:i + 2]
            if(bigram == last):
                count += 1
    return count


# Given an array of ints, return the number of 9's in the array.
def array_count9(nums):
    count = 0
    for i in nums:
        if i == 9:
            count += 1
    return count


# Given an array of ints, return True if one of the first 4 elements in the 
# array is a 9. The array length may be less than 4.
def array_front9(nums):
    has9 = False
    if(len(nums) > 4):
        front = nums[:4]
    else:
        front = nums
    for i in front:
        if i == 9:
            return True
    return False


# Given an array of ints, return True if the sequence of numbers 1, 2, 3 
# appears in the array somewhere.
def array123(nums):
    for i in range(len(nums)):
        trigram = nums[i:i + 3]
        if(trigram == [1, 2, 3]):
            return True
    return False



# Given 2 strings, a and b, return the number of the positions where they 
# contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, 
# since the "xx", "aa", and "az" substrings appear in the same place in both 
# strings.
def string_match(a, b):
    count = 0
    if(len(a) > len(b)):
        my_len = len(b)
    else:
        my_len = len(a)
    for i in range(my_len - 1):
        if(a[i:i+2] == b[i:i+2]):
            count += 1
    return count


