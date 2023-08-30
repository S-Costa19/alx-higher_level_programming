#!/usr/bin/python3
"""Safe Function Execution Module

This module defines the safe_function function.
"""

import sys


def safe_function(fct, *args):
    """Safe Function Execution

    This function executes a given function safely.

    Args:
        fct (function): The function to execute.
        *args: Variable arguments to pass to the function.

    Returns:
        The result of the function, or None if an exception occurred.
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None
