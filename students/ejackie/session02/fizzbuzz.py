# numbers between 1 to 100 inclusive
for n in range(1,101):
    # check if multiples of 3 and 5
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    # check if multiples of 3
    elif n % 3 == 0:
        print("Fizz")
    # check if multiples of 5
    elif n % 5 == 0:
        print("Buzz")
    # print the rest of numbers
    else:
        print(n)
