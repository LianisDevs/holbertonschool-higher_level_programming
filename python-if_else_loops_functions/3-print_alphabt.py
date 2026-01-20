#!/usr/bin/python3
excludedNums = {101, 113}
for i in range(97, 123):
    if i in excludedNums:
        continue
    print("{:c}".format(i), end="")
