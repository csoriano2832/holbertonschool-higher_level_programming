#!/usr/bin/python3
for number in range(1, 101):
    if number != 100:
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=" ")
        elif number % 3 == 0:
            print("Fizz", end=" ")
        elif number % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{:d}".format(number), end=" ")
        else:
            print("Buzz")