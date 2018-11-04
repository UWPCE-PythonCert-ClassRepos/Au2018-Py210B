# We want to make a row of bricks that is goal inches long. We have a number of 
# small bricks (1 inch each) and big bricks (5 inches each). Return True if it 
# is possible to make the goal by choosing from the given bricks. This is a 
# little harder than it looks and can be done without any loops.
def make_bricks(small, big, goal):
    if goal % 5 > small:
        return False
    elif small + (big * 5) < goal:
        return False
    else:
        return True


# Given 3 int values, a b c, return their sum. However, if one of the values is 
# the same as another of the values, it does not count towards the sum.
def lone_sum(a, b, c):
    my_sum = 0
    if a != b:
        my_sum = a + b
    if c != b and c != a:
        my_sum += c
    return my_sum


# Given 3 int values, a b c, return their sum. However, if one of the values is 
# 13 then it does not count towards the sum and values to its right do not 
# count. So for example, if b is 13, then both b and c do not count.
def lucky_sum(a, b, c):
    my_sum = 0
    for i in [a, b, c]:
        if i == 13:
            return my_sum
        else:
            my_sum += i
    return my_sum


# Given 3 int values, a b c, return their sum. However, if any of the values is 
# a teen -- in the range 13..19 inclusive -- then that value counts as 0, 
# except 15 and 16 do not count as a teens. Write a separate helper "def 
# fix_teen(n):"that takes in an int value and returns that value fixed for the 
# teen rule. In this way, you avoid repeating the teen code 3 times (i.e. 
# "decomposition"). Define the helper below and at the same indent level as the 
# main no_teen_sum().
def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(num):
    if num in range(13, 20):
        if num == 15 or num == 16:
            return num
        else:
            return 0
    else:
        return num


# For this problem, we'll round an int value up to the next multiple of 10 if 
# its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round 
# down to the previous multiple of 10 if its rightmost digit is less than 5, so 
# 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded 
# values. To avoid code repetition, write a separate helper "def round10(num):" 
# and call it 3 times. Write the helper entirely below and at the same indent 
# level as round_sum().
def round10(num):
    num_string = str(num)
    if len(num_string) == 1:
        if num >= 5:
            return 10
        else:
            return 0
    elif int(num_string[-1]) >= 5:
        return (int(num_string[:-1]) + 1) * 10
    else:
        return int(num_string[:-1]) * 10

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


# Given three ints, a b c, return True if one of b or c is "close" (differing 
# from a by at most 1), while the other is "far", differing from both other 
# values by 2 or more. Note: abs(num) computes the absolute value of a number.
def close(x, y):
    if abs(x - y) >= 1:
        return True
    else:
        return False

def far(a, b, c):
    if abs(a - b) < 2:
        return False
    elif abs(b - c) < 2:
        return False
    else:
        return True

def close_far(a, b, c):
    dists = {"close": False, "far": False}
    if close(a, b) or close(a, c):
        dists["close"] = True
    if far(a, b, c) or far(a, c, b):
        dists["far"] = True
    return dists["close"] and dists["far"]


# We want make a package of goal kilos of chocolate. We have small bars (1 kilo 
# each) and big bars (5 kilos each). Return the number of small bars to use, 
# assuming we always use big bars before small bars. Return -1 if it can't be 
# done.
def make_chocolate(small, big, goal):
    if (big * 5) + small < goal:
        return -1
    elif goal % 5 > small:
        return -1
    else:
        if goal // 5 <= big:
            return goal % 5
        else:
            goal -= big * 5
            if goal > small:
                return -1
            else:
                return goal
