#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def position(self):
        return self.__size

    @position.setter
    def position(self, value):
       if type(value) is not tuple:
           raise TypeError('position must be a tuple of 2 positive integers')
       if len(value) != 2:
           raise TypeError('position must be a tuple of 2 positive integers')
       for item in value:
           if type(item) is not int or item < 0:
               raise TypeError('position must be a tuple of 2 positive integers')
       self.__position = value
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("Size must be an interger")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return (self.__size) ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                if self.__position[0] > 0:
                    for k in range(self.__position[0]):
                        print(" ", end='')
                for j in range(self.__size):
                    print('#', end='')
                print()
