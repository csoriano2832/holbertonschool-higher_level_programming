#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        student = ""
        score = 0

        for k, v in a_dictionary.items():
            if v > score:
                score = v
                student = k

        return student
    else:
        return None
