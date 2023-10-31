#!/usr/bin/python3
def uppercase(str):
    for i in range(1, len(str) + 1):
        asci_code = ord(str[i - 1])
        if  96 < asci_code < 123:
          upp  = chr(asci_code - 32)
        else:
            upp = chr(asci_code)
        print("{}".format(upp), end='')
    print()
