#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv)
    if length == 1:
        print(f"0 arguments.")
    elif length == 2:
        print(f"1 argument:")
        print(f"1: {sys.argv[1]}")
    else:
        print(f"{length - 1} arguments:")
        for i in range(1, length):
            print(f"{i}: {sys.argv[i]}")
