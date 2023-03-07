#!/usr/bin/python3
'''
A function to check if an object is
    is a subclass of a certain class but not a
    direct object of the class
'''


def inherits_from(obj, a_class):
    '''A function to check if an object is
    is a subclass of a certain class but not a
    direct object of the class
    '''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
