#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    else:
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50,
                      "C": 100, "D": 500, "M": 1000}
        sum_roman = 0
        for c in roman_string:
            value = roman_dict.get(c, 0)
            sum_roman += value
        return sum_roman
