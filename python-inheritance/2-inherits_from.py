def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a specified class or any of its subclasses.

    Args:
        obj: The object to check.
        a_class: The specified class to compare against.

    Returns:
        True if the object is an instance of the specified class or any of its subclasses; False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
