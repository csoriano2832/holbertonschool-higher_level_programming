#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0

    result = 0
    index = 0
    romanNumeralMap = (('M',  1000),
                        ('CM', 900),
                        ('D',  500),
                        ('CD', 400),
                        ('C',  100),
                        ('XC', 90),
                        ('L',  50),
                        ('XL', 40),
                        ('X',  10),
                        ('IX', 9),
                        ('V',  5),
                        ('IV', 4),
                        ('I',  1))

    for numeral, integer in romanNumeralMap:
        while roman_string[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result
