#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == None:
        tuple = (0, None)

    else:
        length = len(sentence)
        char = sentence[0]
        tuple = (length, char)

    return tuple
