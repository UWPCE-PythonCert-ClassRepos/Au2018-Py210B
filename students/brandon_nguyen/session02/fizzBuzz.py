#!/usr/bin/env python3
#Fizz Buzz problem - Week 2 Excercise 1
#Student: Brandon Nguyen - Au2018
for i in range(1,101):
    if (i%3 ==0 and i%5 == 0):
        print('FizzBuzz')
    elif (i%3 == 0):
        print('Fizz')
    elif (i%5 == 0):
        print('Buzz')
    else:
        print(i)