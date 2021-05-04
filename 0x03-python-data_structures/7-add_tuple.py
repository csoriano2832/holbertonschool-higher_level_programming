#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = [0, 0]

    for x in range(2):
        try:
            new_tuple[x] += tuple_a[x]
        except:
            new_tuple[x] += 0
        try:
            new_tuple[x] += tuple_b[x]
        except:
            new_tuple[x] += 0

    return tuple(new_tuple)
