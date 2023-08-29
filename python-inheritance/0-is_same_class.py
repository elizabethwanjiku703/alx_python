#!/usr/bin/python3
     """
    class_checker Module:
    provides a function `is_same_class` that can be used to check if an object is exactly an instance of a specified class.
     """
def is_same_class(obj, a_class):
     """
     Checks if an object is exactly an instance of the specified class.
      Parameters:
        obj (object): The object to be checked.
        a_class (class): The specified class to compare the object's type with.
     Returns:
        True if the object is exactly an instance of the specified class, False otherwise.
     """
    if type(obj) == a_class:
        return True
    else:
        return False
