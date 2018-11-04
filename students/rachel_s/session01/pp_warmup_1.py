def sleep_in(weekday, vacation):
    if(vacation or not weekday):
        return True
    else:
        return False


def monkey_trouble(a_smile, b_smile):
    if(a_smile == b_smile):
        return True
    else:
        return False


# Given two int values, return their sum. Unless the two values are the same,
# then return double their sum.
def sum_double(a, b):
    if(a == b):
        return (a + b) * 2
    else:
        return a + b


# Given an int n, return the absolute difference between n and 21, except 
# return double the absolute difference if n is over 21.
def diff21(n):
    if(n > 21):
        return (n - 21) * 2
    else:
        return 21 - n


# We have a loud talking parrot. The "hour" parameter is the current hour time 
# in the range 0..23. We are in trouble if the parrot is talking and the hour 
# is before 7 or after 20. Return True if we are in trouble.
def parrot_trouble(talking, hour):
    time_trouble = hour < 7 or hour > 20
    if(time_trouble and talking):
        return True
    else:
        return False

# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
def makes10(a, b):
    if(a == 10 or b == 10 or (a + b) == 10):
        return True
    else: 
        return False


# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) 
# computes the absolute value of a number.
def near_hundred(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10


# Given 2 int values, return True if one is negative and one is positive. 
# Except if the parameter "negative" is True, then return True only if both are 
# negative.
def pos_neg(a, b, negative):
    a_pos = a >= 0
    b_pos = b >= 0
    if(negative):
        if(not a_pos and not b_pos):
            return True
        else:
            return False
    else:
        return a_pos != b_pos



# Given a string, return a new string where "not " has been added to the front. 
# However, if the string already begins with "not", return the string unchanged.
def not_string(str):
    if(str[0:3] == "not"):
        return str
    else:
        return "not " + str


# Given a non-empty string and an int n, return a new string where the char at 
# index n has been removed. The value of n will be a valid index of a char in 
# the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
def missing_char(str, n):
    if n == 0:
        return str[1:]
    elif n == len(str):
        return str[:n - 2]
    else:
        return str[:n] + str[n + 1:]


# Given a string, return a new string where the first and last chars have been 
# exchanged.
def front_back(str):
    if(len(str) <= 1):
        return str
    else:
        new_str = str[1:-1]
        new_str = str[-1] + new_str + str[0]
        return new_str


# Given a string, we'll say that the front is the first 3 chars of the string. 
# If the string length is less than 3, the front is whatever is there. Return a 
# new string which is 3 copies of the front.
def front3(str):
    if(len(str) >= 3):
        front = str[:3]
        return front + front + front
    else:
        return str + str + str

