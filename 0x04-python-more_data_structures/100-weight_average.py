#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        f = 0
        s = 0
        for i in my_list:
            x, y = i
            f += x * y
            s += y
        return f / s
    else:
        return 0
