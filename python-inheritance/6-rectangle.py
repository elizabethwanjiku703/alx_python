#!/usr/bin/python3
"""import the BaseGeometry class from the 5-base_geometry module:"""
BaseGeometry = __import__("5-base_geometry").BaseGeometry

"""define the Rectangle class and make it inherit from BaseGeometry:"""
class Rectangle(BaseGeometry):
    """"Initialize the Rectangle class"""
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height
