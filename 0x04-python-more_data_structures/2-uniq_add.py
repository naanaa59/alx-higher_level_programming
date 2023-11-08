#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_uniq = set(my_list)
    list_uniq = list(set_uniq)
    result = 0
    for i in range(len(list_uniq)):
        result += list_uniq[i]
    return result
