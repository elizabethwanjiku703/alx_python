#!/usr/bin/python3
    """This code defines a function is_same_class that can be used to check if an 
    object obj belongs to a specific class a_class. 
    """
def is_same_class(obj, a_class):
    """
    - obj: The object to check.
    - a_class: The class to compare against.
    """
    if type(obj) == a_class:
        return True
        """
        Returns:
    - True if the type of the object is the same as the specified class.
    - False otherwise.
        """
    else:
        return False
