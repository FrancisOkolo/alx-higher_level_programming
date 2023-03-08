#!/usr/bin/python3
'''
Public instance method that validates its arguments
'''


class BaseGeometry:
    ''' A BaseGeometry class'''
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name='', value=0):
        '''A Public instance method  that validates value'''
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
