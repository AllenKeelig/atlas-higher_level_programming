#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """square class"""
    def __init__(self, size=0):
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

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
