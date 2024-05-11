#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """square class"""
    def __init__(self, size=0):
        self.size=size

    @property
    def size(self):
        return self.__size

    @size.setter
    def __init__(self, size=0):
        """Initialize a square with a given size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        return self.__size ** 2
