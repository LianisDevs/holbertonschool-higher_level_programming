#!/usr/bin/python3
def fizzbuzz():
    lastNum = 101
    for i in range(1, lastNum):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" " if i < lastNum - 1 else "")
        elif i % 3 == 0:
            print("Fizz", end=" " if i < lastNum - 1 else "")
        elif i % 5 == 0:
            print("Buzz", end=" " if i < lastNum - 1 else "")
        else:
            print("{}".format(i), end=" " if i < lastNum - 1 else "")
