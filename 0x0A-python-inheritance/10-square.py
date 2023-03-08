#!/usr/bin/python3
'''
A square that inherits from the Rectangle class
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''this Square class inherits from the
    previous Rectangle class
    '''
    def __init__(self, size):
        self.integer_validator(size, size)
        self.__size = size
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__size, self.__size)
