#!/usr/bin/python3
"""BaseGeometry class with the integer_validator method."""
class BaseGeometry:
    def integer_validator(self, name, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")
"""Rectangle class that inherits from BaseGeometry. """
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        """Implement the area() method, simply multiply the width and height attributes together."""
    def area(self):
        return self.__width * self.__height
    """customize the string representation of the Rectangle object, override the __str__ method to return the desired format."""
    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"



