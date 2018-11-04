int(4.5)

int("345")

bool("")

bool(" ")

" abc ".strip()

0 and 456 # both must be true, otherwise ture and returns last value; once zero is evaluated it stops; called shorcut

0 or 456

1 and 0 and (10/0)

not True

if 1 and 2: # 1 is evaluated first and 2 is returned a bool()

if x is False:
    return y


x,y = 0,1
x or y

# above will produce different results than below

def my_or(x,y):
    if x is False:
        return y
    else:
        return x

my_or(0,1)


lst = [1,2,3]
lst[0]

tup = ([1,2,3],4,"abc")
tup[0].append(4)
print(tup)

l = [1,2,3]
l.append(4)
l

l.extend([5,6]) # pythonic: adding values to list
l

l = l + [7,8] # less efficient than above; creates a volatile list
l

l.insert(0,123) # adds to specific index in list; first argument is location, second argument is value
l

# O^n run time is proportional to list

l = ['a', 'b', 'c']
list(enumerate(l)) # generates indexes from list

'Hello' + 'J' + '!' # Do not use

'Hello {}!'.format('J') # Use this instead

