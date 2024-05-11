#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """square class"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        """Initialize a square with a given size"""
        if type(val) is not int:
            raise TypeError("size must be an integer")
        else:
            if val < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = val

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) is 2 and \
            type(value[0]) is int and type(value[1]) is int and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
