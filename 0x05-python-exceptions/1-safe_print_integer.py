#!/usr/bin/python3
"""Safe Print Integer Module

This module defines the safe_print_integer function.
"""


def safe_print_integer(value):
    """Safely Print Integer

    This function prints an integer using the "{:d}".format() method.

    Args:
        value: The value to be printed.

    Returns:
        bool: True if value is an integer and correct, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
