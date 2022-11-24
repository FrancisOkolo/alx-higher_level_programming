#!/usr/bin/python3

"""
    A function that prints out a name followed by a second name
"""


def say_my_name(first_name, last_name=""):
    """ takes 2 argument """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    elif type(last_name) is not str:
        raise TypeError('last_name must be a string')
    else:
        sentence = f"My name is {first_name:s} {last_name:s}"
        print(sentence)
