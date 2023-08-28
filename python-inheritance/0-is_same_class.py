#!/usr/bin/python3
    """ A definition is made to check if an object is exactly an instance of a specified class
    """
def is_same_class(obj, a_class):
    """
    Parameters:
    obj (any): The object to be checked.
    a_class (class): The class to compare against.

    Returns:
    bool: True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) == a_class
