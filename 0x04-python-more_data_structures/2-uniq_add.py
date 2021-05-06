#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is not None:
        unique_list = list(set(my_list))

        accum = 0
        for x in unique_list:
            accum += x

        return accum
