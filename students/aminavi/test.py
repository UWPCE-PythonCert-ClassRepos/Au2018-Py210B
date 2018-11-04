'  abc  '.strip()

if x =='abc':
    print(x)

if 1 and 2:


x,y = 0,1
x or y 

def my_or(x,y):
    if x == False:
        return y
    else:
        return x
my_or(0,1)

tup = (1,2,3)
tup[0]


tup([1,2,3],4,'acy')
tup[0] = [1,2,3,4]
tup[0].append(4)
print(tup)



l = [1,2,3]
l.append(4)
l

l = [1,2,3]
l.extend([12,11,10])
l

l = [1,2,3]
l = l + [4,5,6]
l

l = [1,2,3]
l.insert(0,123)
l


for x in range(10):
    if x == 5:
        break
    else :
        print('finished')


it_did_break = False
for x in range(9):
    if x == 11:
        it_did_break = True
        break
if not it_did_break:
    print('finished')


for x in range(100):
    print(x)

for x in range(1,101):
    print(x)

a = ['apple', 'banana']
a =[y[::-1] for y in a]
print(a)

# '{:^10}{:^10}{:^10}{:^10}'.format('First', '$99.01', 'Second', '$88.09')

