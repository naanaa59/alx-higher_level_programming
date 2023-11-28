#!/usr/bin/python3
'''
    This is a module for a function named text_indentation that

    prints a text with 2 new lines after each of these characters: ., ? and :

        '''


def text_indentation(text):
    '''
        prints a text with 2 new lines after each of these characters:
        ., ? and :

        text must be a string, otherwise raise a TypeError
        exception with the message

        There should be no space at the beginning or
        at the end of each printed line
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1

