#!/usr/bin/python3
"""
Module for checking if an object inherits from a specified class.
"""

def inherits_from(obj, a_class):
    """
    Check if obj inherits from a_class.

    Args:
        obj: The object to check.
        a_class: The specified class to compare against.

    Returns:
        True if obj inherits from a_class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
