#!/usr/bin/python3
"""
Module to check if an object is of the same class as specified.
"""

def is_same_class(obj, a_class):
    """
    Check if obj is of the same class as a_class.

    Args:
        obj: Object to check.
        a_class: Class to compare against.

    Returns:
        True if obj is of the same class as a_class, False otherwise.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
