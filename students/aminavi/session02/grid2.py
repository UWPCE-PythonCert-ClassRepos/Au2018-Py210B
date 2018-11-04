def grid(x):
    for i in range(x*2 + 3):
        if i%(x + 1)==0:
            print("+" + "-"*x + "+" + "-"*x + "+")
        else:
            print("|" + " "*x + "|" + " "*x + "|")
grid(10)