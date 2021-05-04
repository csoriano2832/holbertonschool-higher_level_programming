#!/usr/bin/python3
def multiple_returns(sentence):
    data = [0, ""]

    data[0] = len(sentence)
    try:
        data[1] = sentence[0:1]
    except:
        data[1] = None

    return tuple(data)
