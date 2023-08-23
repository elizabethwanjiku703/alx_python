#!/usr/bin/python3
"""
A class represinting a square.
"""
class Square:
    """
    Attribes:
    __size (int): The size of the square 
    """
    def __init__(self,size=0):
        """
        Initializes a Square object.
        Args:
            size (int): The size of the square. 
            Defaults to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
        """Raises:
            TypeError: If size is not an integer.
        """
            raise TypeError("size must be interger")
        if size < 0:
        """ Raises:
            ValueError: If size is less than 0.
        """
            raise ValueError("size must be >= 0")
        self.size = size

