#!/usr/bin/python3
"""List Division Module

This module defines the list_division function.
"""


def list_division(my_list_1, my_list_2, list_length):
    """List Division

    This function divides element by element from two lists.

    Args:
        my_list_1 (list): The first list of elements.
        my_list_2 (list): The second list of elements.
        list_length (int): The desired length of the resulting list.

    Returns:
        list: A new list with the division results.
    """
    result_list = []
    for i in range(list_length):
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, TypeError):
            quotient = 0
            if (not isinstance(my_list_1[i], (int, float)) or
                    not isinstance(my_list_2[i], (int, float))):
                print("wrong type")
            elif my_list_2[i] == 0:
                print("division by 0")
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            result_list.append(quotient)
    return result_list
