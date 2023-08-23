#!/usr/bin/python3
"""
This class represents a square.
"""
class Square:

    """
    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new instance of the Square class.
        area(self): Calculates and returns the area of the square.
        my_print(self): Prints a representation of the square.
        size(self): Getter method to retrieve the size of the square.
        size(self, value): Setter method to set the size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints a representation of the square.

        Prints a square made up of '#' characters. The number of rows and columns in the square is determined by the size.
        If the size is 0, an empty line is printed.
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Setter method to set the size of the square.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If the provided size is not an integer.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        """
        Raises:
        ValueError: If the provided size is less than 0.
        """
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
