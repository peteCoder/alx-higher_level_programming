#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = number % 10
print("Last digit of", end=" ")
print("is", end=" ")

if last_digit > 5:
    print(f"{number} and is greater than 5", end="\n")
elif last_digit == 0:
    print(f"{number} and is 0", end="\n")
elif last_digit < 6 and last_digit != 0:
    print(f"{number} and is less than 6 and not 0", end="\n")
