def print_grid_arbitrary():
    """Prints a grid of arbitrary size."""
    print("+ - - - + - - - + - - - +")
    for i in range(3):
        print("|       |       |       |")
    print("+ - - - + - - - + - - - +")
    for i in range(3):
        print("|       |       |       |")
    print("+ - - - + - - - + - - - +")
    for i in range(3):
        print("|       |       |       |")
    print("+ - - - + - - - + - - - +")


def print_grid(n):
    """Prints a grid of width and height n that is 2 cells high and wide."""
    width = n // 2
    # Print top border
    print("+", end=" ")
    for i in range(width):
        print("-", end=" ")
    print("+", end=" ")
    for i in range(width):
        print("-", end=" ")
    print("+")
    # Print inside of cells
    for j in range(width):
        print("|", end=" ")
        for i in range(width):
            print(" ", end=" ")
        print("|", end=" ")
        for i in range(width):
            print(" ", end=" ")
        print("|")
    # Print middle line
    print("+", end=" ")
    for i in range(width):
        print("-", end=" ")
    print("+", end=" ")
    for i in range(width):
        print("-", end=" ")
    print("+")
    # Print bottom insides of cells
    for j in range(width):
        print("|", end=" ")
        for i in range(width):
            print(" ", end=" ")
        print("|", end=" ")
        for i in range(width):
            print(" ", end=" ")
        print("|")
    # Print bottom line
    print("+", end=" ")
    for i in range(width):
        print("-", end=" ")
    print("+", end=" ")
    for i in range(width):
        print("-", end=" ")
    print("+")


def print_grid2(grid_size, cell_size):
    """Print a grid of a specified length and cell size

    Keyword arguments:
    grid_size: indicates the number of cells in the grid
    cell_size: indicates the size of the cell"""
    if grid_size < 1 or cell_size < 1:
        print("Please make grid and cell sizes 1 or greater.")
    else:
        for a in range(grid_size):
            grid_edge(grid_size, cell_size)
            for b in range(cell_size):
                grid_inside(grid_size, cell_size)
        grid_edge(grid_size, cell_size)


def grid_edge(grid_size, cell_size):
    """Prints the upper or lower horizontal edge of a grid row
    
    Keyword arguments:
    grid_size: indicates the number of cells in the grid
    cell_size: indicates the size of the cell"""
    for a in range(grid_size):
        print("+", end=" ")
        for b in range(cell_size):
            print("-", end=" ")
    print("+")


def grid_inside(grid_size, cell_size):
    """Prints the internal part of a grid row, the bit with just vertical lines

    Keyword arguments:
    grid_size indicates the number of cells in the grid
    cell_size indicates the size of the cell"""
    for a in range(grid_size):
        print("|", end=" ")
        for b in range(cell_size):
            print(" ", end=" ")
    print("|")