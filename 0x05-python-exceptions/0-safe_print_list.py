#!/usr/bin/python3
"""Safe Print List Module

This module defines the safe_print_list function.
"""


def safe_print_list(my_list=[], x=0):
    """Safely Print List

    This function prints a specified number of elements from a list.

    Args:
        my_list (list, optional): The list of elements. Defaults to [].
        x (int, optional): The number of elements to print. Defaults to 0.

    Returns:
        int: The real number of elements printed.
    """
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    finally:
        print()
        return count
