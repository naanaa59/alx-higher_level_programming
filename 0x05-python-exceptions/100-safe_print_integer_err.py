#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    flag = True
    try:
        print("{:d}".format(value))
    except ValueError as err:
        sys.stderr.write("Exception: {}\n".format(err))
        flag = False
    except TypeError:
        flag = False
    return flag
