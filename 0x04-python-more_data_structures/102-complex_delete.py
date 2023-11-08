#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_k = [key for key, val in a_dictionary.items() if val == value]
    for key in del_k:
        del a_dictionary[key]
    return a_dictionary
