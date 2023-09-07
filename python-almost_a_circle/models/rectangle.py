#!/usr/bin/python3
"""Rectangle module that contains class rectangle"""

from models.base import Base

class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init the rectangle object with given width and height"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for the rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the rectangle width"""
        if type(value) !=int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the rectangle height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the rectangle x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the rectangle x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the rectangle y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the rectangle y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
