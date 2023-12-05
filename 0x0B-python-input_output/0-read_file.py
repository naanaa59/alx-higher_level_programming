#!/usr/bin/python3
'''
    This module defines a method called read_file(filename="")
'''


def read_file(filename=""):
    '''
        reads a text file and prints it to stdout
    '''
    with open(filename, encoding="utf-8") as myFile:
        line = myFile.readline()
        while line:
            print(line.strip('\n'))
            line = myFile.readline()
