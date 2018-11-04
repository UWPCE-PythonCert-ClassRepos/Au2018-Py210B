

for i in range(1,101):
    """This scripy prints the numbers from 1 to 100 inclusive.
    But for multiples of three print “Fizz” instead of the number.
    For the multiples of five print “Buzz” instead of the number.
    For numbers which are multiples of both three and five print “FizzBuzz” instead."""
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)