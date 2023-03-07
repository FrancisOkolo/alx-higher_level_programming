#!/usr/bin/python3
'''
A python functions that lists all attributes
... of  an object
'''


def lookup(obj):
    ''' list object attributes'''
    att = []
    att.append(dir(obj))
    return att
