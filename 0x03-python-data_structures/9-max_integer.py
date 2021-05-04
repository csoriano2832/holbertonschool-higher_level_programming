#!/usr/bin/python3
def max_integer(my_list=[]):
    big_num = 0

    if len(my_list) == 0:
        return None

    for x in range(len(my_list) - 1):
        if my_list[x] > big_num:
            big_num = my_list[x]

    return (big_num)
