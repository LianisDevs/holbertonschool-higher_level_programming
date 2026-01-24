#!/usr/bin/python3
import sys

if __name__ == "__main__":
    length = len(sys.argv)
    arguments = length - 1

    if arguments == 0:
        print("0 arguments.")
    elif arguments == 1:
        print(arguments, "argument:")
        print("1:", sys.argv[1])
    else:
        i = 1
        print(arguments, "arguments:")
        while (i < length):
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
