#!/usr/bin/python3

# Define the Square class
class Square:
    def __init__(self, size=0):
        """
        Constructor method for the Square class.
        Initializes the size attribute of the object.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size**2

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Setter method for the size attribute.
        Checks if the new size is a positive integer.

        Args:
            size (int): The new size of the square.

        Raises:
            TypeError: If the new size is not an integer.
            ValueError: If the new size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
