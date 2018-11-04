def print_grid2(n,m):
    """ n is the size of the row and column; m is the unit of each grid """

    # control the height or how many rows to print
    for l in range(n):
        # print the first + sign
        print('+ ', end='')

        # control the length or how many columns to print
        for i in range(n):
            # one iteration looks like: ----+
            print('- '*m,end='')
            print('+ ',end='')

        # print the vertical bars |
        # the number of | should be the same number as - as within above for loop
        for a in range(m):
            print()
            print('| ',end='')
            for i in range(n):
                print('  '*m,end='')
                print('| ', end='')
        print()

    # print the last line of pattern +----+----+
    print('+ ', end='')
    for b in range(n):
        print('- '*m,end='')
        print('+ ',end='')

print_grid2(5,4)