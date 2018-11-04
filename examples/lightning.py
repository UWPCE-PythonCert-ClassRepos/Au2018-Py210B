import random
import datetime

names = '''
Last1	First1
Last2	First2
Last3	First3
Last4	First4 M
Last5	First5
Last6	First6
Last7	First7
Last8	First8
Last9	First9
Last10	First10 M
Last11	First11 M
Last12	First12 Middle
Last13	First13
Last14	First14 M
'''

names = [name for name in names.split('\n') if name]
random.shuffle(names)

date = datetime.date.today()

print("Here's the order of Authum 2018 PYTHON210B lightning talks! (two students every week):")
print()
for i, name in enumerate(names, 1):
    if i % 2 == 1:
        date += datetime.timedelta(days=7)
    if date == datetime.date(2018, 11, 21): # Thanksgiving 2018
        date += datetime.timedelta(days=7)
    name_parts = name.split('\t')
    print('{:2}. ({}) {} {}'.format(i, date, name_parts[1], name_parts[0]))
