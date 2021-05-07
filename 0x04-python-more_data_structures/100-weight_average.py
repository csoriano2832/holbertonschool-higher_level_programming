#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        sum_aritmetic = 0
        sum_weight = 0
        weighted_average = 0

        for score, weight in my_list:
            sum_aritmetic += score * weight
            sum_weight += weight
        weighted_average = sum_aritmetic / sum_weight

        return weighted_average
