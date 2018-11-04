def grid(x,y):
    for k in range(x):
        for j in range(y+1):
            if j == 0:
                print("+", end="")
                for i in range(x):
                    print(y*"-", end='+')
            else:
                print("|", end="")
                for i in range(x):
                    print(y*" " , end='|')
            print()
    print("+", end="")
    for i in range(x):
        print(y*"-" , end='+')
grid(1,1)