#!/usr/bin/python3

"""
    a function that prints a text with 2 new lines
"""



def text_indentation(text):
    """function to create indentations"""
    if type(text) is not str:
        raise TypeError('text must be string')
    else:
        for char in ".?:":
            # replaces .?: with itself and newline
            text = text.replace(char, char + "\n\n")
        # changes string to list to strip whitspaces
        list_lines =[lines.strip(' ') for lines in text.split('\n')]
        # returns to string and returns newline
        revised = '\n'.join(list_lines)
        print(revised, end='')
