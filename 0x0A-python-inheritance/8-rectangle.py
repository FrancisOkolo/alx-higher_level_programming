#!/usr/bin/python3
'''
Contains parent class BaseGeometry
with public instance method area and integer_validator
Contains subclass Rectangle
with instantiation of private attributes width and height, validated by parent
'''


from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    '''A subclass of BaseGeometry'''
    def __init__(self, width, height):
        self.__width = super().integer_validator('width', width)
        self.__height = super().integer_validator('height', height)
