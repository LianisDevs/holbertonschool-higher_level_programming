#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

def get_last_digit_with_sign(number):
    if number >= 0:
            return number % 10
    else:
            return -(abs(number) % 10)

lastDigit = get_last_digit_with_sign(number);

if number < 0 and lastDigit!= 0:
    print(f"Last digit of", number, "is",lastDigit, "and is less than 6 and not 0")
elif number > 0 and lastDigit > 5:
    print("Last digit of", number, "is",lastDigit, "and is greater than 5")
elif lastDigit == 0:
    print("Last digit of", number, "is",lastDigit, "and is 0")
else:
    print("Last digit of", number, "is",lastDigit, "and is less than 6 and not 0")
