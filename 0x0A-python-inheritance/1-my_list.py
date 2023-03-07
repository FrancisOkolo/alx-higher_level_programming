#!/usr/bin/python3
'''
A class that inherits from python list
'''


class MyList(list):
    '''A class that inherits from Python List'''

    def print_sorted(self, mylist=[]):
        print(sorted(self))
