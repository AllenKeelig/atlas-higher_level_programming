#!/usr/bin/python3
"""
Containssubclass Rectangle
"""

BaseGeometry = __import__('9-rectangle.py').Rectangle


class Square(BaseGeometry):
    """A rectangle"""
    def __init__(self, width, height):
        def __init__(self, size):
        """Initialize a square with a given size"""
        self.__size = size
