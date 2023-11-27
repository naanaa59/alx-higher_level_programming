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
    for char in ".:?":
        text = ''.join([i + '\n\n' if i == char else i for i in text])
    lines = text.split("\n")
    for i in range(len(lines)):
        lines[i] = ' '.join(lines[i].split())
    text = "\n".join(lines)
    print(text)
