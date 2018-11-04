def print_grid1(n):
    """
    n determines the size of the grid
    the formula is size = n // 2 (integer division)
    """
    unit = n // 2
    # control the height or how many rows to print
    for l in range(2):
        # print the first + sign
        print('+ ', end='')

        # control the length or how many columns to print
        for i in range(2):
            # one iteration looks like: ----+
            print('- '*unit,end='')
            print('+ ',end='')

        # print the vertical bars |
        # the number of | should be the same number as - as within above for loop
        for a in range(unit):
            print()
            print('| ',end='')
            for i in range(2):
                print('  '*unit,end='')
                print('| ', end='')
        print()

    # print the last line of pattern +----+----+
    print('+ ', end='')
    for b in range(2):
        print('- '*unit,end='')
        print('+ ',end='')

print_grid1(15)