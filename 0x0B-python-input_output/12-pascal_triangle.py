#!/usr/bin/python3
'''
This module contains 1 function(s):
-----------------------------------
pascal_triangle(n)

'''


def pascal_triangle(n):
    ''' Returns a list of lists of integers representing
    the Pascal's triangle of n '''

    list_results = []

    if n <= 0:
        return list_results

    for i in range(n):

        row = [1]
        if list_results:
            l_row = list_results[-1]
            row.extend([x + y for x, y in zip(l_row, l_row[1:])])
            row.append(1)
        list_results.append(row)

    return list_results
