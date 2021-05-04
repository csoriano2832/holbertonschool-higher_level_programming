#!/usr/bin/python3
def max_integer(my_list=[]):
    big_num = 0

    if my_list is None:
        return

    for x in range(len(my_list) - 1):
        if my_list[x] > big_num:
            big_num = my_list[x]

    return (big_num)
