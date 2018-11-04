
def print_function1():
    """homework2 #1, print a grid as shown in homework"""
    print("+ - - - - + - - - - +")
    for i in range(4):
        print("|         |         |")
    print("+ - - - - + - - - - +")
    for i in range(4):
        print("|         |         |")
    print("+ - - - - + - - - - +")
    return



def print_grid(n):
    """make the print grid function more general.
    This is a function print_grid(n) that takes one integer argument and prints a grid just like before,
    BUT the size of the grid is given by the argument,which is n"""
    for x in range(n+2):

        if x == 0:
            for i in range(n+2):
                if i == 0:
                    print("+", end=" ")
                elif i == (n+2)//2:
                    print("+", end=" ")
                elif i == n+1:
                    print("+", end=" ")
                else:
                    print("-", end=" ")
            print()
        
        elif x == (n+2)//2:
            for i in range(n+2):
                if i == 0:
                    print("+", end=" ")
                elif i == (n+2)//2:
                    print("+", end=" ")
                elif i == n+1:
                    print("+", end=" ")
                else:
                    print("-", end=" ")
            print()

        elif x == n+1:
            for i in range(n+2):
                if i == 0:
                    print("+", end=" ")
                elif i == (n+2)//2:
                    print("+", end=" ")
                elif i == n+1:
                    print("+", end=" ")
                else:
                    print("-", end=" ")
            print()
        
        else:
            for i in range(n+2):
                if i == 0:
                    print("|", end=" ")
                elif i == (n+2)//2:
                    print("|", end=" ")
                elif i == n+1:
                    print("|", end=" ")
                else:
                    print(" ", end=" ")
            print()
       


def print_grid2(a,b):
    """This function can print a grid with a specified number of rows and columns, and with each cell a given size. 
    a is the number of rows and columns. b is the size of each cell"""
    row_1 = ("+ " + b*"- ")*a + "+ "
    row_2 = ("| " + b*"  ")*a + "| "
    for i in range(a):
        print(row_1)
        for i in range(b):
            print(row_2)
    
    print(row_1)


# Below is just for testing
print_function1()
print_grid(3)
print_grid2(3,4)