#!/usr/bin/python3
def uppercase(str):
    stringUpper = ''

    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            stringUpper = stringUpper + chr(ord(str[i]) - 32)
        else:
            stringUpper = stringUpper + str[i]

    print("{}".format(stringUpper))
