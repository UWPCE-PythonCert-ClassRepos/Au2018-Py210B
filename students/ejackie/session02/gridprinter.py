def print_grid(n):
    print('+', end='')
    print(' -'*n, end=' +')
    print(' -'*n, end=' +')
    print()
    print('|', end='')
    print('  '*n, end=' |')
    print('  '*n, end=' |')
    print()
    print('|', end='')
    print('  '*n, end=' |')
    print('  '*n, end=' |')
    print()
    print('+', end='')
    print(' -'*n, end=' +')
    print(' -'*n, end=' +')
    print()
    print('|', end='')
    print('  '*n, end=' |')
    print('  '*n, end=' |')
    print()
    print('|', end='')
    print('  '*n, end=' |')
    print('  '*n, end=' |')
    print()
    print('+', end='')
    print(' -'*n, end=' +')
    print(' -'*n, end=' +')
    print()

print_grid(2)

# print grid with d=dimension and s=size
def print_grid2(d, s):
    for i in range(d):
        # each row starts with '+'
        print('+', end='')
        for i in range(d):
            # draw each column width according to size
            print(' -'*s,'+', end='')
        for i in range(s):
            # each new row start with '|'
            print()
            print('|', end='')
            for i in range(d):
                # draw each row height according to size
                print('  '*s, end=' |')
        print()
    # draw the bottom line to close the grid
    print('+', end='')
    for i in range(d):
        print(' -'*s,'+', end='')

print_grid2(3,3)
