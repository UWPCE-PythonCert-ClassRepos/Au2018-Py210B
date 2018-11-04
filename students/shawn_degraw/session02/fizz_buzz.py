#fizz buzz function
for i in range(1,101):
    result3 = i % 3
    result5 = i % 5
    if result3 == 0 and result5 == 0:
        print("FizzBuzz")
    elif result5 == 0:
        print("Buzz")
    elif result3 == 0:
        print("Fizz")
    else:
        print(i)
