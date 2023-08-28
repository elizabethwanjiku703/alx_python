#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Check if an object belongs to a specific class.

    Parameters:
    - obj: The object to check.
    - a_class: The class to compare against.

    Returns:
    - True if the type of the object is the same as the specified class.
    - False otherwise.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
