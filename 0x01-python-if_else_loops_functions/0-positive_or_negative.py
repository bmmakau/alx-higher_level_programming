#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0:
    print(number, " is positive\n")
elif number == 0:
    print(number, " is zero\n")
elif number < 0:
    print(number, " is negative\n")
