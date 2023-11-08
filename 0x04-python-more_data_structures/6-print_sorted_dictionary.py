#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary.items())
    for i in sorted_dict:
        key, value = i
        print(f"{key}: {value}")
