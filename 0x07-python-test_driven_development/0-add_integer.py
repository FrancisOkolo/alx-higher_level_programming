#!/usr/bin/python3

"""
    This is to define a function for adding two integers
"""


def add_integer(a, b=98):
    """ basically to return a+b as int"""
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    elif type(b) is not int and type(b) is not float:
        raise TypeError('a must be an integer')
    else:
        return int(a) + int(b)

