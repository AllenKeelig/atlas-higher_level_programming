#!/usr/bin/python3
"""Defines an integer addition function."""


def matrix_divided(matrix, div):
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(matrix, int) and not isinstance(matrix, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(div, int) and not isinstance(div, float))):
        raise TypeError("b must be an integer")
    return (int(matrix) / int(div))
