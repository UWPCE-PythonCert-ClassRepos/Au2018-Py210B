# control the height or how many rows to print
for l in range(2):
    # print the first + sign
    print('+ ', end='')

    # control the length or how many columns to print
    for i in range(2):
        # one iteration looks like: ----+
        print('- '*4,end='')
        print('+ ',end='')

    # print the vertical bars |
    # the number of | should be the same number as - as within above for loop
    for m in range(4):
        print()
        print('| ',end='')
        for i in range(2):
            print('  '*4,end='')
            print('| ', end='')
    print()

# print the last line of pattern +----+----+
print('+ ', end='')
for i in range(2):
    print('- '*4,end='')
    print('+ ',end='')
