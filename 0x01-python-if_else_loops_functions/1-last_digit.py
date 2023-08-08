#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
decrement = -10 if number < 0 else 10
lastdigit = number % decrement

if (lastdigit > 5):
    relation = "greater than 5"
elif (lastdigit < 6 and number != 0):
    relation = "less than 6 and not 0"
else:
    relation = "0"
print(f"Last digit of {number} is {lastdigit} and is {relation}")
