#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_elements = 0

    try:
        for index in range(x):
            print(my_list[index], end="")
            num_elements += 1
        print()
        return num_elements
    except:
        print()
        return num_elements
