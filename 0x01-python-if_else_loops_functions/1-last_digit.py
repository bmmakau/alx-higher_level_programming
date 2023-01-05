#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_string = str(number)[-1]
if number > 0:
    if int(last_string) > 5:
        stmt = "Last digit of {} is {} and is greater than 5"
        print(stmt.format(number, last_string,))
    elif int(last_string) == 0:
        stmt = "Last digit of {} is {} and is 0"
        print(stmt.format(number, last_string,))
    else:
        stmt = "Last digit of {} is {} and is less than 6 and not 0"
        print(stmt.format(number, last_string,))
elif number == 0:
    stmt = "Last digit of {} is {} and is 0"
    print(stmt.format(number, last_string,))
else:
    last_string = int(last_string) * -1
    stmt = "Last digit of {} is {} and is less than 6 and not 0"
    print(stmt.format(number, last_string,))
