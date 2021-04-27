#!/usr/bin/python3
for leftDigit in range(0, 10):
    for rightDigit in range(0, 10):
        if leftDigit != rightDigit and leftDigit < rightDigit:
            if leftDigit == 8 and rightDigit == 9:
                print("{:d}{:d}".format(leftDigit, rightDigit))
            else:
                print("{:d}{:d}".format(leftDigit, rightDigit), end=", ")
