#!/usr/bin/python3
""" Check """
from models.square import Square

r = Square(5, 1, 4, 89)
rd = r.to_dictionary()

if rd is None:
    print("to_dictionary is not returning a dictionary")
    exit(1)

key = "y"
value = 4

if rd.get(key) is None:
    print("Missing {} key: {}".format(key, rd))
    exit(1)

if rd.get(key) != value:
    print("Wrong {} value: {}".format(key, rd.get(key)))
    exit(1)

print("OK", end="")
