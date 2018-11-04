def print_grid2(x,y):

    plus = (("+" + "-"*y) * x) + "+"
    pipe = (("|" + " "*y) * x) + "|"

    for row in range((y * x) + x + 1):
        if row%(y + 1) == 0:
            print(plus)
        else:
            print(pipe)

print_grid2(5,3)