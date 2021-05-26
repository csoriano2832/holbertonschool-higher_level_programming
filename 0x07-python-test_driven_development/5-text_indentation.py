#!/usr/bin/python3
''' This module defines (1) method(s),
-------------------------------------------

 [text_indentation(text)]

-------------------------------------------
'''


def text_indentation(text):
    '''Prints a text with 2 new lines after each of these characters: . ? :'''

    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = 0
    for letter in text:
        if letter == " " and flag == 1:
            continue
        print(letter, end="")
        flag = 0
        if letter == "." or letter == "?" or letter == ":":
            print("\n")
            flag = 1
