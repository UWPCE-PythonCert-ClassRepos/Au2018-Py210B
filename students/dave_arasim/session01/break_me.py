#practice python programming
#break_me.py for task 1: Explore errors

import datetime

def myfunc(x):
    x += 1
    return x

#y = myfunk(1)  #This shows NameError because 'myfunc' is misspelled as 'myfunk'
y = myfunc(1)   #Here is previous line now corrected to myfunc()

#print("Adding 1 to 1 is: " + y)  #This shows TypeError because can't concatenate string and int types in print()
print("Adding 1 to 1 is: ", y)    #Here is previous line now corrected to use "," concatenation instead

#print("Oops!')  #This shows SyntaxError because the string delimiters don't match (" vs ')
print("Oops!")   #Here is previous line with delimiters matching to use "

#print (datetime.datetim.now())  #This shows AttibuteError because attribute 'datetim' doesn't exist 
print (datetime.datetime.now())  #Here is previous line with 'datetime' instead