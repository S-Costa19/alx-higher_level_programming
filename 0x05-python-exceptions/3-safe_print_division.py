#!/usr/bin/python3
"""Safe Print Division Module

This module defines the safe_print_division function.
"""


def safe_print_division(a, b):
    """Safely Print Division

    This function divides two integers and prints the result.

    Args:
        a (int): The dividend.
        b (int): The divisor.

    Returns:
        float: The result of the division, or None if an exception occurred.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
