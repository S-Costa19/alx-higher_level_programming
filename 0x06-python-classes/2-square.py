#!/usr/bin/python3
"""Square Module

This module defines the Square class.
"""


class Square:
    """Square Class

    This class defines a square its size as a private instance attribute.
    """

    def __init__(self, size=0):
        """Initializer

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.__size = size
        self.__check_size()

    def __check_size(self):
        """Size Validation

        This method checks the validity of the size attribute.
        """
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
