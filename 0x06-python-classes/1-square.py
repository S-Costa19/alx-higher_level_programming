#!/usr/bin/python3
"""Square Module

This module defines the Square class.
"""


class Square:
    """Square Class

    This class defines a square its size as a private instance attribute.
    """

    def __init__(self, size):
        """Initializer

        Args:
            size (int): The size of the square.
        """
        self.__size = size
