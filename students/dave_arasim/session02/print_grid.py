''' Grid printing exercise.  Showing simple 'four-square' grid and
    configurable multi-square grid. 
    Written by David K. Arasim, 10/15/18 '''

#Functions section

def print_grid1(grid_size):
    #Single-parameter function to print basic 'four-square' grid.
    #Parameter indcates square size >= 2, where 2 is minimum square size.
    grid_corner = '+'
    grid_horiz  = '-'
    grid_vert   = '|'
    grid_space  = ' '
    grid_min    = 2

    if grid_size < grid_min:
        print('Invalid square size (minimum 2)')
        return

    grid_len = grid_size - grid_min  #Length of each square side, minus corners

    print_grid_border1(grid_corner, grid_horiz, grid_len)
    print_grid_center1(grid_vert, grid_space, grid_len)
    print_grid_border1(grid_corner, grid_horiz, grid_len)
    print_grid_center1(grid_vert, grid_space, grid_len)
    print_grid_border1(grid_corner, grid_horiz, grid_len)
	
def print_grid_border1(grid_corner, grid_horiz, grid_len): 
    print(grid_corner, end='') #Left corner
    print(grid_horiz*grid_len, sep='', end='')
    print(grid_corner, end='') #Center separator
    print(grid_horiz*grid_len, sep='', end='')
    print(grid_corner, end='') #Right corner
    print()                    #New line

def print_grid_center1(grid_vert, grid_space, grid_len): 
    if grid_len > 0:
        for grid_ct in range(grid_len):
            print(grid_vert, grid_space*grid_len, grid_vert, grid_space*grid_len, grid_vert, sep='')

def print_grid2(grid_size, square_ct):
    #Double-parameter function to print multi-square grid.
    #Parameter 1 indicates square size >= 2, where 2 is minimum square size.
    #Parameter 2 indicates square count >= 1, where 1 is minimum square count for x/y dimensions.
    grid_corner = '+'
    grid_horiz  = '-'
    grid_vert   = '|'
    grid_space  = ' '
    grid_min    = 2
    square_min  = 1

    if grid_size < grid_min:
        print('Invalid square size (minimum 2)')
        return

    if square_ct < square_min:
        print('Invalid square count (minimum 1)')
        return

    grid_len = grid_size - grid_min  #Length of each square side, minus corners

    print_grid_border2(grid_corner, grid_horiz, grid_len, square_ct)  #Top border (always printed)

    for this_square in range(square_ct):
        print_grid_center2(grid_vert, grid_space, grid_len, square_ct)
        print_grid_border2(grid_corner, grid_horiz, grid_len, square_ct)

def print_grid_border2(grid_corner, grid_horiz, grid_len, square_ct): 
    print(grid_corner, end='')     #Left corner (always printed)

    for this_square in range(square_ct):
        print(grid_horiz*grid_len, sep='', end='')
        print(grid_corner, end='') #Corner/Separator
    print()                        #New line

def print_grid_center2(grid_vert, grid_space, grid_len, square_ct): 
    if grid_len > 0:
        for grid_ct in range(grid_len):
            print(grid_vert, end='')       #Left side (always printed)

            for this_square in range(square_ct):
                print(grid_space*grid_len, end='')
                print(grid_vert, end='')
            print()                        #New line

##################################################################################	
#User interfaces for functions

#Basic 'four-square' grid.
print('Enter square size (>= 2): ', end = '')
grid_size = int(input())
print_grid1(grid_size)
print()

#Multi-square grid.
print('Enter square size (>= 2): ', end = '')
grid_size = int(input())
print('Enter square count for x/y dimensions (>= 1): ', end='')
square_size = int(input())
print_grid2(grid_size, square_size)
