
lst = (2, 123.4567, 10000, 12345.67)

# Task One
'file_{:0>3d} :    {:.2f}, {:.2e}, {:.2e}'.format(*lst)

# Task Two
f'file_{lst[0]:03} :    {lst[1]:.2f}, {lst[2]:.2e}, {lst[3]:.2e}'

seq = (1.1,2,3,4,5)
# Task Three
def formatter(in_tuple):
    l = len(in_tuple)
    return ('the {} numbers are: ' + ', '.join(['{}'] * l)).format(l, *in_tuple)
print(formatter(seq))

# Task Four
seq4 = [4,30,2017,2,27]
'{4:0>2d} {3:0>2d} {2:0>2d} {0:0>2d} {1:0>2d}'.format(*seq4)

# Task Five
object1 ='oranges'
weight_object1 = 1.3
object2 = 'lemons'
weight_object2 = 1.1
f"The weight of an {object1} is {weight_object1} and the weight of a {object2} is {weight_object2}"

# Task Six
table = [['alex', 125, 100],['amir', 22, 100000],['jack', 36, 55555],['jason', 32, 888999.99]]
print('{:^10}|{:^5}|{:^10}'.format('Name','Age','Cost'))
for i in table:
     print('{:^10}|{:^5}|${:.2f}'.format(i[0], i[1], i[2]))

# Task Six.Two
tuple6 = [10,13,14,15,16,18,23,36,78,100]
print (' '.join(['{: >5d}'.format(x) for x in tuple6]))





