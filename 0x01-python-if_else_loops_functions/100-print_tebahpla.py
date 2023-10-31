#!/usr/bin/python3
for i in range(122, 95, -1):
    if 90 < i < 97:
        pass
    else:
        if i % 2 == 0:
            alpha = i
        else:
            alpha = i - 32
        print("{}".format(chr(alpha)), end='')
