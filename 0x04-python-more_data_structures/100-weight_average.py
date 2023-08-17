#!/usr/bin/python3
def weight_average(my_list=[]):
    avg = 0
    weight = 0
    score = 0
    for t in my_list:
        score += t[0] * t[1]
        print("score: ", score)
        weight += t[0]
    avg = score / weight
    return (avg)
