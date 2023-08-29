#!/usr/bin/python3
Rectangle = __import__("7-rectangle").Rectangle

class Square(Rectangle):
    """A class representing a square"""
    def __init__(self, size):
        """Initialize a square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
