#!/usr/bin/python3
'''
Notes:
        use type() to get specific class
        use isinstance() to get class and any parent classes too
        use issubclass() to get what object is a subclass of
'''


def is_same_class(obj, a_class):
    '''A function to check if an object is
    is an instance of a certain class
    '''
    if type(obj) == a_class:
        return True
    else:
        return False
