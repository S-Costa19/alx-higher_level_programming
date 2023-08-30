#!/usr/bin/python3
"""Safe Print List of Integers Module

This module defines the safe_print_list_integers function.
"""


def safe_print_list_integers(my_list=[], x=0):
    """Safely Print List of Integers

    This function prints the first x integers from a list.

    Args:
        my_list (list, optional): The list of elements. Defaults to [].
        x (int, optional): The number of elements to access. Defaults to 0.

    Returns:
        int: The real number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError, IndexError):
            continue
    print()
    return count
