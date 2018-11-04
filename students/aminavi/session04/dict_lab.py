#!/usr/bin/env python3

d = {'name': 'Chris','City': 'Seattle', 'Cake': 'Chocolate'}
d
d.pop('Cake')
d
d['fruit'] = 'Mango'
d
d.values()
'cake' in d
'Mango' in d.values()

d2 = {}
for k,v in d.items():
    d2[k] = v.lower().count('t')
d2



s2 =  set()
s3 =  set()
s4 =  set()

for i in range(0,21):
    if i % 2 == 0:
        s2.add(i)
    if i % 3 == 0:
        s3.add(i)
    if i % 4 == 0:
        s4.add(i)
s2
s3
s4
s3.issubset(s2)
s4.issubset(s2)


s5 = set('Python')
s5.update
s5.update(['i'])

fs = frozenset('marathon')

s5.union(fs)``
s5.intersection(fs)