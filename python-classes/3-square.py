#!/usr/bin/python3
class Square:
    """
    This line defines a class named "Square".
    """
    def __init__(self, size=0):
        self.__size = size
        """This line checks if the "size" parameter is an instance of the "int" class. 
        This line assigns the value of the "size" parameter to the instance variable "__size".
        """
    @property
    def size(self):
            """The @property decorator is used to define a getter method for the size attribute. 
            This allows to access the size attribute as if it were a regular attribute, 
            using the dot notation (square.size).
            """
            return self.__size
    """
    The @size.setter decorator is used to define a setter method for the size attribute.
    """
    @size.setter
    def size (self, value):
        """ 
        This allows to update the size attribute using the assignment operator 
        (square.size = new_size).
        """
        if not isinstance (value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        """Inside the setter method, type and value checks are performed to ensure that the 
        size attribute is an integer and greater than or equal to 0. If these checks fail, 
        appropriate exceptions (TypeError and ValueError) are raised.
        """
    def area(self):
             """
             The area method calculates and returns the area of the square.
             """
             return self.__size **2

