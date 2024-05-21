#!/usr/bin/python3
"""
Contains subclass Square that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """A rectangle"""
    def __init__(self, size):
        """Initialize a square with a given size"""
        self.__size = size
