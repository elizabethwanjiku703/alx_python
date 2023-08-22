#!/usr/bin/python3
class Square:
    """The class defines a square."""

    def __init__(self, size):
        """
        We initialize the Square object.
        """
        self.__size = size

    def get_size(self):
        """
        We get the size of the square.

       It Returns:
            int: The size of the square.

        """
        return self.__size

    def set_size(self, size):
        """
        Set the size of the square.

        """
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2

