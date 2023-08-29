#!/usr/bin/python3
"""A class representing a base geometry."""
class BaseGeometry:
    def area(self):
        """Public instance method that raises an Exception."""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Public instance method that validates the 'value'.
        Raises:
        - TypeError: If the 'value' is not an integer.
        - ValueError: If the 'value' is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
