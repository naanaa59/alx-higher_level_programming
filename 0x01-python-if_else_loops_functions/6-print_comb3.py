#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i == j or i > j or (i == 8 and j == 9):
            pass
        else:
            print("{}{}".format(i, j), end=', ')
print("{}{}".format(i - 1, j))
'''print("\n")'''
