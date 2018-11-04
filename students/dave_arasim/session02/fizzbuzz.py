#Fizz Buzz Exercise for Lesson 2

for x in range(1,101):
    if not(x%3) and not(x%5):
        print('FizzBuzz')
    elif not(x%3):
        print('Fizz')
    elif not(x%5):
        print('Buzz')
    else:
        print(x)
