#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > len(str):
        return str
    copy_str = ""
    for c in str:
        if c == str[n]:
            pass
        else:
            copy_str += c
    return copy_str
