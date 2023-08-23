#!/usr/bin/python3
"""This line defines a class named "Square". """
class Square:
    """
    This is the constructor method for the Square class. 
    It is called when a new object of the class is created.
    """
    def __init__(self, size=0):
        """
        This line checks if the "size" parameter is an instance of the "int" class. 
        If it is not, a TypeError is raised with the message 
        'size must be an integer'.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        """
        This line checks if the "size" parameter is less than 0. 
        If it is, a ValueError is raised with the message 
        'size must be >= 0'.
        """
        if size < 0:
            raise ValueError("size must be >=0")
        """
        This line assigns the value of the "size" parameter to the instance variable "__size".
        The double underscore before the variable name indicates 
        that it is intended to be a private variable, 
        meaning it should not be accessed directly from outside 
        the class.
        """
        self.__size = size
    def area(self):
        """
        Public instance method: 
        def area(self): that returns the current square area"""
        return self.__size **2
    


