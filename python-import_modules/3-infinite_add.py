#!/usr/bin/python3
import sys

if __name__ == "__main__":
    length = len(sys.argv)
    arguments = length - 1
    i = 1
    result = 0

    while (i < length):
        result += int(sys.argv[i])
        i += 1
    print(result)
