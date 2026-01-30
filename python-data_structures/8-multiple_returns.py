#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)

    if length == 0:
        tuple = (0, None)
    else:
        char = sentence[0]
        tuple = (length, char)
    return tuple
