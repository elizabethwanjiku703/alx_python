#!/usr/bin/python3
class BaseGeometry:
    """
    A class representing a base geometry.

    Methods:
    - area(): Public instance method that raises an Exception with the message area() is not implemented.
    - integer_validator(name, value): Public instance method that validates an integer value.

    Attributes: None
    """

    def area(self):
        """
        Public instance method that raises an Exception with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates the 'value'.

        Parameters:
        - name: A string representing the name of the value.
        - value: The value to be validated.

        Raises:
        - TypeError: If the 'value' is not an integer.
        - ValueError: If the 'value' is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
