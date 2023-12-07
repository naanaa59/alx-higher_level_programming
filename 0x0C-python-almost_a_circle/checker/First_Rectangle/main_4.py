#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

r = Rectangle(12, 14, 4, 5, 10)
if r is None:
    print("Can't create Rectangle")
    exit(1)

if r._Rectangle__width != 12:
    print("Wrong width: {}".format(r._Rectangle__width))
    exit(1)

if r._Rectangle__height != 14:
    print("Wrong height: {}".format(r._Rectangle__height))
    exit(1)

if r._Rectangle__x != 4:
    print("Wrong x: {}".format(r._Rectangle__x))
    exit(1)

if r._Rectangle__y != 5:
    print("Wrong y: {}".format(r._Rectangle__y))
    exit(1)

if r.id != 10:
    print("ID is not initialized at 10")
    exit(1)

print("OK", end="")
